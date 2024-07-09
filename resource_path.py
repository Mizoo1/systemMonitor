# test_resource_path.py
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    final_path = os.path.join(base_path, relative_path)
    print(f"Resource path resolved to: {final_path}")
    return final_path

if __name__ == '__main__':
    print(resource_path('icons/cpu.png'))
