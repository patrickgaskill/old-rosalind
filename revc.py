def revc(dna_string):
    r"""
    In a DNA string, the complement of A is T, and the complement of C is G.

    The reverse complement of a DNA string s is the string sc formed by
    reversing the symbols of s, then taking the complement of each symbol
    (e.g., the reverse complement of GTCA is TGAC).

    Given: A DNA string s of length at most 1000 bp.

    Return: The reverse complement of s.
    """
    import string
    return dna_string.translate(string.maketrans("ATCG", "TAGC"))[::-1]

if __name__ == "__main__":
    assert(revc("AAAACCCGGT") == "ACCGGGTTTT")

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as dna_file:
            print revc(dna_file.read())