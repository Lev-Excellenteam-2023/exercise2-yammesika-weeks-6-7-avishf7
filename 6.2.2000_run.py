import time


def timer(func, *args, **kwargs):
    """
    Measures the execution time of a given function.

    :param func: The function to be timed.
    :param args: Positional arguments to be passed to the function.
    :param kwargs: Keyword arguments to be passed to the function.

    :return: The elapsed time in seconds.
    """
    start = time.time()
    func(*args, **kwargs)
    end = time.time()

    return end - start


print(timer(print, "Hello"))

print(timer(zip, [1, 2, 3], [4, 5, 6]))

print(timer("Hi {name}".format, name="Bug"))
