#!/bin/bash
#SBATCH -A snicX-X-X
#SBATCH -t X:00:00
#SBATCH -J assembly
module load python3/3.7.2 java/sun_jdk1.8.0_151 
module load bioinfo-tools blast/2.9.0+ Pilon/1.22 samtools/1.10  bowtie2/2.3.5.1 spades/3.13.1 quast/4.5.4  MultiQC/1.2
cd ./Raw_files/trim_galore
for f1 in  *_1_val_1.fq.gz
do
        f2=${f1%%_1_val_1.fq.gz}"_2_val_2.fq.gz"
        f3=${f1%%_1_val_1.fq.gz}""
        .local/bin/unicycler --min_fasta_length 400  -o unicycler_$f3 -1 $f1 -2 $f2 --pilon_path /sw/apps/bioinfo/Pilon/1.22/rackham/pilon.jar
done
cd ./Raw_files/
mkdir assembly_files
mv ./Raw_files/trim_galore/unicycler* ./Raw_files/assembly_files
cd ./Raw_files/assembly_files
assembled_dir=unicycler_*
for dir in $assembled_dir
do       
        cd $dir
        mv assembly.fasta ${dir#unicycler_}"".fasta
        cd ..
done  
cp unicycler_*/*.fasta .
file=*.fasta
for f1 in $file
do
     f3=${f1%%.fasta}""
     quast.py -o quast_$f3 $f1
done
mkdir quast
mv quast* quast
cd  quast
cp quast*/*.txt .
multiqc .

 
