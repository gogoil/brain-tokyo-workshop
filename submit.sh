#!/bin/bash

#Write output to biped_STDOUT_JOB_ID.out
#SBATCH -J WANN
#SBATCH -o swing_RNN_V2_T_5_STDOUT_%j.out
#Write error output to swing_RNN_STDERR_JOB_ID.err
#SBATCH -e swing_RNN_V2_T_5_STDERR_%j.err
#submit to elsc.q partition
#SBATCH --partition=elsc.q
#SBATCH --mail-user=ido.goldb@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --cpus-per-task=1
#SBATCH --ntasks=33

source /ems/elsc-labs/loewenstein-y/ido.goldberg/WANN/brain-tokyo-workshop/venv/bin/activate
python WANNRelease/WANN/wann_train.py -p WANNRelease/WANN/p/laptop_swing.json -d WANNRelease/WANN/p/default_wan.json -n 32
