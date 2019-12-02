# INF554-projet
Link prediction for the French Web

## Potential Methods

- [] lec slides 
	
	[Graph-Of-Words ](https://moodle.polytechnique.fr/pluginfile.php/171960/mod_resource/content/1/ML_DL_graphs.pdf)  p28/60
- [Grakel](https://ysig.github.io/GraKeL/dev/)



### 1. Data
#### 1.1. Input
- node_information.zip: all node files where each file is a node (file name = node id) 
- training.txt: $[id1,id2,(id1,id2)] \in training.txt$ where $(id1,id2) = \begin{cases} 1, &\text{if }  id1 \rightarrow id2\\ 0, &\text{otherwise} \end{cases}$
- testing.txt: $[id1,id2,(id1,id2)^*] \in testing.txt$ 

#### 1.2. Task
Predict $(id1,id2)^* \in testing.txt$ given the above information 

#### 1.3. Some ideas
- NLP task
	- txt representation: word embedding(word2vec), n-gram
	- construct features 
- Define a metric (e.g., node similarity) for the exsitance of a link between two nodes 
 