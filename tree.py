def tree(n, edges):
    r"""
    Given: A positive integer n (n <= 1000) and an adjacency list corresponding
    to a graph on n nodes that contains no cycles.

    Return: The minimum number of edges that can be added to the graph to
    produce a tree.
    """
    return n - len(edges) - 1

if __name__ == "__main__":
    assert(tree(10, [[1, 2], [2, 8], [4, 10], [5, 9], [6, 10], [7, 9]]) == 3)

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as data:
            n = int(data.readline().rstrip())
            edges = map(lambda e: map(int, e.rstrip().split()), data.readlines())
            print tree(n, edges)