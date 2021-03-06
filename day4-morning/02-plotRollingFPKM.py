#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table(sys.argv[1])

df_roi = df["chr"] == "3L"
df_chrom = df[df_roi]
smoothed = df_chrom["FPKM"].rolling(200).mean()
# print smoothed

plt.figure()
plt.plot(smoothed)
plt.title("Chromosome 3L, FPKM rolling mean (size=200)")
plt.savefig("smooth.png")
plt.close()