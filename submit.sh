#!/bin/bash

#Write output to WANN-STDOUT-JOB_ID.out
#SBATCH -J WANN
#SBATCH -o WANN-STDOUT-%j.out
#Write error output to WANN-STDERR-JOB_ID.err
#SBATCH -e WANN-STDERR-%j.err
#submit to elsc.q partition
#SBATCH --partition=elsc.q
#SBATCH --mail-user=ido.goldb@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --cpus-per-task=1
#SBATCH --ntasks=33

source /ems/elsc-labs/loewenstein-y/ido.goldberg/WANN/brain-tokyo-workshop/venv/bin/activate
python WANNRelease/WANN/wann_train.py -p WANNRelease/WANN/p/biped.json -d WANNRelease/WANN/p/default_wan.json -n 32
