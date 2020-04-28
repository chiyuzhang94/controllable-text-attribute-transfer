#!/bin/bash
#SBATCH --time=96:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --gres=gpu:4
#SBATCH --mem=64G
#SBATCH --job-name=amazon
#SBATCH --output=amazon.out
#SBATCH --account=rrg-mageed
#SBATCH --mail-user=zcy94@outlook.com
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
module load cuda cudnn
source ~/py3.6/bin/activate

python3 main2.py
