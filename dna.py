def dna(dna_string):
    r"""
    A string is simply an ordered collection of symbols selected from some
    alphabet and formed into a word; the length of a string is the number of
    symbols that it contains.

    An example of a DNA string (whose alphabet contains the symbols A, C, G,
    and T) is "ATGCTTCAGAAAGGTCTTACG".

    Given: A DNA string s of length at most 1000 nt.

    Return: Four integers separated by space corresponding to the number of
    times that the symbols A, C, G, and T occur in s.
    """
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in dna_string:
        counts[char] += 1
    return "{A} {C} {G} {T}".format(A=counts['A'], C=counts['C'],
                                    G=counts['G'], T=counts['T'])

if __name__ == "__main__":
    assert(dna("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC") == "20 12 17 21")

    import sys
    dna_file = open(sys.argv[1], 'r')
    print dna(dna_file.read())