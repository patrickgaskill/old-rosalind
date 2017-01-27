def subs(s, t):
    r"""
    Given: Two DNA strings s and t (each of length at most 1 kbp).

    Return: All locations of t as a substring of s.
    """
    import re
    return " ".join(str(m.start() + 1) for m in \
        re.finditer(r"(?={0})".format(re.escape(t)), s))

if __name__ == "__main__":
    assert(subs("ACGTACGTACGTACGT", "GTA") == "3 7 11")

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data_file:
            print subs(data_file.readline(), data_file.readline())