def kmp(dna):
    r"""
    Given: A DNA string s (of length at most 100 kbp).

    Return: The failure array of s.
    """
    pi = [0] * len(dna)
    k = 0
    for q in range(1, len(dna)):
        while k > 0 and dna[k] != dna[q]:
            k = pi[k - 1]
        if dna[k] == dna[q]:
            k += 1
        pi[q] = k

    return " ".join(map(str, pi))


if __name__ == "__main__":
    assert(kmp("CAGTAAGCAGGGACTG") == "0 0 0 0 0 0 0 1 2 3 0 0 0 1 0 0")
    assert(kmp("ABAABA") == "0 0 1 1 2 3")
    assert(kmp("AAACAAAAAAGCTGATAAAAGATTGCC") == "0 1 2 0 1 2 3 3 3 3 0 0 0 0 1 0 1 2 3 3 0 1 0 0 0 0 0")
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            print kmp(f.read().strip())