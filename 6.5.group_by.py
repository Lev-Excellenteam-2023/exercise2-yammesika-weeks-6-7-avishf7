def group_by(func, *iterable):
    """
    Groups the items in the given iterables based on the output of the given function.

    :param func: A function that takes one argument and returns a hashable object. This function is applied to each
        item in the iterables to determine the key for grouping.
    :param iterable: One or more iterable objects whose items will be grouped according to the output of the `func`
        function. The iterables can contain any type of object.
    :return: A dictionary where each key corresponds to a unique output of the `func` function and the value is a
        list of items that produce that output.
    """

    keys_set = {func(it) for it in list(*iterable)}
    return {key: [it for it in list(*iterable) if func(it) == key] for key in keys_set}
