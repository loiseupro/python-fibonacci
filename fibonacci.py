def fibonacci(limit):
    """ Returns numbers from the Fibonacci sequence.

    Parameters
    ----------
    limit : int, required
        The num of items to return

    Returns
    -------
    tuple
        a tuple of numbers

    """

    sequence = ();
    if(limit == 0): sequence = (0)
    if(limit > 1): sequence = (0, 1)

    for i in range(2, limit):    
        sequence = sequence + (sequence[i-1] + sequence[i-2],)   

    return sequence


# Example of use. Return 8 first number of Fibonacci sequence
res = fibonacci(8)
print(res)
