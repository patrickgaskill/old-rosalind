def iprb(k, m, n):
    return round(float(4*k*(k-1) + 8*k*m + 8*k*n + 3*m*(m-1) + 4*m*n)/(4*(k+m+n)*(k+m+n-1)), 5)

if __name__ == '__main__':
    assert iprb(2, 2, 2) == 0.78333

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data:
            k, m, n = [int(x) for x in data.readline().rstrip().split()]
            print iprb(k, m, n)