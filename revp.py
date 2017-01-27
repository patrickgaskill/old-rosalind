from revc import revc

def revp(dna):
    rc = revc(dna)
    L = len(dna)

    for i in range(L-3):
        stack = []
        for offset in range(5):
            if dna[i-offset:i+4+offset] == rc[L-i-4-offset:L-i+offset]:
                stack.append("{0} {1}".format(i+1-offset, 4+2*offset))
            else:
                while stack:
                    print stack.pop()
                break

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            revp(f.read().strip())