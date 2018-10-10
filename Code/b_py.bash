#!/bin/bash
for timefa in `seq 0 1 100`
do 
    for alpha in  "0.0001" "0.0005" "0.001" "0.005" "0.01" "0.05" "0.1" "0.5" "1.0" "5.0" "10.0" "50" "100" 
    do
        for fold in "1" "2" "3" "4"
        do
            work=/scratch/guo.yu/Active/Netflix/
            cd $work
            sbatch executem.bash $timefa $alpha $fold
        done
    done
done 
