def pdst(strings):
    N = len(strings)
    L = len(strings[0])
    matrix = [["0.00"] * N for i in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            matrix[i][j] = matrix[j][i] = \
                "{:.2f}".format(float(sum(a != b for a, b in zip(strings[i], strings[j]))) / L)

    return "\n".join(" ".join(row) for row in matrix)

def parse_fasta(text):
    from StringIO import StringIO
    data = StringIO(text)
    strings = []
    s = ""
    for line in data:
        line = line.rstrip()
        if line[0] == ">":
            if s != "":
                strings += [s]
            s = ""
        else:
            s += line
    strings += [s]
    return strings

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data_file:
            print pdst(parse_fasta(data_file.read()))