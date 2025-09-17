import pandas as pd
from dateutil import parser
from epiweeks import Week
import numpy as np


db_path = '/Users/dikledikek/Desktop/NICD_work/FLU/Influenza_Runs/250805_IRMA/quali/cov/'
pns_metadata = 'coverage_meta.xlsx'
pns_sheet = 'Sheet1'

# Load the original spreadsheet
original_df = pd.read_excel(db_path+pns_metadata, sheet_name=pns_sheet)

##format the columns

# Rename columns
original_df = original_df.rename(columns={
    'Formatted_GISAID': 'Isolate_Name',
    'subtype': 'Subtype',
    'CASE_PERSON_PROVINCE': 'province',
    'CRDM Number': 'Seq_Id (HA)',
    'CRDM Number2': 'Seq_Id (NA)',
    'CRDM Number3': 'Seq_Id (PA)',
    'CRDM Number4': 'Seq_Id (PB1)',
    'CRDM Number5': 'Seq_Id (PB2)',
    'CRDM Number6': 'Seq_Id (NS)',
    'CRDM Number7': 'Seq_Id (NP)',
    'CRDM Number8': 'Seq_Id (MP)',
    'CASE_TEST_SPEC_COLLECTION_DATE': 'Collection_Date',
    'Age': 'Host_Age',
    'CASE_PERSON_PATIENT_SEX': 'Host_Gender'

})

##format the columns
original_df['Isolate_Id'] = pd.Series(dtype='float64')
original_df['Segment_Ids'] = pd.Series(dtype='float64')
original_df['Isolate_Name'] = original_df['Isolate_Name'].str.replace('_25', '/2025', regex=False)
original_df['Lineage'] = pd.Series(dtype='float64')
original_df['Passage_History'] = "Original"
original_df['Location'] = "South Africa"
original_df['sub_province'] = pd.Series(dtype='float64')
original_df['Location_Additional_info'] = pd.Series(dtype='float64')
original_df['Host'] = "Human"
original_df['Host_Additional_info'] = pd.Series(dtype='float64')
original_df['Seq_Id (HE)'] = pd.Series(dtype='float64')
original_df['Seq_Id (P3)'] = pd.Series(dtype='float64')
original_df['Submitting_Sample_Id'] = pd.Series(dtype='float64')
original_df['Authors'] = "Kekana, D; Mnguni, A; Mahlangu, B; Stock A; Nzimande, A; Ismail, A; Wolter, N"
original_df['Originating_Lab_Id'] = "3513"
original_df['Originating_Sample_Id'] = pd.Series(dtype='float64')
original_df['Originating_Sample_Id'] = pd.Series(dtype='float64')


# Ensure Collection_Date is datetime type
original_df['Collection_Date'] = pd.to_datetime(original_df['Collection_Date'])

# Extract month (as number 1-12)
original_df['Collection_Month'] = original_df['Collection_Date'].dt.month

original_df['Collection_Year'] = original_df['Collection_Date'].dt.year

original_df['Antigen_Character'] = pd.Series(dtype='float64')
original_df['Adamantanes_Resistance_geno'] = pd.Series(dtype='float64')
original_df['Oseltamivir_Resistance_geno'] = pd.Series(dtype='float64')
original_df['Zanamivir_Resistance_geno'] = pd.Series(dtype='float64')
original_df['Peramivir_Resistance_geno'] = pd.Series(dtype='float64')
original_df['Other_Resistance_geno'] = pd.Series(dtype='float64')
original_df['Adamantanes_Resistance_pheno'] = pd.Series(dtype='float64')
original_df['Oseltamivir_Resistance_pheno'] = pd.Series(dtype='float64')
original_df['Zanamivir_Resistance_pheno'] = pd.Series(dtype='float64')
original_df['Peramivir_Resistance_pheno'] = pd.Series(dtype='float64')
original_df['Other_Resistance_pheno'] = pd.Series(dtype='float64')

original_df['Host_Gender'] = original_df['Host_Gender'].str.replace('Female', 'F', regex=False)
original_df['Host_Gender'] = original_df['Host_Gender'].str.replace('Male', 'M', regex=False)

original_df['Host_Age_Unit'] = np.where(original_df['Host_Age'].notna(), 'Y', '')
original_df['Health_Status'] = pd.Series(dtype='float64')
original_df['Note'] = pd.Series(dtype='float64')
original_df['PMID'] = pd.Series(dtype='float64')

# Reorder columns
original_df = original_df[["Isolate_Id", "Segment_Ids", "Isolate_Name", "Subtype", "Lineage", "Passage_History", "Location", 
                           "province", "sub_province", "Location_Additional_info", "Host", "Host_Additional_info", "Seq_Id (HA)", 
                           "Seq_Id (NA)", "Seq_Id (PB1)", "Seq_Id (PB2)", "Seq_Id (PA)", "Seq_Id (MP)", "Seq_Id (NS)", "Seq_Id (NP)", 
                           "Seq_Id (HE)", "Seq_Id (P3)", "Submitting_Sample_Id", "Authors", "Originating_Lab_Id", "Originating_Sample_Id", 
                           "Collection_Month", "Collection_Year", "Collection_Date", "Antigen_Character", "Adamantanes_Resistance_geno", 
                           "Oseltamivir_Resistance_geno", "Zanamivir_Resistance_geno", "Peramivir_Resistance_geno", "Other_Resistance_geno", 
                           "Adamantanes_Resistance_pheno", "Oseltamivir_Resistance_pheno", "Zanamivir_Resistance_pheno", "Peramivir_Resistance_pheno", 
                           "Other_Resistance_pheno", "Host_Age", "Host_Age_Unit", "Host_Gender", "Health_Status", "Note", "PMID"
]]



# Save the filtered data to a new spreadsheet
original_df[["Seq_Id (HA)", "Seq_Id (NA)", "Seq_Id (PB1)", "Seq_Id (PB2)", "Seq_Id (PA)", "Seq_Id (MP)", "Seq_Id (NS)", "Seq_Id (NP)"]].stack().to_csv(db_path+'ids_GISAID.txt', index=False, header=False)

original_df.to_excel(db_path+"template_GISAID_250805.xlsx", index=False)


####output file for GISAID fasta

# Explicit list of the 8 columns
crdm_columns = [
    "Seq_Id (HA)",
    "Seq_Id (NA)",
    "Seq_Id (PA)",
    "Seq_Id (PB1)",
    "Seq_Id (PB2)",
    "Seq_Id (NS)",
    "Seq_Id (NP)",
    "Seq_Id (MP)",
]

# Collect values
values = []
for col in crdm_columns:
    if col in original_df.columns:
        values.extend(original_df[col].dropna().astype(str))

# Write to file
with open(db_path+"ids_GISAID.txt", "w") as f:
    f.write("\n".join(values))





