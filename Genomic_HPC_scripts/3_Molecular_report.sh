#!/bin/bash
#SBATCH -A snicX-X-X
#SBATCH -t 10:00:00
#SBATCH -J MoleRep
module load python3/3.7.2
module load bioinfo-tools biopython/1.73-py3
module load bioinfo-tools blast/2.9.0+
cd ./assembled_files
file=*fasta 
for f1 in $file; do     mkdir cge_results_${f1%%.fasta}"";     cp  $f1 cge_results_${f1%%.fasta}"";    mkdir small_farm_EC_cge_results;    mv cge_results_${f1%%.fasta}"" EC_cge_results;     wait; done
cd EC_cge_results
DIR=cge_results_D*
for dir in $DIR; do     cd $dir;    mkdir kmerfinder mlst_ec mlst_ec2 resfinder pointfinder plasmidfinder virulencefinder;     cd ..;    wait; done

#KMERFINDER
for dir in $DIR; do     cd $dir;     python3 ./pipeline_programmes/kmerfinder/kmerfinder.py -i *.fasta  -o kmerfinder -db ./pipeline_programmes/kmerfinder_db/bacteria.ATG -tax ./pipeline_programmes/kmerfinder_db/bacteria.name -kp ~/bin/ -x;    cd ..;   wait;done
for dir in $DIR; do     cd $dir;    cd kmerfinder;      mv results.txt results_${dir#cge_results_}.txt;     mv results.spa results_${dir#cge_results_}.spa;     cd ../../;    wait;done

#RESFINDER 
for dir in $DIR; do     cd $dir;     python3 ./pipeline_programmes/resfinder/resfinder.py -i D* -o resfinder -p ./pipeline_programmes/resfinder_db -mp blastn  -t 0.90 -l 0.60 -x;        cd resfinder;     mv results_tab.tsv results_tab_${dir#cge_results_}.tsv;     mv results.txt results_${dir#cge_results_}.txt;    cd ../..;    wait; done

#MLST
for dir in $DIR; do     cd $dir;     python3 ./pipeline_programmes/mlst/mlst.py -i *.fasta  -o mlst_ec -s ecoli -p ./pipeline_programmes/mlst_db/ -mp blastn -x;    cd mlst_ec;     mv results_tab.tsv results_tab_${dir#cge_results_}.tsv;     mv results.txt results_${dir#cge_results_}.txt;    cd ../..;     wait;done
for dir in $DIR; do     cd $dir;     python3 ./pipeline_programmes/mlst/mlst.py -i *.fasta  -o mlst_ec2 -s ecoli_3 -p ./pipeline_programmes/mlst_db/ -mp blastn -x;    cd mlst_ec2;     mv results_tab.tsv results_tab_${dir#cge_results_}.tsv;     mv results.txt results_${dir#cge_results_}.txt;    cd ../..;     wait;done

#POINTFINDER
for dir in $DIR; do     cd $dir;     python3 ./pipeline_programmes/pointfinder/PointFinder.py -i D*.fasta -o pointfinder -s escherichia_coli -p ./pipeline_programmes/pointfinder_db -m blastn -m_p /sw/bioinfo/blast/2.9.0+/rackham/bin/blastn --unknown_mut --stop_codons all;    cd pointfinder;     mv results_tab.tsv results_tab_${dir#cge_results_}.tsv;     mv results.txt results_${dir#cge_results_}.txt;    cd ../..;     wait;done

#PLASMIDFINDER
for dir in $DIR; do     cd $dir;     python3 ./pipeline_programmes/plasmidfinder/plasmidfinder.py -i *.fasta -o plasmidfinder -mp blastn -p ./pipeline_programmes/plasmidfinder_db/ -l 400  -t 0.9 -x;    cd plasmidfinder;     mv results_tab.tsv results_tab_${dir#cge_results_}.tsv;     mv results.txt results_${dir#cge_results_}.txt;    cd ../..;   wait;done

#VIRULENCEFINDER
for dir in $DIR; do     cd $dir;     python3 ./pipeline_programmes/virulencefinder/virulencefinder.py -i *.fasta -o virulencefinder -mp blastn -p ./pipeline_programmes/virulencefinder_db/   -t 0.9 -x;    cd virulencefinder;     mv results_tab.tsv results_tab_${dir#cge_results_}.tsv;     mv results.txt results_${dir#cge_results_}.txt;    cd ../..;    wait; done
