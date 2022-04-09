import pandas as Panda

def DFSearch(graf, v, x):
    stk, route = [v], []

    while stk:
        vertices = stk.pop()
        if vertices in route:
            continue
        elif vertices == x:
            route.append(vertices)
            break
        route.append(vertices)
        for ttg in graf[vertices]:
            stk.append(ttg)
    i = -1
    while route:
        out = route.pop(0)
        if route:
            i+=1
            print("Atribut_"+out[6:]+"_"+route[0][6:], end = "-")
    print(" ("+str(i)+" Tabel antara)")

def BFSearch(graf, v,x):
    vis = []
    q = []
    vis.append(v)
    q.append(v)
    i = -1
    while q:
        m = q.pop(0) 
        if m == x:
            break
        else:
            i+=1
            print("Atribut_"+m[6:]+"_", end = "") 
        for ttg in graf[m]:
            if ttg not in vis:
                vis.append(ttg)
                q.append(ttg)
        if q:
            print(q[0][6:],end="-")
    print(" ("+str(i)+" Tabel antara)")

def bacaXLSX():
    vertex = {}
    daftarTabel = Panda.read_excel(r"Tabel.xlsx",header=0)
    daftarRelasi = Panda.read_excel(r"Relasi.xlsx",header=0)
    relasi = daftarRelasi.to_numpy()
    tabel = daftarTabel.to_numpy()
    for i in tabel:
        key = i[1].replace(" ","")
        vertex[key] = []
    for i in relasi:
        key = i[2].replace(" ","")
        vertex[key].append(i[3].replace(" ",""))
    return vertex

vertex = bacaXLSX()
v = input("Asal tabel (ex. Tabel_7) : ")
x = input("Tujuan tabel (ex. Tabel_4) : ")
m = input("Metode pencarian (DFS/BFS) : ")

if m in ("BFS","bfs"):
    BFSearch(vertex, v, x)
elif m in ("DFS","dfs"):
    DFSearch(vertex, v, x)
else:
    print("Metode tidak diimplementasikan !")