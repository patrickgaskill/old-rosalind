def prtm(protein):
    r"""
    Given: A protein string P of length at mos't': 1000,  aa.

    Return: The weight of P to an accuracy of two decimal places. Consult the
    monoisotopic mass table.
    """
    from operator import mul

    mass = {
        'A': 71.03711, 
        'C': 103.00919, 
        'D': 115.02694, 
        'E': 129.04259, 
        'F': 147.06841, 
        'G': 57.02146, 
        'H': 137.05891, 
        'I': 113.08406, 
        'K': 128.09496, 
        'L': 113.08406, 
        'M': 131.04049, 
        'N': 114.04293, 
        'P': 97.05276, 
        'Q': 128.05858, 
        'R': 156.10111, 
        'S': 87.03203, 
        'T': 101.04768, 
        'V': 99.06841, 
        'W': 186.07931, 
        'Y': 163.06333,  
    }

    return "{:.2f}".format(sum(map(mass.get, protein)))

if __name__ == "__main__":
    assert(prtm("SKADYEK") == "821.39")

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data:
            print prtm(data.read())