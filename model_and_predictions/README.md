# INF554-projet (Link prediction for the French Web)


## 1. Data
#### 1.1. Input
- node_information.zip: all node files where each file is a node (file name = node id) where we use node2vec convert it to *text_matrix.npy file*
- training.txt: $[id1,id2,(id1,id2)] \in training.txt$ where $(id1,id2) = \begin{cases} 1, &\text{if }  id1 \rightarrow id2\\ 0, &\text{otherwise} \end{cases}$
- testing.txt: $[id1,id2,(id1,id2)^*] \in testing.txt$ 

#### 1.2. Task
Predict $(id1,id2)^* \in testing.txt$ given the above information 


## 2. Feature engineering and Train/test 

For details please refer to */model_and_predictions/feature_engineering.ipynb* file

We split the training.txt into 70% for (X_train,y_train), 30% for( X_test,y_test) so that we can independently build graph which is a subgraph of the whole graph so as to avoid overfitting.


## 3. Models and parameter tuning 
All the models below including feature selection, parameter-tuning are stored in the */model_and_predictions/models_include_majorityVote.ipynb* file
All coresponding final predictions are stored in */model_and_predictions/predictions* folder
### 3.1. Single models
Random forest, XGBoost, HMM/GMMHMM, KNN, GradientBoosting

### 3.2 Improved models 
majority vote (Random forest, XGBoost,KNN)
majority vote1 (Random forest, XGBoost,KNN,XGBoost,GradientBoosting1)
majority vote best (majority vote, majority vote1, more approximation with XGboost)

