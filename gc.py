r"""
DNA strings must be labeled when they are consolidated into a database.
A commonly used method of string labeling is called FASTA format. In this
format, the string is introduced by a line that begins with ">", followed
by some information naming and characterizing the string. Subsequent lines
contain the string itself; the next line starting with ">" indicates the
label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by
the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between
0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp
each).

Return: The ID of the string having the highest GC-content, followed by
the GC-content of that string. The GC-content should have an accuracy of
4 decimal places (see the note below on decimal accuracy).
"""

import sys
from collections import Counter
from StringIO import StringIO
import operator

def gc_content(dna_string):
    c = Counter(dna_string)
    return float((c["G"] + c["C"])) / float(len(dna_string))

sample_dataset = """\
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""

if len(sys.argv) > 1:
    data = open(sys.argv[1], 'r')
else:
    data = StringIO(sample_dataset)

strings = dict()
key = ""
for line in data:
    line = line.rstrip()
    if line[0] == ">":
        if key:
            strings[key] = gc_content(dna_string)

        key = line[1:]
        dna_string = ""
    else:
        dna_string += line
strings[key] = gc_content(dna_string)

name, content = sorted(strings.iteritems(), key=operator.itemgetter(1), reverse=True)[0]

print "{0}\n{1:.6f}%".format(name, content * 100)
