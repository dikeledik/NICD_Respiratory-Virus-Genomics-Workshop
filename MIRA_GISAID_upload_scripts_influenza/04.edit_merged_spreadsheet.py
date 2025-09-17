# file: add_suffix_and_subtype.py

import pandas as pd

# Load your Excel file
path = '/Users/dikledikek/Desktop/NICD_work/FLU/Influenza_Runs/Influenza_fastQC/IRMA/'
input_file = path + 'coverage_250805.xlsx'  # Replace with your actual filename
output_excel = path + 'coverage_250805_edited.xlsx'
output_sample_txt = path + 'samples_over_90pct_coverage.txt'
output_sample_txt_all = path + 'samples_over_0pct_coverage.txt'

# Define the mapping from column name to suffix
column_suffix_map = {
    'CRDM Number': '_4',
    'CRDM Number2': '_6',
    'CRDM Number3': '_3',
    'CRDM Number4': '_2',
    'CRDM Number5': '_1',
    'CRDM Number6': '_8',
    'CRDM Number7': '_5',
    'CRDM Number8': '_7',
}

# Read Excel
df = pd.read_excel(input_file)

# Apply suffixes
for column, suffix in column_suffix_map.items():
    if column in df.columns:
        df[column] = df[column].astype(str) + suffix

# Add 'subtype' column based on 'BAM_file' contents
def determine_subtype(bam):
    if pd.isna(bam):
        return ''
    if "A_HA_H3.bam" in bam:
        return 'H3N2'
    elif "A_HA_H1.bam" in bam:
        return 'H1N1'
    return ''

if 'BAM_File' in df.columns:
    df['subtype'] = df['BAM_File'].apply(determine_subtype)
else:
    print("Warning: 'BAM_File' column not found in Excel.")


# Add 'type' column based on 'BAM_file' contents
def determine_type(bam):
    if pd.isna(bam):
        return ''
    if "A_" in bam:
        return 'A'
    elif "B_" in bam:
        return 'B'
    return ''

if 'BAM_File' in df.columns:
    df['type'] = df['BAM_File'].apply(determine_type)
else:
    print("Warning: 'BAM_File' column not found in Excel.")


# Filter samples where Coverage_HA > 90%
if 'Coverage_HA' in df.columns and 'sample' in df.columns:
    high_coverage_samples = df[pd.to_numeric(df['Coverage_HA'].str.rstrip('%'), errors='coerce') > 90]['sample']
    high_coverage_samples.dropna().astype(str).to_csv(output_sample_txt, index=False, header=False)
else:
    print("Warning: 'Coverage_HA' or 'sample' column not found.")

# Filter samples where Coverage_HA > 0%
if 'Coverage_HA' in df.columns and 'sample' in df.columns:
    all_coverage_samples = df['sample']
    all_coverage_samples.astype(str).to_csv(output_sample_txt_all, index=False, header=False)
else:
    print("Warning: 'Coverage_HA' or 'sample' column not found.")

# Save Excel
df.to_excel(output_excel, index=False)
print(f"Updated Excel saved to: {output_excel}")
print(f"Sample names with >90% HA coverage saved to: {output_sample_txt}")
