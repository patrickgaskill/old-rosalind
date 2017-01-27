def inod(n):
    r"""
    Given: A positive integer n (3 <= n <= 10000).

    Return: The number of internal nodes of any unrooted binary tree having
    n leaves.
    """
    return n - 2

if __name__ == "__main__":
    assert(inod(4) == 2)

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data:
            n = int(data.readline().rstrip())
            print inod(n)