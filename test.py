import os
import subprocess
import sys

for root, dirs, files in os.walk(os.path.join(".", "trajectory_planning_helpers"), topdown=False):
    for name in files:
        if name == "__init__.py" or ".pyc" in name:
            continue
        file_path = os.path.join(root, name)
        print(f"Testing {name}")
        process = subprocess.run([sys.executable, file_path], capture_output=True, text=True)
        if process.returncode == 0:
            print(f"Execution of {name} successful.")
            if process.stdout:
                print("Output:")
                print(process.stdout)
        else:
            print(f"Error: Failed to execute '{file_path}'.", file=sys.stderr)
            print("Error output:", file=sys.stderr)
            print(process.stderr, file=sys.stderr)
