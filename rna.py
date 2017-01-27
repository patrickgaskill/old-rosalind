def rna(dna_string):
    r"""
    An RNA string is formed from the alphabet containing A, C, G, and U.

    Given a DNA string t corresponding to a coding strand, its transcribed RNA 
    string u is formed by replacing all occurrences of T with U.

    Given: A DNA string t of length at most 1000 nucleotides.

    Return: The transcribed RNA string of t.
    """
    return dna_string.replace("T", "U")

if __name__ == "__main__":
    assert(rna("GATGGAACTTGACTACGTAAATT") == "GAUGGAACUUGACUACGUAAAUU")

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as dna_file:
            print rna(dna_file.read())