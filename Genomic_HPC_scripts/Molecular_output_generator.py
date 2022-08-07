#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"""
#Created on Mon Mar 23 12:19:41 2020

#@author: rachi870
#"""

import pandas as pd
import os
from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image
from openpyxl.utils.dataframe import dataframe_to_rows

# Create new workbook
cge_results = r"./cge_results.xlsx"
#kmerfinder
os.chdir('./cge_results/kmerfinder')
file_list_k = list()

for file in os.listdir():
    if file.endswith('.txt'):
        k = pd.read_csv(file,sep="\t")
        k['filename'] = file
        file_list_k.append(k)
kmerfinder= pd.concat(file_list_k, axis=0, ignore_index=True)
#mlst
os.chdir('cge_results/mlst_ec')
file_list_m1 = list()

for file in os.listdir():
    if file.endswith('grep.txt'):
        m1 = pd.read_csv(file,sep="\t",header=None)
        m1['filename'] = file
        file_list_m1.append(m1)
mlst_ec1= pd.concat(file_list_m1, axis=0, ignore_index=True)

#mlst2
os.chdir('./cge_results/mlst_ec2')
file_list_m2 = list()

for file in os.listdir():
    if file.endswith('grep.txt'):
        m2 = pd.read_csv(file,sep="\t",header=None)
        m2['filename'] = file
        file_list_m2.append(m1)
mlst_ec2= pd.concat(file_list_m1, axis=0, ignore_index=True)

#plasmidfinder
os.chdir('./cge_results/CGE_results/medium_farm_EC_cge_results/plasmidfinder')
file_list_p = list()

for file in os.listdir():
    if file.endswith('.tsv'):
        p = pd.read_csv(file,sep="\t")
        p['filename'] = file
        file_list_p.append(p)
plasmidfinder= pd.concat(file_list_p, axis=0, ignore_index=True)
plasmidfinder['Farm_size']= 'medium'
plasmidfinder['Species_MALDI_TOF']= 'E.coli'
#pointfinder
os.chdir('./cge_results/pointfinder')
file_list_po = list()

for file in os.listdir():
    if file.endswith('.tsv'):
        po = pd.read_csv(file,sep="\t")
        po['filename'] = file
        file_list_po.append(po)
pointfinder= pd.concat(file_list_po, axis=0, ignore_index=True)

#resfinder
os.chdir('./cge_results/resfinder')
file_list_r = list()

for file in os.listdir():
    if file.endswith('.tsv'):
        r = pd.read_csv(file,sep="\t",header=None)
        r['filename'] = file
        file_list_r.append(r)
resfinder= pd.concat(file_list_r, axis=0, ignore_index=True)

#virulencefinder
os.chdir('./cge_results/virulencefinder')
file_list_v = list()

for file in os.listdir():
    if file.endswith('.tsv'):
        v = pd.read_csv(file,sep="\t",header=None)
        v['filename'] = file
        file_list_v.append(v)
virulencefinder= pd.concat(file_list_v, axis=0, ignore_index=True)

writer = pd.ExcelWriter(medium_farm_EC_cge_results, engine = 'xlsxwriter')
kmerfinder.to_excel(writer, sheet_name = 'kmerfinder_results')
mlst_ec1.to_excel(writer, sheet_name = 'mlst_ec1_results')
mlst_ec2.to_excel(writer, sheet_name = 'mlst_ec2_results')
plasmidfinder.to_excel(writer, sheet_name = 'plasmidfinder_results')
pointfinder.to_excel(writer, sheet_name = 'pointfinder_results')
resfinder.to_excel(writer, sheet_name = 'resfinder_results')
virulencefinder.to_excel(writer, sheet_name = 'virulencefinder_results')
writer.save()
writer.close()
