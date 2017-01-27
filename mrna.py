def mrna(protein):
    r"""
    Given: A protein string of length at most 1000 aa.

    Return: The total number of different RNA strings from which the protein
    could have been translated, modulo 1,000,000. (Don't neglect the importance
    of the stop codon in protein translation.)
    """
    from operator import mul

    aa = {'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4, 'H': 2,
          'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4,
          'A': 4, 'D': 2, 'E': 2, 'G': 4}

    return reduce(mul, map(aa.get, protein) + [3]) % 1000000

if __name__ == "__main__":
    assert(mrna("MA") == 12)

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data:
            print mrna(data.read())