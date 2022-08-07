#!/bin/bash
#SBATCH -A snicX-X-X
#SBATCH -t X:00:00
#SBATCH -J phylo_tree
module load bioinfo-tools blast/2.9.0+ prokka/1.12-12547ca Roary/3.12.0
module load gcc/8.4.0 openmpi/4.0.2
module load bioinfo-tools iqtree/2.0-rc2-omp-mpi
cd ./Raw_files/assembly_files
FILE=*.fasta
for file in $FILE
do
      file2=${file%.fasta}""
      prokka  "$file" --outdir Prokka_$file2 --prefix $file2 --genus Escherichia --species coli --kingdom Bacteria --gcode 11 --usegenus --locustag JPIA_EC
done
mkdir Prokka
mv Prokka_* Prokka
cd Prokka
mv Prokka_*/*.gff .
roary –f roary_output -e -g 60000 -p 8 *.gff
cd roary_output
iqtree -s core_gene_alignment.aln -B 1000 -alrt 1000 -T AUTO -nt AUTO


