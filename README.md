Experimental Design Acceleration
==============================
This project will improve the time performance for D-optimal design algorithm. Besides, we also provide three algorithms Mutual Information (Mut), Fisher Information (Fisher), Entropy (Ent). Simulator of experiments presented in ["Accelerated Experimental Designfor Pairwise Comparisons"].

Usage
======================

We use the b_py.bash to run the experiment. The 'timefa', 'fold' can determine which pickle file is selected. 'alpha' can determine the hyperparameter.

Usage
-----
An example execution is as follows:

	./b_py.bash

in the 'b_py.bash', we connect it to the executem.bash file. 

executem.bash
------------------


In the file:

* SBATCH --time.  the run time 
* SBATCH --mem.  the memory
* SBATCH --partition which partition should be used
* SBATCH --constraint the hardware requirement for this experiment.

