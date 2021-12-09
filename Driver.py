import os
from Graph_MST_library import *

# PLEASE CHANGE THIS PATH TO WHERE THE TEST FILES ARE STORED IN YOUR COMPUTER
#path = r"C:\Users\Majd\Desktop\Middlebury\1- Midd Cources\4- Senior\1- Fall\CSCI 302\HWs\IPA-2\CS302_project_group\MST-Test-Files"
path = "/Users/Danzan/workspace/CS-Middlebury/CS302_MST_/MST-Test-Files"


os.chdir(path)

files = []
for file in os.listdir():
#     print(str(file).split(".txt"))
    if file.endswith(".txt"):
        #file_path = f"{path}\{file}"
        file_path = f"{path}/{file}"
        f = open(file_path, 'r')
        files.append(f.readlines())
        f.close()


for file in files:
    num_lines = len(file)
    # get n and m from first line
    g = file[0].split()
    n = int(g[0])
    m = int(g[1])

    # create a graph
    g = Graph_kruskal(n, m)
    g_2 = Graph_prim(n, m)

    # fill graph
    for i in range(1, num_lines-1):
        line = file[i].split()
        u = int(line[0])
        v = int(line[1])
        w = float(line[2])
        g.add_edge([u, v, w])
        g_2.add_edge([u, v, w])

    # run kruskal
    cost, MST = g.kruskal()
    print("Kruskal's method MST cost = " + str(cost) + " known cost = " + str(file[num_lines-1]))
    cost, MST = g_2.prim()
    print("Prim's method MST cost = " + str(cost) + " known cost = " + str(file[num_lines-1]))
