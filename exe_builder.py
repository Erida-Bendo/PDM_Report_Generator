import os
import subprocess
import sys

# Get the path to the current script's directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Get the path to the user's desktop
desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")


BHlogo=os.path.join(script_dir, 'BH.jpg')
# Construct the correct --add-data argument
if sys.platform.startswith('win'):
    add_data_arg = f"{BHlogo};."
else:
    add_data_arg = f"{BHlogo}:."

command = [
    'pyinstaller',
    '--noconfirm',
    '--onefile',
    '--noconsole',
    '--icon', os.path.join(script_dir, 'resources\logo.png'),
    '--add-data', add_data_arg,
    os.path.join(script_dir, 'PDM_GEN.py'),
    '--distpath', desktop_dir
]

print("Running PyInstaller with the following command:")
print(" ".join(command))

result = subprocess.run(command, capture_output=True, text=True)

print("PyInstaller Output:")
print(result.stdout)

if result.returncode != 0:
    print("Error occurred:")
    print(result.stderr)
else:
    print("PyInstaller completed successfully.")