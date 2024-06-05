def ft_tqdm(lst: range):
    """Print a progress bar given an object of type 'range'"""
    if not isinstance(lst, range):
        raise TypeError("lst has to be of type 'range'")

    fill = "█"
    count = 1

    for itr in lst:
        ratio = count / lst.stop
        percentage = '{:>4.0%}'.format(ratio)
        bar = '{:<50}'.format(fill * int(ratio * 50))
        trail = " {:>3}/{:>3}".format(count, lst.stop)
        count += 1

        print(percentage, bar, trail, sep="|", end="\r")
        yield itr
