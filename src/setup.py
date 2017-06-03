import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"build_exe":"../dist", "include_files": ["help.png", "icon.png", "mainMenu.png", "pause.png", "playerCar.png", "policeCar.png", "road.png", "trafficCone.png"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable('TurbulentTailing.py', base=base)
]

setup(  name='TurbulentTailing',
        version='0.1',
        description='A car chase game where you avoid obstacles and try not to get captured.',
        options = {"build_exe": build_exe_options},
        executables = executables)
