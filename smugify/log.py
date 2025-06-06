from datetime import datetime
import sys

def log(message, level="info"):
    colors = {
        "info": "\033[94m",    # Blue
        "warn": "\033[93m",    # Yellow
        "error": "\033[91m",   # Red
        "debug": "\033[90m",   # Gray
    }
    emoji = {
        "info": "ℹ️",
        "warn": "⚠️",
        "error": "❌",
        "debug": "🐛",
    }
    color = colors.get(level, "\033[0m")
    icon = emoji.get(level, "💬")
    now = datetime.now().strftime("%H:%M:%S")
    print(f"{color}[{now}] {icon} {message}\033[0m", file=sys.stderr if level=="error" else sys.stdout)
