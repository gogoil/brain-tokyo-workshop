#!/bin/bash

#Write output to helloWorld-JOB_ID.out
#SBATCH -o helloWorl-%j.out
#Write error output to helloWorl-JOB_ID.err
#SBATCH -o helloWorl-%j.err
#submit to elsc.q partition
#SBATCH --partition=elsc.q
#ask for 2g for the job
#SBATCH --mem=2g
#SBATCH --mail-user=ido.goldb@gmail.com
source /ems/elsc-labs/loewenstein-y/ido.goldberg/WANN/brain-tokyo-workshop/venv/bin/activate
python /ems/elsc-labs/loewenstein-y/ido.goldberg/WANN/brain-tokyo-workshop/WANNRRelease/WANN/wann_train.py -p /ems/elsc-labs/loewenstein-y/ido.goldberg/WANN/brain-tokyo-workshop/WANNRRelease/WAN/p/improved_wan.json