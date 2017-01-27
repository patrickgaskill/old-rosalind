def lexf(alphabet, n):
    r"""
    Given: A collection of at most 10 symbols defining an ordered alphabet,
    and a positive integer n (n <= 10).

    Return: All strings of length n that can be formed from the alphabet,
    ordered lexicographically.
    """
    from itertools import product
    return "\n".join(map(''.join, product(alphabet, repeat=n)))

if __name__ == "__main__":
    assert(lexf("TAGC", 2) == \
"""TT
TA
TG
TC
AT
AA
AG
AC
GT
GA
GG
GC
CT
CA
CG
CC""")
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data_file:
            print lexf(data_file.readline().rstrip().split(), \
                int(data_file.readline().rstrip()))