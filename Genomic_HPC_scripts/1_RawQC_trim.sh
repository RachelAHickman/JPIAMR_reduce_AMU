#!/bin/bash
#SBATCH -A snicX-X-X
#SBATCH -t 10:00:00
#SBATCH -J RawREADSQC_TrimRawReads
module load bioinfo-tools FastQC/0.11.8 MultiQC/1.2
cd ./X/Raw_files
FILES=*.fq.gz
for file in $FILES
do
    mkdir fastqc
    fastqc -o fastqc/ $(basename $file)
done
cd fastqc 
multiqc .
cd ./Raw_files
for f1 in *_1.fq.gz
do
        f2=${f1%%_1.fq.gz}"_2.fq.gz"
        trim_galore --paired --phred33 --fastqc --clip_R1 5 --clip_R2 5 --three_prime_clip_R1 5 --three_prime_clip_R2 5 -o trim_galore $f1 $f2 
done
cd ./Raw_files/trim_galore
multiqc .