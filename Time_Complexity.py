import os
from Graph_MST_library import *
import time
import matplotlib.pyplot as plt

  
# PLEASE CHANGE THIS PATH TO WHERE THE TEST FIELS ARE STORED IN YOUR COMPUTER
path = r"C:\Users\Majd\Desktop\Middlebury\1- Midd Cources\4- Senior\1- Fall\CSCI 302\HWs\IPA-2\CS302_project_group\MST-Test-Files"

os.chdir(path)
  
files = []
for file in os.listdir():
#     print(str(file)[0])
#     print(str(file).split(".txt"))
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
        f = open(file_path, 'r')
        files.append([str(file), f.readlines()])
        f.close()



# Dense graph comparison
k_i_times = []
p_i_times = []
k_r_times = []
p_r_times = []
v_i = []
v_r = []

for file in files:
    name = file[0].split("-")
    file = file[1]
    if name[2] == "dense.txt":
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
            
        # starting time 
        start = time.time()
        cost, MST = g.kruskal()
        # end time
        end = time.time()
        if name[0] == "Int":
            k_i_times.append(end-start)
            v_i.append(int(name[1]))
        else:
            k_r_times.append(end-start)
            v_r.append(int(name[1]))
        
        # starting time 
        start = time.time()
        cost, MST = g_2.prim()
        # end time
        end = time.time()
        if name[0] == "Int":
            p_i_times.append(end-start)
        else:
            p_r_times.append(end-start)
plt.figure(1)
plt.scatter(v_i, p_i_times)
plt.scatter(v_i, k_i_times)
plt.scatter(v_r, p_r_times)
plt.scatter(v_r, k_r_times)
plt.title("Run Time comparison for dense graphs")
plt.xlabel("# of Vertices")
plt.ylabel("Run time (sec)")
plt.legend(["Prim-Int", "Kruskal-Int", "Prim-Real", "Kruskal-Real"])
plt.show()


# sparse graph comparison
k_i_times = []
p_i_times = []
k_r_times = []
p_r_times = []
v_i = []
v_r = []
for file in files:
    name = file[0].split("-")
    file = file[1]
    if name[2] != "dense.txt":
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
            
        # starting time 
        start = time.time()
        cost, MST = g.kruskal()
        # end time
        end = time.time()
        if name[0] == "Int":
            k_i_times.append(end-start)
            v_i.append(int(name[1]))
        else:
            k_r_times.append(end-start)
            v_r.append(int(name[1]))
        
        # starting time 
        start = time.time()
        cost, MST = g_2.prim()
        # end time
        end = time.time()
        if name[0] == "Int":
            p_i_times.append(end-start)
        else:
            p_r_times.append(end-start)
plt.figure(2)
plt.scatter(v_i, p_i_times)
plt.scatter(v_i, k_i_times)
plt.scatter(v_r, p_r_times)
plt.scatter(v_r, k_r_times)
plt.title("Run Time comparison for sparse graphs")
plt.xlabel("# of Vertices")
plt.ylabel("Run time (sec)")
plt.legend(["Prim-Int", "Kruskal-Int", "Prim-Real", "Kruskal-Real"])
plt.show()
    
    
