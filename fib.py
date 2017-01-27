memo = {}
def fib(n, k):
    if n < 3: return 1
    if not n in memo:
        memo[n] = {k: fib(n-1, k) + k * fib(n-2, k)}
    elif k not in memo[n]:
        memo[n][k] = fib(n-1, k) + k * fib(n-2, k)
    return memo[n][k]

if __name__ == '__main__':
    assert fib(5, 3) == 19

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data:
            n, k = [int(x) for x in data.readline().rstrip().split()]
            print fib(n, k)