def perm(n):
    r"""
    A permutation of length n is some ordering of the positive integers
    {1,2,...,n}. For example, pi=(5,3,2,1,4) is a permutation of length 5.

    Given: A positive integer n <= 7.

    Return: The total number of permutations of length n, followed by a list
    of all such permutations (in any order).
    """
    from math import factorial
    from itertools import imap, permutations
    stringify = lambda p: " ".join(imap(str, p))

    return str(factorial(int(n))) + "\n" + \
           "\n".join(imap(stringify, permutations(range(1, int(n)+1))))

if __name__ == "__main__":
    assert(perm("3") == \
"""6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1""")

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data:
            print perm(data.readline())