def prot(rna):
    r"""
    Given: An RNA string s corresponding to a strand of mRNA (of length at
    most 10 kbp).

    Return: The protein string encoded by s.
    """
    codon_dict = {
        'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F', 'CUC': 'L',
        'AUC': 'I', 'GUC': 'V', 'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
        'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V', 'UCU': 'S', 'CCU': 'P',
        'ACU': 'T', 'GCU': 'A', 'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'UCG': 'S', 'CCG': 'P',
        'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
        'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'CAA': 'Q', 'AAA': 'K',
        'GAA': 'E', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'UGU': 'C', 'CGU': 'R',
        'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'UGG': 'W', 'CGG': 'R', 'AGG': 'R',
        'GGG': 'G', 
    }
    
    protein = ""
    for n in range(0, len(rna), 3):
        codon = rna[n:n+3]
        if codon in ['UAA', 'UAG', 'UGA']:
            return protein
        else:
            protein += codon_dict[codon]

if __name__ == "__main__":
    assert(prot("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA") == "MAMAPRTEINSTRING")

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data_file:
            print prot(data_file.read())