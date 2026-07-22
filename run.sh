#!/bin/bash
# ==========================================================================
# WEBLOGIC MIGRATION TOOL - PORTABLE LINUX LAUNCHER
# Nimis Consulting Information Technologies
# ==========================================================================

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

if [ -f "$SCRIPT_DIR/jdk/bin/java" ]; then
    JAVA_EXEC="$SCRIPT_DIR/jdk/bin/java"
else
    JAVA_EXEC="java"
fi

echo "Avvio WebLogic Migration Tool (FlatLaf Gold)..."
"$JAVA_EXEC" -jar "$SCRIPT_DIR/MigrationTool.jar" "$@"
