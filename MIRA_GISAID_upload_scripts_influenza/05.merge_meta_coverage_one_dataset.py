import pandas as pd

# Load the data (modify file paths as needed)
path='/Users/dikledikek/Desktop/NICD_work/FLU/Influenza_Runs/250805_IRMA/quali/cov/'
coverage_next = pd.read_excel(path+'coverage_250805_edited.xlsx', sheet_name="Sheet1")  # Replace with your file path

# Load the two Excel sheets
meta = pd.read_excel(path+'Labslip_metadata.xlsx')

####DD FORMATING FOR SEGMENTS ID FOR GISAID

print(meta)

# Merge the dataframes on the 'sample' column
merge_flu = pd.merge(coverage_next, meta, on='sample', how='outer') ####make sure that the id's colunm in the metadata file and the coverage file is "sample"

# Save the merged dataframe to an Excel file
output_path = path+'coverage_meta.xlsx'
merge_flu.to_excel(output_path, index=False)

print(f'Merged file saved at: {output_path}')
