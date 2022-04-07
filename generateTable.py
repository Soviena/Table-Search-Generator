import random
import pandas as pd
import numpy as np
N = int(input("Jumlah Tabel : "))
x = N*5
y = N*5

tabel = set()
for i in range(0,y,5):
    itr = 0
    while itr < random.randint(3, 5):
        r = random.randint(0, N-1)*5
        if (i,r) not in tabel:
            tabel.add((i,r))
            itr+=1
tbl = []
tbl.append(["No.","Nama Tabel"])
for i in range(0,N):
    tbl.append([i+1,"Tabel_"+str(i)])
    # print("Tabel_"+str(i))
np.savetxt("Tabel.csv", 
           tbl,
           delimiter =", ", 
           fmt ='% s')
tblR = pd.read_csv (r'Tabel.csv')
tblR.to_excel(r"Tabel.xlsx",index = None, header=True)
# print(tabel)

# for i in range(0,x,5):
#     for j in range(0,y,5):
#         found = False
#         for t in tabel:
#             if t[0] == i and t[1] == j:
#                 found = True
#                 break
#         if found:
#             print(" x ", end="")
#         else:
#             print(" . ", end="")
#     print()

csv = []
csv.append(["No.","Nama Label","Tabel 1","Tabel 2"])
idx = 1
for i in tabel:
    csv.append([idx,"Atribut_"+str(i[0]//5)+"_"+str(i[1]//5),"Tabel_"+str(i[0]//5),"Tabel_"+str(i[1]//5)])
    idx+=1
    # print("Atribut_"+str(i[0]//5)+"_"+str(i[1]//5),"Tabel_"+str(i[0]//5),"Tabel_"+str(i[1]//5))
np.savetxt("Relasi.csv", 
           csv,
           delimiter =", ", 
           fmt ='% s')
csvE = pd.read_csv (r'Relasi.csv')
csvE.to_excel(r"Relasi.xlsx",index = None, header=True)