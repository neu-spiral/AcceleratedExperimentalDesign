Experimental Design Acceleration
==============================
This code improves the time performance of the greedy algorithm for maximizing D-optimal design for comparisons. We also provide three algorithms Mutual Information (Mut), Fisher Information (Fisher), Entropy (Ent). When using this code, cite the paper 
>["Experimental Design Under the Bradley-Terry Model"](https://arxiv.org/abs/1901.06080).
>Yuan Guo, Jennifer Dy, Deniz Erdogmus, Jayashree Kalpathy-Cramer, Susan Ostmo, 
J. Peter Campbell, Michael F. Chiang, Stratis Ioannidis.
>(SDM 2019)

Usage
======================

An example execution is as follows:

	python Main.py outputfile --timefa 10 --alpha 0.2 --fold 3 --Size 100 

The 'timefa' is the dataset sequence, the alpha determines which cross_validation fold is used, the 'alpha' is the hyperparameter, the 'Size' is the batch size for different algorithm. 

Simulator Overview
======================

There are four experimental design algorithms can be used to acquire the optimal samples. They are all submodular functions. Especially, the D optimal design can be further accelerated by fundamental greedy algorithms or lazy greedy algorithms. In the code, we can change between these algorithms by selecting the following classes. The full list of the classes is listed below: 

Acceleration Class List
----------------------------------
* NaiveGreedy(Naive Greedy algorithm):
The first “naive” implementation slightly improves upon the abstract greedy algorithm (Alg. 1), which operates on the value oracle model, by computing a simpler version of gains.
* FactorizationGreedy(Factorization Naive Greedy algorithm): We exploit the pairwise comparison structure, the greedy algorithm can indeed be accelerated by Cholesky factorization and the Sherman Morisson formula. 
* ScalarGreedy(Memoization Naive Greedy algorithm): This algorithm takes advantage of the previous iteration’s computation. 
* NaiveLazy(Naive Lazy Greedy): The lazy greedy algorithm is a well-known variant of the standard greedy algorithm; it reduces execution time by avoiding the computation of all |Ω \ S | marginal gains ∆(e|S ) at each iteration. This is accomplished via a “lazy” evaluation of each inner loop in FindMax in Alg. 1.
* FactorizationLazy: Precalculation Factorization Lazy Greedy
* FactorizationLazyMemo: Factorization Lazy Greedy
* ScalarLazy: Precalculation Scalar Lazy Greedy
* ScalarLazyMemo: Scalar Lazy Greedy


## Acknowledgement

Our work is supported by NIH (R01EY019474, P30EY10572), NSF (SCH-1622542 at MGH; SCH-1622536 at Northeastern; SCH-1622679 at OHSU), and by unrestricted departmental funding from Research to Prevent Blindness (OHSU).





