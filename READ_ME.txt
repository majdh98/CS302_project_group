Names: Majd Hamdan, Danzan Achit-Erdene.

In this files, we have implemented two algorithms find the the minimum spanning tree (MST) of a weighted undirected graph. 
The first algorithm is kruskal's algorithm. It was implemented with a union-find data structure and has a time complexity 
of O(mlog(m) + mlog(n)). The second algorithm in Prim's. It was implemented with an array and has a time complexity of 
O(n^2). Given these two algorithm we have implemented a detailed analysis on the two algorithms where we compared their run
time for dense and sparse graphs with integers or real valued edges (please see 2). We also provided a visualization using 
Netlogo that shows how the two algorithms works step by step (please see 3).

Driver.py runs both algorithms on the testing files provided by professor Professor Matthew Dickerson and present their 
results next to the expected results to confirm the functionality of both algorithms.

1- Please change the path in Driver.py and Time_Complexity.py to where the test files are stored in your computer. As an 
example, the path is assigned to a valid string path.

2- We used the python library matplotlib for plotting time complexity comparison in Time_Complexity.py. To install, please 
type the following command in the terminal: pip install matplotlib. You must exit each figure for the next figure 
to be displayed. To avoid having to exit every figure, we ran the program in a Jupiter notebook (Time_Complexity.ipynb)
which allowed US to display graphs and make annotations in a visual friendly way. To avoid having to install the Jupiter
notebook framework, we saved Time_Complexity.ipynb into a pdf (Time_Complexity.pdf).
Having said all of this, Time_Complexity.py contains all the code necessary to generate all the graphs in 
Time_Complexity.ipynb. 

It is important to note that the analysis works on the testing files provided by Professor Matthew Dickerson. The programs 
works on any testing files in the same format. The analysis can identify the run time of both algorithms better with more
testing files. 

To summarize the results of the analysis: We confirmed that prim's run in O(n^2) and that kruskal runs in O(mlog(m) +
mlog(n)). For sparse graphs, so we found that our version of Kruskal's run faster than our version of Prim's.
For a dense graph, we found that our version of Prim's runs faster than our version Kruskal's. 

3- To run the visualization, you must install netlogo. You can find the visualization in Visualization.nlogo. 
Once you open Visualization.nlogo, you will find instructions on how to use the visualization in the info section. The 
visualization runs on the test files stored in MST-Test-Files. You must change the path to this file in the file-path 
variable in the netlogo app. Instructions on how to do so are in the info section of the app.
