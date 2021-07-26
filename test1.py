def decorate_func(to_dec):
    print("Starting decoration")

    to_dec()

    print("additional work done")


@decorate_func
def base_func():
    print("this is the base function")

base_func