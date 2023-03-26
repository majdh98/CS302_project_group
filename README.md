# MST: Kruskal VS Prim

> Authors: Majd Hamdan, Danzan Achit-Erdene
> 
...CS 302 - Algorithms and Complexity-Fall 2021-Final Project
...December 15, 2021

In these files, we have implemented two algorithms to find the the minimum spanning tree (MST) of a weighted undirected graph. 
The first algorithm is kruskal's algorithm. It is implemented with a union-find data structure and has a time complexity 
of O(mlog(m) + mlog(n)). The second algorithm is Prim's. It is implemented with an array and has a time complexity of 
O(n^2). Given these two algorithm we have implemented a detailed analysis on the two algorithms where we compared their run
time for dense and sparse graphs with integers or real valued edges (please see 2). We also provided a visualization using 
Netlogo that shows how the two algorithms works step by step (please see 3).

## [Graph_MST_library.py](https://github.com/majdh98/Kruskal-Prim-MST-Alg-Benchmark/blob/main/Graph_MST_library.py) 
Graph_MST_library.py is a python library that contains the code for both algorithms. Graph_MST_library.py has two classes, Graph_kruskal and Graph_prim, that encapsulate the creation of graphs suitable for each method along with their logic.

## [MST-Test-Files](https://github.com/majdh98/Kruskal-Prim-MST-Alg-Benchmark/tree/main/MST-Test-Files)
MST-Test-Files contains test files provided by Professor Matthew Dickerson. 

Each file has a name beginning with the word “Real-“ or “Int-“. 
The files beginning with “Real-“ having floating point edge weights in the range from 1.0 to 100.0.  
The files beginning with “Int-“ have integer edge weights from 1..99.  (Consider that a bucket sort could be used to sort these edges in linear time by weight!)
Following “Real-“ or “Int-“ is the number of vertices.
Last comes either the number of edges or the word “dense”.  Dense graphs are complete, with n choose 2 edges.
Each files between with one line containing n and m where n=|V| and m=|V|. This is followed by m lines each of which contains three numbers. The first two numbers are a pair of vertices each indicated by an index in the range 0..(n-1). The final number is the edge weight.

The last line of the file contains the total weight of the MST computed by Professor Matthew Dickerson's solutions. We use these values in Driver.py to confirm out algorithms are generating the correct results.

## [Driver.py](https://github.com/majdh98/Kruskal-Prim-MST-Alg-Benchmark/blob/main/Driver.py)
Driver.py runs both algorithms on the testing files provided by Professor Matthew Dickerson and present their results next to the expected results to confirm the functionality of both algorithms.

## [Time_Complexity.ipynb](https://github.com/majdh98/Kruskal-Prim-MST-Alg-Benchmark/blob/main/Time_Complexity.ipynb)
Time_Complexity.ipynb is a Jupyter notebook that performs detailed comparison of run times between Kruskal's algorithm and Prim's algorithm for computing the minimum spanning tree (MST) of a weighted undirected graph using the test files in [MST-Test-Files](https://github.com/majdh98/Kruskal-Prim-MST-Alg-Benchmark/tree/main/MST-Test-Files). Both dense and sparse graphs are considered. The notebook is divided into four sections: 
Two sections to confirm the time complexity analysis:
...1.Prim's run time check
...2.Kruskal run time check
and two sections to compare the algorithms performance on dense and sparse graphs:
...3.Dense Graph Comparison
...4.Sparse Graph Comparison
A pdf version of this file is provided as [Time_Complexity.pdf](https://github.com/majdh98/Kruskal-Prim-MST-Alg-Benchmark/blob/main/Time_Complexity.pdf)

## [Time_Complexity.py](https://github.com/majdh98/Kruskal-Prim-MST-Alg-Benchmark/blob/main/Time_Complexity.py)
Time_Complexity.py implements the analysis in [Time_Complexity.ipynb](https://github.com/majdh98/Kruskal-Prim-MST-Alg-Benchmark/blob/main/Time_Complexity.ipynb) as a python script.

## Notes & Summery

1. Please change the path in Driver.py and Time_Complexity.py to where the test files are stored in your computer. As an 
example, the path is assigned to a valid string path.

2. We used the python library matplotlib for plotting time complexity comparison in Time_Complexity.py. To install, please 
type the following command in the terminal: pip install matplotlib. You must exit each figure for the next figure 
to be displayed. To avoid having to exit every figure, we ran the program in a Jupiter notebook (Time_Complexity.ipynb)
which allowed us to display graphs and make annotations in a visual friendly way. To avoid having to install the Jupiter
notebook framework, we saved Time_Complexity.ipynb into a pdf (Time_Complexity.pdf).
Having said all of this, Time_Complexity.py contains all the code necessary to generate all the graphs in Time_Complexity.ipynb. 

It is important to note that the analysis works on the testing files provided by Professor Matthew Dickerson. The programs work on any testing files in the same format. The quality of the analysis increases with more testing files. 

To summarize the results of the analysis: We confirmed that prim's run in O(n^2) and that kruskal runs in O(mlog(m) +mlog(n)). For sparse graphs, so we found that our version of Kruskal's run faster than our version of Prim's.
For a dense graph, we found that our version of Prim's runs faster than our version Kruskal's. 

3. To run the visualization, you must install netlogo. You can find the visualization in Visualization.nlogo. 
Once you open Visualization.nlogo, you will find instructions on how to use the visualization in the info section. The visualization runs on the test files stored in MST-Test-Files. You must change the path to this file in the file-path variable in the netlogo app. Instructions on how to do so are in the info section of the app.
