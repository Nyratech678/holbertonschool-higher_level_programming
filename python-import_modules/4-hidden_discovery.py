#!/usr/bin/python3
from importlib.machinery import SourcelessFileLoader

if __name__ == "__main__":
    module = SourcelessFileLoader("hidden_4", "/tmp/hidden_4.pyc").load_module()
    names = [name for name in dir(module) if not name.startswith("__")]
    for name in sorted(names):
        print(name)
