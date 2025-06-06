import platform
import os

def notify(message):
    system = platform.system()
    if system == "Darwin":
        os.system(f"osascript -e 'display notification \"{message}\" with title \"Smugify Alert\"'")
    elif system == "Linux":
        os.system(f"notify-send 'Smugify Alert' '{message}'")
    elif system == "Windows":
        from win10toast import ToastNotifier
        ToastNotifier().show_toast("Smugify Alert", message, duration=3)
    else:
        print(f"\a🔔 {message}")  # Fallback bell
