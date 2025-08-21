import subprocess
import os
import sys

try:
    # Flags to prevent a new terminal window on Windows
    creationflags = 0
    if sys.platform == "win32":
        creationflags = subprocess.CREATE_NO_WINDOW

    process = subprocess.Popen(
        ["go", "run", "main.go"],
        cwd=r"D:\whatsapp-mcp\whatsapp-bridge",
        stdout=subprocess.PIPE,   # Capture logs if you want
        stderr=subprocess.PIPE,
        creationflags=creationflags
    )

    print(f"Go server started in background with PID {process.pid}")

except Exception as e:
    print("An unexpected error occurred:", e)
