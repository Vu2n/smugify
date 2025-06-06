import sys
import inspect

def cli():
    frame = inspect.stack()[1]
    mod = inspect.getmodule(frame[0])
    main = [obj for name, obj in vars(mod).items() if callable(obj) and name == "main"]
    if not main:
        print("No main() function found for CLI.")
        return
    from argparse import ArgumentParser
    func = main[0]
    sig = inspect.signature(func)
    parser = ArgumentParser()
    for name, param in sig.parameters.items():
        param_type = param.annotation if param.annotation != inspect.Parameter.empty else str
        parser.add_argument(f"--{name}", type=param_type, default=param.default)
    args = parser.parse_args()
    func(**vars(args))
