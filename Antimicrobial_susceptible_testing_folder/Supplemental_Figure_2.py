#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"""
#Created on Fri May 29 13:21:31 2020

#@author: rachi870
#"""
import pandas as pd
import seaborn as sns

#Import Data as a dataframe
JPIA_MIC_data = pd.read_excel (r './Antimicrobial_susceptible_testing_folder/antimicrobial_suceptible_raw_data.xlsx')
JPIA_MIC_data.head()
#Seperate dataframes for E. coli 
E_coli = JPIA_MIC_data.loc[JPIA_MIC_data['Iden.'] == 'E.coli']
#Making resistance catogories
E_coli_AMP = E_coli[['bact_code', 'farm_no','Sources','media', 'col_no', 'AMP']]
E_coli_CHL = E_coli[['bact_code', 'farm_no','Sources','media', 'col_no', 'CHL']]
E_coli_CIP = E_coli[['bact_code', 'farm_no','Sources','media', 'col_no','CIP']]
E_coli_COL= E_coli[['bact_code', 'farm_no','Sources','media', 'col_no', 'COL']]
E_coli_FOT = E_coli[['bact_code', 'farm_no','Sources','media', 'col_no','FOT']]
E_coli_GEN = E_coli[['bact_code', 'farm_no','Sources','media', 'col_no', 'GEN']]
E_coli_MERO = E_coli[['bact_code', 'farm_no','Sources','media', 'col_no', 'MERO']]
E_coli_NAL = E_coli[['bact_code', 'farm_no','Sources','media', 'col_no', 'NAL']]
E_coli_TAZ = E_coli[['bact_code', 'farm_no','Sources','media', 'col_no', 'TAZ']]
E_coli_TET = E_coli[['bact_code', 'farm_no','Sources','media', 'col_no', 'TET']]
E_coli_TGC = E_coli[['bact_code', 'farm_no','Sources','media', 'col_no', 'TGC']]
E_coli_TMP = E_coli[['bact_code', 'farm_no','Sources','media', 'col_no', 'TMP']]
#
E_coli_AMP['Antibiotic_Drug'] = 'AMP'
E_coli_CHL['Antibiotic_Drug'] = 'CHL'
E_coli_CIP['Antibiotic_Drug'] = 'CIP'
E_coli_COL['Antibiotic_Drug'] = 'COL'
E_coli_FOT['Antibiotic_Drug'] = 'FOT'
E_coli_GEN['Antibiotic_Drug'] = 'GEN'
E_coli_MERO['Antibiotic_Drug'] = 'MERO'
E_coli_NAL['Antibiotic_Drug'] = 'NAL'
E_coli_TAZ ['Antibiotic_Drug'] = 'TAZ'
E_coli_TET ['Antibiotic_Drug'] = 'TET'
E_coli_TGC ['Antibiotic_Drug'] = 'TGC'
E_coli_TMP ['Antibiotic_Drug'] = 'TMP'
#
E_coli_AMP.rename(columns={'AMP': 'MIC_Value(mg/L)'}, inplace=True)
E_coli_CHL.rename(columns={'CHL': 'MIC_Value(mg/L)'}, inplace=True)
E_coli_CIP.rename(columns={'CIP': 'MIC_Value(mg/L)'}, inplace=True)
E_coli_COL.rename(columns={'COL': 'MIC_Value(mg/L)'}, inplace=True)
E_coli_FOT.rename(columns={'FOT': 'MIC_Value(mg/L)'}, inplace=True)
E_coli_GEN.rename(columns={'GEN': 'MIC_Value(mg/L)'}, inplace=True)
E_coli_MERO.rename(columns={'MERO': 'MIC_Value(mg/L)'}, inplace=True)
E_coli_NAL.rename(columns={'NAL': 'MIC_Value(mg/L)'}, inplace=True)
E_coli_TAZ.rename(columns={'TAZ': 'MIC_Value(mg/L)'}, inplace=True)
E_coli_TET.rename(columns={'TET': 'MIC_Value(mg/L)'}, inplace=True)
E_coli_TGC.rename(columns={'TGC': 'MIC_Value(mg/L)'}, inplace=True)
E_coli_TMP.rename(columns={'TMP': 'MIC_Value(mg/L)'}, inplace=True)

#For clinical breakpoints
E_coli_AMP['Resistance_status'] = 	E_coli_AMP['MIC_Value(mg/L)'].apply(lambda x: 0 if x <= 8 else 1) 
E_coli_CHL['Resistance_status'] = 	E_coli_CHL['MIC_Value(mg/L)'].apply(lambda x: 0 if x <= 8 else 1) 

def parse_values(x):
    if x <= 0.25:
       return 0
    elif x <= 0.5:
       return 0.5
    else:
       return 1
E_coli_CIP['Resistance_status'] = E_coli_CIP['MIC_Value(mg/L)'].apply(parse_values)
E_coli_COL['Resistance_status'] = 	E_coli_COL['MIC_Value(mg/L)'].apply(lambda x: 0 if x <= 2 else 1) 
 
def parse_values(x):
    if x <= 1:
       return 0
    elif x <= 2:
       return 0.5
    else:
       return 1
E_coli_FOT['Resistance_status'] = E_coli_FOT['MIC_Value(mg/L)'].apply(parse_values)

def parse_values(x):
    if x <= 2:
       return 0
    elif x <= 4:
       return 0.5
    else:
       return 1
E_coli_GEN['Resistance_status'] = E_coli_GEN['MIC_Value(mg/L)'].apply(parse_values)

def parse_values(x):
    if x <= 2:
       return 0
    elif x <= 8:
       return 0.5
    else:
       return 1
E_coli_MERO['Resistance_status'] = E_coli_MERO['MIC_Value(mg/L)'].apply(parse_values)

def parse_values(x):
    if x <= 1:
       return 0
    elif x <= 4:
       return 0.5
    else:
       return 1
E_coli_TAZ['Resistance_status'] = E_coli_TAZ['MIC_Value(mg/L)'].apply(parse_values)

E_coli_TGC['Resistance_status'] = E_coli_TGC['MIC_Value(mg/L)'].apply(lambda x: 0 if x <= 0.5 else 1)

def parse_values(x):
    if x <= 2:
       return 0
    elif x <= 4:
       return 0.5
    else:
       return 1
E_coli_TMP['Resistance_status'] = E_coli_TMP['MIC_Value(mg/L)'].apply(parse_values)
#Remodel
E_coli_Remodelled_JPIA_MIC_data = pd.concat([E_coli_AMP, E_coli_CHL, E_coli_CIP, E_coli_COL, E_coli_FOT, E_coli_GEN, E_coli_MERO, E_coli_TAZ, E_coli_TGC, E_coli_TMP])
#Seperated by selection media
E_coli_CARBA_selected = E_coli_Remodelled_JPIA_MIC_data.loc[E_coli_Remodelled_JPIA_MIC_data['media'] == 'C']
#Pivot table
heatmap_E_coli_CARBA_selected =pd.pivot_table (E_coli_CARBA_selected, index=['farm_no','Sources', 'media', 'col_no'], columns=['Antibiotic_Drug'],
                                              values=['Resistance_status'])
#Suplemental figure 2 -Carbapenem selected isolates and their AST profile
cmap = sns.color_palette("coolwarm", 11)
supplemental_figure_2=sns.clustermap(heatmap_E_coli_CARBA_selected, cmap = cmap)
ax = supplemental_figure_2.ax_heatmap
ax.set_xticklabels(['COL', 'TGC', 'TMP', 'CIP', 'MERO', 'GEN', 'AMP', 'TAZ', 'CHL', 'FOT'], rotation=0)
ax.set_ylabel('Bacterial Isolate (labelled by Farm-Source-Isolation media-Colony)')
ax.set_xlabel('Antibiotic Drug')
supplemental_figure_2.savefig('./Antimicrobial_susceptible_testing_folder/supplemental_figure_2.png', dpi=300)
