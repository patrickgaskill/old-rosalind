def hamm(s1, s2):
    r"""
    Given two strings s and t of equal length, the Hamming distance between
    s and t, denoted dH(s,t), is the number of corresponding symbols that
    differ in s and t. See Figure 2.

    Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

    Return: The Hamming distance dH(s,t).
    """
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

if __name__ == "__main__":
    assert(hamm("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7)

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as dna_file:
            print hamm(dna_file.readline(), dna_file.readline())