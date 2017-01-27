def prob(prob_string):
    r"""
    Given: An array A containing at most 20 real numbers between 0 and 1,
    inclusively.

    Return: An array B in which B[i] represents the probability (to an
    accuracy of three decimal places) that for the GC-content in A[i], two
    randomly chosen symbols will be the same.
    """
    return " ".join("{0:.6f}".format(float(x)*(float(x)-1) + 0.5) \
        for x in prob_string.split())

if __name__ == "__main__":
    assert(prob("0.23 0.31 0.75") == "0.322900 0.286100 0.312500")

    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as prob_file:
            print prob(prob_file.read())