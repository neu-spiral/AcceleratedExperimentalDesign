#!/bin/bash
#set a job name 
#SBATCH --job-name=netflix
#a file for job output, you can check job progress
#SBATCH --output=netflix.out
# a file for errors from the job
#SBATCH --error=netflix.err
#time you think you need: default is one day 
#in minutes in this case, hh:mm:ss
#SBATCH --time=48:00:00
#number of tasks you are requesting 
#SBATCH -n 1
#SBATCH --mem=4Gb
#partition to use 
#SBATCH --partition=ioannidis
#SBATCH --constraint="E5-2680v4@2.40GHz"
#number of nodes to distribute n tasks across

python Main.py $1 $2 $3
