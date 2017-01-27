def cons(strings):
    r"""
    Given: A collection of at most 10 DNA strings of equal length (at most
    1 kbp).

    Return: A consensus string and profile matrix for the collection. (If
    several possible consensus strings exist, then you may return any one of
    them.)
    """
    from collections import Counter

    counters = map(Counter, zip(*strings))
    consensus = "".join(c.most_common(1)[0][0] for c in counters)
    profile_matrix = "\n".join(b + ": " + \
        " ".join(str(c[b]) for c in counters) for b in "ACGT")

    return consensus + "\n" + profile_matrix

if __name__ == "__main__":
    assert(cons(['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT', \
        'ATGCCATT', 'ATGGCACT']) == \
"""ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6""")

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data_file:
            print cons(data_file.read().split("\n"))