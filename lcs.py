def lcs(strings):
    shortest = min(strings, key=len)
    L = len(shortest)

    for length in range(L, 1, -1):
        for offset in range(L - length + 1):
            target = shortest[offset:offset + length]
            try:
                map(lambda s: s.index(target), strings)
                return target
            except ValueError:
                continue

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            print lcs(f.readlines())