def uniform_num(n):
    """
    uniform_num(n)
    """
    if n == 1:
        return 1
    else:
        return n * uniform_num(n - 1)


uniform_num(5)
