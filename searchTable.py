import pandas as pd
import re

v = {}

tabel = pd.read_excel(r"Tabel.xlsx",header=0)
relasi = pd.read_excel(r"Relasi.xlsx",header=0)
rls = relasi.to_numpy()
tbl = tabel.to_numpy()
for i in tbl:
    key = i[1].replace(" ","")
    v[key] = []
for i in rls:
    key = i[2].replace(" ","")
    v[key].append(i[3].replace(" ",""))

# print(v)
def bfs(graph, node,x):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)
    i = -1
    while queue:
        m = queue.pop(0) 
        if m == x:
            break
        else:
            i+=1
            print ("Atribut_"+m[6:]+"_", end = "") 
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
        print(queue[0][6:],end="-")
    print(" ("+str(i)+" Tabel antara)")


def dfs(graph, start, end):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        elif vertex == end:
            path.append(vertex)
            break
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
    i = -1
    while path:
        m = path.pop(0)
        if path:
            i+=1
            print("Atribut_"+m[6:]+"_"+path[0][6:], end = "-")
    print(" ("+str(i)+" Tabel antara)")
# for i in v:
#     print(i,v[i])

asal = input("Asal tabel (cth Tabel_0) : ")
akhir = input("Tujuan tabel (cth Tabel_9) : ")
metode = input("Metode pencarian (bfs/dfs) : ")

if metode == "bfs":
    bfs(v, "Tabel_3", "Tabel_0")
elif metode == "dfs":
    dfs(v, "Tabel_3", "Tabel_0")
else:
    print("Metode tidak ada !")