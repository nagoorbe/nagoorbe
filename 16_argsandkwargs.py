def print_args_kwargs(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

print_args_kwargs(10, 20, 30, name="Alice", age=25)
