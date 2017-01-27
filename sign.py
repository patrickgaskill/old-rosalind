def sign(n):
    r"""
    Given: A positive integer n <= 6.

    Return: The total number of signed permutations of length n, followed by a
    list of all such permutations (you may list the signed permutations in any
    order).
    """
    from itertools import imap, permutations, product
    from operator import mul
    stringify = lambda p: " ".join(imap(str, p))

    perms = permutations(range(1, n+1))
    signs = product((-1, 1), repeat=n)
    signed_perms = [imap(mul, p, s) for (p,s) in product(perms, signs)]

    return str(len(signed_perms)) + "\n" + "\n".join(imap(stringify, signed_perms))

if __name__ == "__main__":
    assert(sign(int("2")) == \
"""8
-1 -2
-1 2
1 -2
1 2
-2 -1
-2 1
2 -1
2 1""")

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data:
            print sign(int(data.readline()))