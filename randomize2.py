from sipmap.io import safio
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path='pgs.00.pgsimp_squash-1004080151-1.saf'
saf_file = safio.openSafFile(file_path)
contents = saf_file.getRecords()
hh = saf_file.getHistoryHeader()
attrib = saf_file.getAttributes()
attrib_names = saf_file.getAttributeNames()
#fold = contents[contents['BINMUL']== 80]
rand = contents.sample(n=10000)
#plt.scatter(contents['IBLSEQ'],contents['IBPSEQ'],c=contents['BINMUL'])
#plt.scatter(rand['IBLSEQ'],rand['IBPSEQ'],c=rand['BINMUL'],s=1)
#plt.show()
f = open("pgs_include.txt", 'w')
f.write("TRARAN\n")
f.write("THDIRAACCEPTIBLSEQIBPSEQ\n")
for i in rand.itertuples(index=False, name='Pandas'):
	il = int(getattr(i,"IBLSEQ"))
	xln = int(getattr(i,"IBPSEQ"))
	f.write("THOR12%12d%12d%12d%12d%12d%12d\n"%(il,1,il,xln,1,xln))
f.close()
print("finished")

