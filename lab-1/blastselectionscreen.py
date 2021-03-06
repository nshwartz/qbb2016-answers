#!/usr/bin/env python

from __future__ import division
import sys
import fasta
import itertools
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statsmodels.api as sm

query = fasta.FASTAReader(open(sys.argv[1]))

codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', '---':'*'
    }

reference = []
hits = []
dS = [0] * 3434
dN = [0] * 3434 

for identifier, sequence in query:
    aa_index = 0
    # search through 3 nt codon through query
    for codon in range(0,len(sequence),3):
        # test to verify codon is valid (in codontable dictionary)
        temp_codon = sequence[codon:codon+ 3]
        if temp_codon not in codontable:
            continue
        else:
            # new aa gets assigned appropriate codon
            aa = codontable[temp_codon]
            if identifier == "0_1":
                reference.append(aa)
            else:
                if aa == reference[aa_index]:
                    dS[aa_index] = dS[aa_index] + 1
                    aa_index += 1
                    # print aa_index
                else:
                    dN[aa_index] = dN[aa_index] + 1
                    aa_index += 1
                    # print aa_index

ds_dn_ratio = []

for i in range(0, len(dS)):
    if dS[i] == 0:
        dS[i] = 1
    else:
        pass
    dN[i]/dS[i]
    ratio.append(dN[i]/dS[i])
    

yvals = np.asarray(ratio)

positions =[]

xvals = np.asarray(positions)

for j in range(3434):
    positions.append(str(j))

sm.ztest(yvals, x2=None)

plt.figure()
plt.bar(positions,yvals, width = 0.35, bottom=None, hold=None)
plt.ylabel("dN/dS")
plt.xlabel("Codon Position")
plt.savefig("ratio.png")
plt.close()
