def grph(fasta):
    r"""
    Given: A collection of DNA strings in FASTA format having total length
    at most 10 kbp.

    Return: The adjacency list corresponding to O3.
    """
    from itertools import product
    overlap = lambda ((n1, s1),(n2, s2)): n1 != n2 and s1[-3:] == s2[0:3]
    stringify = lambda ((n1, s1),(n2, s2)): " ".join([n1, n2])
    return "\n".join(\
        map(stringify, \
            filter(overlap, \
                product(fasta.iteritems(), repeat=2))))

def parse_fasta(text):
    from StringIO import StringIO
    data = StringIO(text)
    strings = dict()
    for line in data:
        line = line.rstrip()
        if line[0] == ">":
            key = line[1:]
            strings[key] = ""
        else:
            strings[key] += line
    return strings

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data_file:
            print grph(parse_fasta(data_file.read()))