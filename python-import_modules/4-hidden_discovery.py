#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "hidden_4", "/tmp/hidden_4.pyc")
    if spec is not None and spec.loader is not None:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        names = [name for name in dir(module) if not name.startswith("__")]
        for name in sorted(names):
            print(name)
