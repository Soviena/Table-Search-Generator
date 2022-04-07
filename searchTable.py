import pandas as pd

v = {}

tabel = pd.read_excel(r"Tabel.xlsx",header=0)
relasi = pd.read_excel(r"Relasi.xlsx",header=0)
rls = relasi.to_numpy()
tbl = tabel.to_numpy()
for i in tbl:
    key = int(i[1][7:])
    v[key] = []
for i in rls:
    key = int(i[2][7:])
    v[key].append(int(i[3][7:]))
print(v)