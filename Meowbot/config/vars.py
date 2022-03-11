# Configs imports from here

import os

ENV = bool(os.environ.get("ENV", False))

if not ENV and os.path.exists("config.py") or ENV:
    pass

# Meowbot
