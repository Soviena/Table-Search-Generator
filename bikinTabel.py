import random
import pandas as Panda
import numpy as numberPy
import os

def buatTabelRelasi(N):
    x = N*5
    y = N*5
    table = set()
    # Buat Relasi
    for i in range(0,y,5):
        iterasi = 0
        while iterasi < random.randint(3, 5):
            randInteger = random.randint(0, N-1)*5
            if (i,randInteger) not in table:
                table.add((i,randInteger))
                iterasi+=1
    return table

def exportTabel(N):
    listOfTable = []
    listOfTable.append(["No.","Nama Tabel"])
    for i in range(0,N):
        listOfTable.append([i+1,"Tabel_"+str(i)])
        # print("Tabel_"+str(i))
    numberPy.savetxt("Tabel.csv", 
            listOfTable,
            delimiter =", ", 
            fmt ='% s')
    Table = Panda.read_csv (r'Tabel.csv')
    Table.to_excel(r"Tabel.xlsx",index = None, header=True)
    os.remove("Tabel.csv")

def lihatRelasi(listOfTable):
    x = N*5
    y = N*5
    for i in range(0,x,5):
        for j in range(0,y,5):
            relasi = False
            for tabel in listOfTable:
                if tabel[0] == i and tabel[1] == j:
                    relasi = True
                    break
            if relasi:
                print(" x ", end="")
            else:
                print(" . ", end="")
        print()

def exportTabelRelasi(TabelRelasi):
    temp = []
    temp.append(["No.","Nama Label","Tabel 1","Tabel 2"])
    index = 1
    for i in TabelRelasi:
        temp.append([index,"Atribut_"+str(i[0]//5)+"_"+str(i[1]//5),"Tabel_"+str(i[0]//5),"Tabel_"+str(i[1]//5)])
        index+=1
    numberPy.savetxt("Relasi.csv", 
            temp,
            delimiter =", ", 
            fmt ='% s')
    excel = Panda.read_csv (r'Relasi.csv')
    excel.to_excel(r"Relasi.xlsx",index = None, header=True)
    os.remove("Relasi.csv")

N = int(input("Jumlah Tabel : "))
exportTabel(N)
table = buatTabelRelasi(N)
# lihatRelasi(table)
exportTabelRelasi(table)
