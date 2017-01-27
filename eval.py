def eval(m, n, a):
    r"""
    Given: A positive integer m (m <= 10), a positive integer n (n <= 10,000),
    and an array A of length at most 20 containing real numbers between 0 and 
    1, inclusively.

    Return: An array B in which B[i] represents the expected number of
    substring matches of a random string t of length m as a substring of
    random string s of length n, where both are formed from GC-content A[i]
    (see "Introduction to Probability"). Each value in B should be accurate to
    three decimal places.
    """
    return " ".join("{:.6f}".format((n-m+1) * (x**2 - x + 0.5)**m) for x in a)


if __name__ == "__main__":
    assert(eval(2, 10, [0.32, 0.42, 0.81]) == "0.717748 0.591669 1.078067")

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data_file:
            m, n = map(int, data_file.readline().rstrip().split())
            a = map(float, data_file.readline().rstrip().split())
            print eval(m, n, a)