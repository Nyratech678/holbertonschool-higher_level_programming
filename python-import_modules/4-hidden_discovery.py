#!/usr/bin/python3
if __name__ == "__main__":
    from importlib.machinery import SourcelessFileLoader
    loader = SourcelessFileLoader("hidden_4", "/tmp/hidden_4.pyc")
    module = loader.load_module()
    names = [name for name in dir(module) if not name.startswith("__")]
    for name in sorted(names):
        print(name)
