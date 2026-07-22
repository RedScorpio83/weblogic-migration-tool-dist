import os
import sys
import json
import base64
import subprocess

def ensure_dependencies():
    needed = []
    try:
        import paramiko
    except ImportError:
        needed.append("paramiko")
    try:
        import dotenv
    except ImportError:
        needed.append("python-dotenv")
    
    if needed:
        print("[BRIDGE AUTO-INSTALL] Rilevati moduli Python mancanti: " + ", ".join(needed) + ". Installazione automatica via pip...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install"] + needed)
            print("[BRIDGE AUTO-INSTALL] Moduli installati con successo!")
        except Exception as e:
            print("[BRIDGE AUTO-INSTALL WARN] Impossibile autoinstallare i moduli via pip: " + str(e))

ensure_dependencies()

import paramiko
try:
    from dotenv import load_dotenv
    load_dotenv('.env')
except Exception:
    pass

def get_ssh():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    password = os.getenv('SSH_DEFAULT_PASSWORD') or os.getenv('PROXMOX_PASSWORD') or 'root'
    ssh.connect('192.168.10.217', port=22, username='root', password=password)
    return ssh

def extract_domain(target_ip, output_dump_dir=None):
    vmid = "114" if "240" in target_ip else "115"
    container = "real_weblogic11" if "240" in target_ip else "real_weblogic12"
    pass_wls = "Weblogic123!" if "240" in target_ip else "p5KLXBan"
    
    extract_wlst = """
connect('weblogic', '""" + pass_wls + """', 't3://localhost:7001')
domainConfig()

def to_json_str(val):
    if val is None:
        return 'null'
    s_val = str(val)
    if s_val == 'True' or s_val == 'true':
        return 'true'
    if s_val == 'False' or s_val == 'false':
        return 'false'
    t = type(val).__name__
    if t in ('int', 'long', 'float', 'PyInteger', 'PyLong'):
        return str(val)
    if t in ('list', 'tuple'):
        res = []
        for x in val:
            res.append(to_json_str(x))
        return '[' + ', '.join(res) + ']'
    if t == 'dict':
        res = []
        for k, v in val.items():
            res.append(to_json_str(k) + ':' + to_json_str(v))
        return '{' + ', '.join(res) + '}'
    return '"' + str(val).replace('\\\\', '\\\\\\\\').replace('"', '\\\\"') + '"'

machines = []
try:
    machines = [m.getName() for m in cmo.getMachines()]
except Exception, e:
    pass

clusters = []
try:
    for c in cmo.getClusters():
        clusters.append({'name': c.getName(), 'servers': []})
except Exception, e:
    pass

servers = []
try:
    for s in cmo.getServers():
        m_name = None
        if s.getMachine():
            m_name = s.getMachine().getName()
        c_name = None
        if s.getCluster():
            c_name = s.getCluster().getName()
        
        listen_addr = s.getListenAddress()

        ss = s.getServerStart()
        jvm_args = None
        classpath = None
        java_vendor = None
        java_home = None
        bea_home = None
        root_dir = None
        auto_restart = True
        if ss:
            jvm_args = ss.getArguments()
            classpath = ss.getClassPath()
            java_vendor = ss.getJavaVendor()
            java_home = ss.getJavaHome()
            bea_home = ss.getBeaHome()
            root_dir = ss.getRootDirectory()
            if hasattr(ss, 'getAutoRestart'):
                auto_restart = ss.getAutoRestart()
            
        ssl = s.getSSL()
        ssl_port = None
        ssl_enabled = False
        if ssl:
            ssl_port = ssl.getListenPort()
            ssl_enabled = ssl.isEnabled()

        servers.append({
            'name': s.getName(),
            'port': s.getListenPort(),
            'listenAddress': listen_addr,
            'machine': m_name,
            'cluster': c_name,
            'jvmArgs': jvm_args,
            'classpath': classpath,
            'javaVendor': java_vendor,
            'javaHome': java_home,
            'beaHome': bea_home,
            'rootDirectory': root_dir,
            'autoRestart': auto_restart,
            'sslPort': ssl_port,
            'sslEnabled': ssl_enabled
        })
        if c_name:
            for cl in clusters:
                if cl['name'] == c_name:
                    cl['servers'].append(s.getName())
except Exception, e:
    pass

domain_dir = cmo.getRootDirectory()
decrypted_pwds = {}
try:
    import os, glob
    from weblogic.security.internal import SerializedSystemIni
    from weblogic.security.internal.encryption import ClearOrEncryptedService
    encryption_service = SerializedSystemIni.getEncryptionService(domain_dir)
    ces = ClearOrEncryptedService(encryption_service)
    jdbc_files = glob.glob(domain_dir + '/config/jdbc/*.xml')
    for f in jdbc_files:
        content = open(f).read()
        if '<password-encrypted>' in content:
            enc_val = content.split('<password-encrypted>')[1].split('</password-encrypted>')[0].strip()
            ds_name = os.path.basename(f).split('-')[0]
            pwd = ces.decrypt(enc_val)
            decrypted_pwds[ds_name] = pwd
except Exception, e:
    pass

datasources = []
try:
    for ds in cmo.getJDBCSystemResources():
        res_m = ds.getJDBCResource()
        ds_p = res_m.getJDBCDataSourceParams()
        jndi = ""
        if ds_p and ds_p.getJNDINames():
            jndi = ds_p.getJNDINames()[0]
        drv_p = res_m.getJDBCDriverParams()
        url = ""
        usr = "db_user"
        driver_name = "oracle.jdbc.OracleDriver"
        if drv_p:
            url = drv_p.getUrl()
            if drv_p.getDriverName():
                driver_name = drv_p.getDriverName()
            if drv_p.getProperties():
                for prop in drv_p.getProperties().getProperties():
                    if prop.getName() == 'user':
                        usr = prop.getValue()
        
        cp = res_m.getJDBCConnectionPoolParams()
        init_cap = 5
        max_cap = 15
        cap_inc = 1
        test_tbl = ""
        test_res = False
        stmt_cache = 10
        conn_tout = 10
        if cp:
            init_cap = cp.getInitialCapacity()
            max_cap = cp.getMaxCapacity()
            cap_inc = cp.getCapacityIncrement()
            test_tbl = cp.getTestTableName()
            test_res = cp.isTestConnectionsOnReserve()
            stmt_cache = cp.getStatementCacheSize()
            conn_tout = cp.getConnectionReserveTimeoutSeconds()

        tgt = None
        if ds.getTargets():
            tgt = ds.getTargets()[0].getName()
        
        pwd = decrypted_pwds.get(ds.getName(), '*****')
        
        datasources.append({
            'name': ds.getName(),
            'jndi': jndi,
            'url': url,
            'user': usr,
            'password': pwd,
            'target': tgt,
            'driverClassName': driver_name,
            'initialCapacity': init_cap,
            'maxCapacity': max_cap,
            'capacityIncrement': cap_inc,
            'testTableName': test_tbl,
            'testConnectionsOnReserve': test_res,
            'statementCacheSize': stmt_cache,
            'connectionReserveTimeout': conn_tout
        })
except Exception, e:
    pass

applications = []
try:
    for app in cmo.getAppDeployments():
        tgt = None
        all_targets = []
        if app.getTargets():
            tgt = app.getTargets()[0].getName()
            all_targets = [t.getName() for t in app.getTargets()]
        
        stg = "stage"
        if hasattr(app, 'getStagingMode'):
            stg = app.getStagingMode()
        order = 100
        if hasattr(app, 'getDeploymentOrder'):
            order = app.getDeploymentOrder()
        sec_model = "DDOnly"
        if hasattr(app, 'getSecurityDDModel'):
            sec_model = app.getSecurityDDModel()
        mod_type = "war"
        if hasattr(app, 'getModuleType'):
            mod_type = app.getModuleType()

        applications.append({
            'name': app.getName(),
            'target': tgt,
            'targets': all_targets,
            'path': app.getSourcePath(),
            'stagingMode': stg,
            'deploymentOrder': order,
            'securityDDModel': sec_model,
            'moduleType': mod_type
        })
except Exception, e:
    pass

res = {
    'name': cmo.getName(),
    'machines': [{'name': m} for m in machines],
    'clusters': clusters,
    'servers': servers,
    'datasources': datasources,
    'applications': applications
}

print "===JSON_RESULT_START==="
print to_json_str(res)
print "===JSON_RESULT_END==="
exit()
"""
    b64 = base64.b64encode(extract_wlst.encode('utf-8')).decode('ascii')
    wlst_path = "/root/Oracle/Middleware/wlserver_10.3/common/bin/wlst.sh" if "240" in target_ip else "/u01/oracle/oracle_common/common/bin/wlst.sh"
    
    cmd = f"""pct exec {vmid} -- docker exec {container} bash -c "mkdir -p /tmp/wlst && echo '{b64}' | base64 -d > /tmp/wlst/extract.py && {wlst_path} /tmp/wlst/extract.py" """
    
    ssh = get_ssh()
    _, stdout, stderr = ssh.exec_command(cmd)
    out_str = stdout.read().decode('utf-8', errors='ignore')
    
    if "===JSON_RESULT_START===" in out_str and "===JSON_RESULT_END===" in out_str:
        json_str = out_str.split("===JSON_RESULT_START===")[1].split("===JSON_RESULT_END===")[0].strip()
        data = json.loads(json_str)

        # Scarica automaticamente i file applicativi (.war, .ear, .jar) nella cartella apps/
        if output_dump_dir:
            apps_dir = os.path.join(output_dump_dir, "apps")
            if not os.path.exists(apps_dir):
                os.makedirs(apps_dir)
            for app in data.get('applications', []):
                src_path = app.get('path')
                if src_path:
                    fn = os.path.basename(src_path)
                    dst_app_file = os.path.join(apps_dir, fn)
                    try:
                        dl_cmd = f"""pct exec {vmid} -- docker exec {container} bash -c "cat '{src_path}' | base64 -w 0" """
                        _, dl_stdout, _ = ssh.exec_command(dl_cmd)
                        b64_content = dl_stdout.read().decode('utf-8', errors='ignore').strip()
                        if b64_content:
                            with open(dst_app_file, 'wb') as f_app:
                                f_app.write(base64.b64decode(b64_content))
                            print(f"[SSH HARVEST] Scaricata applicazione {fn} ({os.path.getsize(dst_app_file)} bytes) -> {dst_app_file}")
                    except Exception as e_dl:
                        print(f"[SSH HARVEST WARN] Impossibile scaricare {src_path}: {e_dl}")
        ssh.close()
        return data
    else:
        ssh.close()
        raise RuntimeError("Failed to extract WLST domain json: " + out_str)

def apply_wlst(target_ip, script_file, wls_url="t3://localhost:7001", wls_user="weblogic", wls_pass="p5KLXBan"):
    vmid = "115" if "197" in target_ip else "114"
    container = "real_weblogic12" if "197" in target_ip else "real_weblogic11"
    wlst_path = "/u01/oracle/oracle_common/common/bin/wlst.sh" if "197" in target_ip else "/root/Oracle/Middleware/wlserver_10.3/common/bin/wlst.sh"
    
    with open(script_file, 'r', encoding='utf-8') as f:
        script_content = f.read()

    b64 = base64.b64encode(script_content.encode('utf-8')).decode('ascii')
    
    if not wls_url.startswith("t3://"):
        wls_url = "t3://" + wls_url

    ssh = get_ssh()

    # Se la cartella del task contiene apps/, carica tutti i file WAR/EAR su /tmp/apps/ nel container remoto
    task_dir = os.path.dirname(os.path.abspath(script_file))
    local_apps_dir = os.path.join(task_dir, "apps")
    if os.path.exists(local_apps_dir) and os.path.isdir(local_apps_dir):
        mkdir_cmd = f"""pct exec {vmid} -- docker exec {container} bash -c "mkdir -p /tmp/apps" """
        ssh.exec_command(mkdir_cmd)
        for app_fn in os.listdir(local_apps_dir):
            app_fp = os.path.join(local_apps_dir, app_fn)
            if os.path.isfile(app_fp):
                with open(app_fp, 'rb') as f_app:
                    app_b64 = base64.b64encode(f_app.read()).decode('ascii')
                up_cmd = f"""pct exec {vmid} -- docker exec {container} bash -c "echo '{app_b64}' | base64 -d > '/tmp/apps/{app_fn}'" """
                ssh.exec_command(up_cmd)
                print(f"[SSH UPLOAD] Caricata applicazione in remoto sul target: /tmp/apps/{app_fn}")

    cmd = f"""pct exec {vmid} -- docker exec {container} bash -c "mkdir -p /tmp/wlst && echo '{b64}' | base64 -d > /tmp/wlst/apply.py && cd /tmp/wlst && {wlst_path} /tmp/wlst/apply.py '{wls_url}' '{wls_user}' '{wls_pass}'" """
    
    _, stdout, stderr = ssh.exec_command(cmd)
    out_str = stdout.read().decode('utf-8', errors='ignore')
    err_str = stderr.read().decode('utf-8', errors='ignore')
    ssh.close()
    
    print("STDOUT:\n", out_str)
    if err_str:
        print("STDERR:\n", err_str)
    return out_str

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "extract":
        dump_target = sys.argv[3] if len(sys.argv) > 3 else None
        res = extract_domain(sys.argv[2], dump_target)
        print(json.dumps(res, indent=2))
    elif len(sys.argv) > 3 and sys.argv[1] == "apply":
        script_file = sys.argv[3]
        wls_url = sys.argv[4] if len(sys.argv) > 4 else "t3://localhost:7001"
        wls_user = sys.argv[5] if len(sys.argv) > 5 else "weblogic"
        wls_pass = sys.argv[6] if len(sys.argv) > 6 else "p5KLXBan"
        
        apply_wlst(sys.argv[2], script_file, wls_url, wls_user, wls_pass)
