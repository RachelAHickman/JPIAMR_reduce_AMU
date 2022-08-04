# JPIAMR_reduce_AMU 
This repository to complimemt the publication "Exploring the Antibiotic Resistance Burden in Livestock, Livestock Handlers and Their Non-Livestock Handling Contacts: A One Health Perspective" by Hickman et. 2021
(https://www.frontiersin.org/articles/10.3389/fmicb.2021.651461/full)

All Genomic data processing was performed on the high computing capacity provided by SNIC through Uppsala Multidisciplinary Centre for Advance Computational Science (UPPMAX). Under the computational project SNIC2019-8-275 and small storage - Uppstore2019121

All processing of the whole genome sequences was done with open software with an in-house bioinformatics pipeline. 
Our pipeline consists of four main modules: 
Dependencies listed below.
1) For quality control (QC) assessment of the raw sequence files and trimming the sequence reads 
- FastQC (Wingett and Andrews, 2018)
- MultiQC (Ewels et al., 2016)
- Trim Galore (Babraham Bioinformatics, 2020)

2) De novo assembly with assembly QC
- Unicycler (Wick et al., 2017)
- QUAST (Gurevich et al., 2013)
- MultiQC (Ewels et al., 2016)

3) Molecular output excel report of genomic data 
- KmerFinder (Larsen et al., 2014)
- ARIBA (Hunt et al., 2017)
- ResFinder (Zankari et al., 2012)
- PointFinder (Zankari et al., 2017)

4) A core genome maximum likelihood phylogenetic 
- Prokka (Seemann, 2014)
- Roary (Page et al., 2015)
- IQ-Tree2 (Quang et al., 2020)

Downstream figure production and visualization was done locally via python scripts.




