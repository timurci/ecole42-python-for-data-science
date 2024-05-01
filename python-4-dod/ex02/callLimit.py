def callLimit(limit: int):
    """Return a decorator"""
    count = 0

    def callLimiter(function):
        """Return a wrapper"""

        def limit_function(*args: any, **kwds: any):
            """Call `function` limited number of times and return its values"""
            nonlocal count
            if (count >= limit):
                # raise Exception(repr(function) + " called too many times")
                print("Error:", repr(function), "called too many times")
                return
            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter
