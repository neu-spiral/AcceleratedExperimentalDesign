Experimental Design Acceleration
==============================
This project will improve the time performance for D-optimal design algorithm. Besides, we also provide three algorithms Mutual Information (Mut), Fisher Information (Fisher), Entropy (Ent). Simulator of experiments presented in ["Accelerated Experimental Designfor Pairwise Comparisons"].

Usage
======================


In the main.py file, we import the 'timefa', 'alpha' and 'fold': the 'timefa' is the dataset sequence, the alpha determines which cross_validation fold is used, the 'alpha' is the hyperparameter.   

Main.py
------------------

* Size1: the batch size for Random, D-optimal Design and Entropy method
* Size2: the batch size for Fisher Information method
* Size3: the batch size for Mutual Information method

* Xab: absolute feature in set $\mathcal{A}$.
* Yab: absolute label in set $\mathcal{A}$
* Xarray: all the absolute feature
* Omega: all the comparison pairs

* Naive Greedy:  Naive Greedy algorithm
* DecompositionGreedy: Factorization Naive Greedy algorithm
* MemoizationGreedy: Memoization Naive Greedy algorithm
* NaiveLazy: Naive Lazy Greedy 
* DecompositionLazy: Precalculation Factorization Lazy Greedy
* DecomLazyMemo: Factorization Factorization Lazy Greedy
* ScalarLazy: Precalculation Scalar Lazy Greedy
* ScalarLazyMemo: Scalar Lazy Greedy


