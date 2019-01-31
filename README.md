Experimental Design Acceleration
==============================
This code improves the time performance of the greedy algorithm for maximizing D-optimal design for comparisons. We also provide three algorithms Mutual Information (Mut), Fisher Information (Fisher), Entropy (Ent). When using this code, cite the paper  ["Accelerated Experimental Design for Pairwise Comparisons"](https://arxiv.org/abs/1901.06080) Yuan Guo, Jennifer Dy, Deniz Erdogmus, Jayashree Kalpathy-Cramer, Susan Ostmo, J. Peter Campbell, Michael F. Chiang, Stratis Ioannidis. SDM 2019.

Usage
======================

An example execution is as follows:

	python Main.py outputfile --timefa 10 --alpha 0.2 --fold 3 --Size 100 

The 'timefa' is the dataset sequence, the alpha determines which cross_validation fold is used, the 'alpha' is the hyperparameter, the 'Size' is the batch size for different algorithm. 

Simulator Overview
======================

There are four experimental design algorithms can be used to acquire the optimal samples. They are all submodular functions. Especially, the D optimal design can be further accelerated by fundamental greedy algorithms or lazy greedy algorithms. In the code, we can change between these algorithms by selecting the following classes. The full list for acceleration algorithms are listed below: 

Acceleration Algorithms Class List
----------------------------------
* NaiveGreedy:  Naive Greedy algorithm
* DecompositionGreedy: Factorization Naive Greedy algorithm
* MemoizationGreedy: Memoization Naive Greedy algorithm
* NaiveLazy: Naive Lazy Greedy 
* DecompositionLazy: Precalculation Factorization Lazy Greedy
* DecomLazyMemo: Factorization Factorization Lazy Greedy
* ScalarLazy: Precalculation Scalar Lazy Greedy
* ScalarLazyMemo: Scalar Lazy Greedy


* Xab: absolute feature in set $\mathcal{A}$.
* Yab: absolute label in set $\mathcal{A}$
* Xarray: all the absolute feature
* Omega: all the comparison pairs




