#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 12:58:54 2020

@author: rachi870
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Import Data as a dataframe
JPIA_MIC_data = pd.read_excel (r'./Antimicrobial_susceptible_testing_folder/antimicrobial_suceptible_raw_data.xlsx')
JPIA_MIC_data.head()
###E.coli info first
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

#Add in farm size information
key1= pd.read_excel (r'/Users/rachi870/Desktop/JPIA_reduce_amu/key_farm_size_EC.xlsx')
key1.set_index(['Key'], inplace=True)
key1_dict=key1['Farm_size'].to_dict()
print(key1_dict)
E_coli_Remodelled_JPIA_MIC_data['Farm_size']= E_coli_Remodelled_JPIA_MIC_data['bact_code'].map(key1_dict)




##Use both farm size and  source to calulate average and standard deviation
#EC
EC_Contact_person = E_coli_Remodelled_JPIA_MIC_data.loc[E_coli_Remodelled_JPIA_MIC_data['Sources'] == 'C']
EC_Pig = E_coli_Remodelled_JPIA_MIC_data.loc[E_coli_Remodelled_JPIA_MIC_data['Sources'] == 'P']
EC_Non_contact_person = E_coli_Remodelled_JPIA_MIC_data.loc[E_coli_Remodelled_JPIA_MIC_data['Sources'] == 'U']

small_EC_Pig = EC_Pig.loc[EC_Pig['Farm_size'] == 'small']
small_EC_Pig['Group']='Small-scale Farm - Pig Isolates'
small_EC_Contact_person = EC_Contact_person.loc[EC_Contact_person['Farm_size'] == 'small']
small_EC_Contact_person['Group']='Small-scale Farm - Contact Human Isolates'
small_EC_Non_contact_person = EC_Non_contact_person.loc[EC_Non_contact_person['Farm_size'] == 'small']
small_EC_Non_contact_person['Group']='Small-scale Farm - Non-contact Human Isolates'
medium_EC_Pig = EC_Pig.loc[EC_Pig['Farm_size'] == 'medium']
medium_EC_Pig['Group']='Medium-scale Farm - Pig Isolates'
medium_EC_Contact_person = EC_Contact_person.loc[EC_Contact_person['Farm_size'] == 'medium']
medium_EC_Contact_person['Group']='Medium-scale Farm - Contact Human Isolates'
medium_EC_Non_contact_person = EC_Non_contact_person.loc[EC_Non_contact_person['Farm_size'] == 'medium']
medium_EC_Non_contact_person['Group']='Medium-scale Farm - Non-contact Human Isolates'
EC_new=pd.concat([small_EC_Pig, medium_EC_Pig, small_EC_Contact_person, medium_EC_Contact_person, small_EC_Non_contact_person, medium_EC_Non_contact_person])

#Antibiogram figure
fig = plt.figure(figsize = (50,20)) # width x height
ax1 = fig.add_subplot(2, 5, 1) # row, column, position
ax2 = fig.add_subplot(2, 5, 2)
ax3 = fig.add_subplot(2, 5, 3)
ax4 = fig.add_subplot(2, 5, 4)
ax5 = fig.add_subplot(2, 5, 5)
ax6 = fig.add_subplot(2, 5, 6)
ax7 = fig.add_subplot(2, 5, 7)
ax8 = fig.add_subplot(2, 5, 8)
ax9 = fig.add_subplot(2, 5, 9)
ax10 = fig.add_subplot(2, 5, 10)
AMP = EC_new.loc[EC_new['Antibiotic_Drug'] == 'AMP']
sns.pointplot(x="Antibiotic_Drug", y="MIC_Value(mg/L)", hue="Group", data=AMP, col="Antibiotic_Drug", ax=ax1, palette=["#fcc5c0", "#e7298a", "#c7e9c0", "#41ab5d", "#c6dbef", "#2171b5"], join=False, ci="sd", dodge=0.3)
ax1.set_xlabel("Antibiotic Drug", fontsize=12)
ax1.set_ylabel("MIC Value (mg/L)", fontsize=12)
ax1.axhline(8, ls=':')
ax1.get_legend().set_visible(False)
ax1.set_ylim(0,80)

CHL = EC_new.loc[EC_new['Antibiotic_Drug'] == 'CHL']
sns.pointplot(x="Antibiotic_Drug", y="MIC_Value(mg/L)", hue="Group", data=CHL, col="Antibiotic_Drug", ax=ax2, palette=["#fcc5c0", "#e7298a", "#c7e9c0", "#41ab5d", "#c6dbef", "#2171b5"], join=False,  ci="sd", dodge=0.3)
ax2.set_xlabel("Antibiotic Drug", fontsize=12)
ax2.set_ylabel("MIC Value (mg/L)", fontsize=12)
ax2.get_legend().set_visible(False)
ax2.axhline(8, ls=':')
ax2.set_ylim(0,120)

CIP = EC_new.loc[EC_new['Antibiotic_Drug'] == 'CIP']
sns.pointplot(x="Antibiotic_Drug", y="MIC_Value(mg/L)", hue="Group", data=CIP, col="Antibiotic_Drug", ax=ax3, palette=["#fcc5c0", "#e7298a", "#c7e9c0", "#41ab5d", "#c6dbef", "#2171b5"], join=False,  ci="sd", dodge=0.3)
ax3.set_xlabel("Antibiotic Drug", fontsize=12)
ax3.set_ylabel("MIC Value (mg/L)", fontsize=12)
ax3.get_legend().set_visible(False)
ax3.axhline(0.5, ls=':')
ax3.set_ylim(0,10)

COL = EC_new.loc[EC_new['Antibiotic_Drug'] == 'COL']
sns.pointplot(x="Antibiotic_Drug", y="MIC_Value(mg/L)", hue="Group", data=COL, col="Antibiotic_Drug", ax=ax4, palette=["#fcc5c0", "#e7298a", "#c7e9c0", "#41ab5d", "#c6dbef", "#2171b5"], join=False,  ci="sd", dodge=0.3)
ax4.set_xlabel("Antibiotic Drug", fontsize=12)
ax4.set_ylabel("MIC Value (mg/L)", fontsize=12)
ax4.get_legend().set_visible(False)
ax4.axhline(2, ls=':')
ax4.set_ylim(0,10)

FOT = EC_new.loc[EC_new['Antibiotic_Drug'] == 'FOT']
sns.pointplot(x="Antibiotic_Drug", y="MIC_Value(mg/L)", hue="Group", data=FOT, col="Antibiotic_Drug", ax=ax5, palette=["#fcc5c0", "#e7298a", "#c7e9c0", "#41ab5d", "#c6dbef", "#2171b5"], join=False,  ci="sd", dodge=0.3)
ax5.set_xlabel("Antibiotic Drug", fontsize=12)
ax5.set_ylabel("MIC Value (mg/L)", fontsize=12)
ax5.legend(loc='upper left', title="Group", bbox_to_anchor=(1, 0.5),shadow=True, fancybox=True, borderpad=1)
ax5.axhline(2, ls=':')
ax5.set_ylim(0,10)

GEN = EC_new.loc[EC_new['Antibiotic_Drug'] == 'GEN']
sns.pointplot(x="Antibiotic_Drug", y="MIC_Value(mg/L)", hue="Group", data=GEN, col="Antibiotic_Drug", ax=ax6, palette=["#fcc5c0", "#e7298a", "#c7e9c0", "#41ab5d", "#c6dbef", "#2171b5"], join=False,  ci="sd", dodge=0.3)
ax6.set_xlabel("Antibiotic Drug", fontsize=12)
ax6.set_ylabel("MIC Value (mg/L)", fontsize=12)
ax6.get_legend().set_visible(False)
ax6.axhline(2, ls=':')
ax6.set_ylim(0,40)

MERO = EC_new.loc[EC_new['Antibiotic_Drug'] == 'MERO']
sns.pointplot(x="Antibiotic_Drug", y="MIC_Value(mg/L)", hue="Group", data=MERO, col="Antibiotic_Drug", ax=ax7, palette=["#fcc5c0", "#e7298a", "#c7e9c0", "#41ab5d", "#c6dbef", "#2171b5"], join=False,  ci="sd", dodge=0.3)
ax7.set_xlabel("Antibiotic Drug", fontsize=12)
ax7.set_ylabel("MIC Value (mg/L)", fontsize=12)
ax7.get_legend().set_visible(False)
ax7.axhline(8, ls=':')
ax7.set_ylim(0,10)

TAZ = EC_new.loc[EC_new['Antibiotic_Drug'] == 'TAZ']
sns.pointplot(x="Antibiotic_Drug", y="MIC_Value(mg/L)", hue="Group", data=TAZ, col="Antibiotic_Drug", ax=ax8, palette=["#fcc5c0", "#e7298a", "#c7e9c0", "#41ab5d", "#c6dbef", "#2171b5"], join=False,  ci="sd", dodge=0.3)
ax8.set_xlabel("Antibiotic Drug", fontsize=12)
ax8.set_ylabel("MIC Value (mg/L)", fontsize=12)
ax8.get_legend().set_visible(False)
ax8.axhline(4, ls=':')
ax8.set_ylim(0,10)

TGC = EC_new.loc[EC_new['Antibiotic_Drug'] == 'TGC']
sns.pointplot(x="Antibiotic_Drug", y="MIC_Value(mg/L)", hue="Group", data=TGC, col="Antibiotic_Drug", ax=ax9, palette=["#fcc5c0", "#e7298a", "#c7e9c0", "#41ab5d", "#c6dbef", "#2171b5"], join=False,  ci="sd", dodge=0.3)
ax9.set_xlabel("Antibiotic Drug", fontsize=12)
ax9.set_ylabel("MIC Value (mg/L)", fontsize=12)
ax9.get_legend().set_visible(False)
ax9.axhline(0.5, ls=':')
ax9.set_ylim(0,5)

TMP = EC_new.loc[EC_new['Antibiotic_Drug'] == 'TMP']
sns.pointplot(x="Antibiotic_Drug", y="MIC_Value(mg/L)", hue="Group", data=TMP, col="Antibiotic_Drug", ax=ax10, palette=["#fcc5c0", "#e7298a", "#c7e9c0", "#41ab5d", "#c6dbef", "#2171b5"], join=False,  ci="sd", dodge=0.3)
ax10.set_xlabel("Antibiotic Drug", fontsize=12)
ax10.set_ylabel("MIC Value (mg/L)", fontsize=12)
ax10.get_legend().set_visible(False)
ax10.axhline(4, ls=':')
ax10.set_ylim(0,40)   
plt.savefig('./Antimicrobial_susceptible_testing_folder/Average_Drug_MIC_plots_with_clincal_breakpoints.png', dpi=300, bbox_inches='tight')