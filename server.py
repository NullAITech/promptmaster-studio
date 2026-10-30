#!/usr/bin/env python3
"""
PromptMaster Studio - Sovereign Standalone REST API & Web Workstation Server
Listens on http://127.0.0.1:8123 by default.
"""

import os
import sys
from pathlib import Path

# Ensure src/ is on PYTHONPATH
ROOT_DIR = Path(__file__).resolve().parent
SRC_DIR = ROOT_DIR / "src"
PUBLIC_DIR = ROOT_DIR / "public"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from promptmaster_studio.ui_server import start_server

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8123))
    host = os.environ.get("HOST", "127.0.0.1")
    print(f"⚡ Starting PromptMaster Studio on http://{host}:{port} ...")
    start_server(host=host, port=port, open_browser=False, public_dir=PUBLIC_DIR)
