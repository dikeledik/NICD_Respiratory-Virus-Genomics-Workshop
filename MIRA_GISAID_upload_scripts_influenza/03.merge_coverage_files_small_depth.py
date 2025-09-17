import pandas as pd
import sys

path = '/Users/dikledikek/Desktop/NICD_work/FLU/Influenza_Runs/Influenza_fastQC/IRMA/'
ha_file = 'cov_results_HA_all.csv' 
na_file = 'cov_results_NA_all.csv'
pa_file = 'cov_results_PA_all.csv'
pb1_file = 'cov_results_PB1_all.csv'
pb2_file = 'cov_results_PB2_all.csv'
mp_file = 'cov_results_MP_all.csv'
ns_file = 'cov_results_NS_all.csv'
np_file = 'cov_results_NP_all.csv'
metadata_file = 'cov.xlsx'
outfile = 'coverage_250805.xlsx'

# column in metadta containin IDs
merge_id_col = 'sample'

# determine if extra metadata kept
#want_african_country = False

# determine if have years (i.e. PNS samples)
#add_pns_year = True


# read in all files and drop unneeded columns
def read_files_for_merge(file_path, ha_filename, na_filename, pa_filename, pb1_filename, pb2_filename, ns_filename, np_filename, mp_filename, meta_id_filename):
    """Read in all files and drop columns not needed.

    Parameters
    __________
    file_path: str
        Path to files of interest
    ha_filename: str
        coverage output from qualimap
    na_filename: str
        coverage output from qualimap
    pa_filename: str
        coverage output from qualimap
    pb1_filename: str
        coverage output from qualimap
    pb2_filename: str
        coverage output from qualimap
    ns_filename: str
        coverage output from qualimap
    np_filename: str
        coverage output from qualimap
    mp_filename: str
        coverage output from qualimap
    meta_id_filename: str
        Excel file containing IDs to be reported
    
    Returns
    _______
    All information as separate dataframes if files are present
    If missing file: prints error message for the file returns -1 for that file.
    """

    # determine if can continue after this function
    # initially tried to set failed df to False/None but always gave
    # ValueError: The truth value of a DataFrame is ambiguous
    all_dfs_read = True

    try:
        ha_df = pd.read_csv(file_path+ha_filename, sep='\t')
        ha_df = ha_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        ha_df = ha_df.fillna(0)
        ha_df = ha_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_HA',
    'coverage': 'Coverage_HA',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})

    except KeyError:
        ha_df = pd.read_csv(file_path+ha_filename, sep=',')
        ha_df = ha_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        ha_df = ha_df.fillna(0)
        ha_df = ha_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_HA',
    'coverage': 'Coverage_HA',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except FileNotFoundError:
        print('Could not find sequencing metrics file "'+ ha_filename+ '" in', file_path, 'folder. Please double check path and filenames and try again.')
        ha_df = None  # return correct number of vals even if can't read
        all_dfs_read = False 

    try:
        na_df = pd.read_csv(file_path+na_filename, sep='\t')
        na_df = na_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        na_df = na_df.fillna(0)
        na_df = na_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_NA',
    'coverage': 'Coverage_NA',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except KeyError:
        na_df = pd.read_csv(file_path+na_filename, sep=',')
        na_df = na_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        na_df = na_df.fillna(0)
        na_df = na_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_NA',
    'coverage': 'Coverage_NA',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except FileNotFoundError:
        print('Could not find sequencing metrics file "'+ na_filename+ '" in', file_path, 'folder. Please double check path and filenames and try again.')
        na_df = None  # return correct number of vals even if can't read
        all_dfs_read = False 

    try:
        pa_df = pd.read_csv(file_path+pa_filename, sep='\t')
        pa_df = pa_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        pa_df = pa_df.fillna(0)
        pa_df = pa_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_PA',
    'coverage': 'Coverage_PA',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except KeyError:
        pa_df = pd.read_csv(file_path+pa_filename, sep=',')
        pa_df = pa_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        pa_df = pa_df.fillna(0)
        pa_df = pa_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_PA',
    'coverage': 'Coverage_PA',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except FileNotFoundError:
        print('Could not find sequencing metrics file "'+ pa_filename+ '" in', file_path, 'folder. Please double check path and filenames and try again.')
        pa_df = None  # return correct number of vals even if can't read
        all_dfs_read = False 

    try:
        pb1_df = pd.read_csv(file_path+pb1_filename, sep='\t')
        pb1_df = pb1_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        pb1_df = pb1_df.fillna(0)
        pb1_df = pb1_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_PB1',
    'coverage': 'Coverage_PB1',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except KeyError:
        pb1_df = pd.read_csv(file_path+pb1_filename, sep=',')
        pb1_df = pb1_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        pb1_df = pb1_df.fillna(0)
        pb1_df = pb1_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_PB1',
    'coverage': 'Coverage_PB1',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except FileNotFoundError:
        print('Could not find sequencing metrics file "'+ pb1_filename+ '" in', file_path, 'folder. Please double check path and filenames and try again.')
        pb1_df = None  # return correct number of vals even if can't read
        all_dfs_read = False 

    try:
        pb2_df = pd.read_csv(file_path+pb2_filename, sep='\t')
        pb2_df = pb2_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        pb2_df = pb2_df.fillna(0)
        pb2_df = pb2_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_PB2',
    'coverage': 'Coverage_PB2',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except KeyError:
        pb2_df = pd.read_csv(file_path+pb2_filename, sep=',')
        pb2_df = pb2_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        pb2_df = pb2_df.fillna(0)
        pb2_df = pb2_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_PB2',
    'coverage': 'Coverage_PB2',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except FileNotFoundError:
        print('Could not find sequencing metrics file "'+ pb2_filename+ '" in', file_path, 'folder. Please double check path and filenames and try again.')
        pb2_df = None  # return correct number of vals even if can't read
        all_dfs_read = False  

    try:
        ns_df = pd.read_csv(file_path+ns_filename, sep='\t')
        ns_df = ns_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        ns_df = ns_df.fillna(0)
        ns_df = ns_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_NS',
    'coverage': 'Coverage_NS',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except KeyError:
        ns_df = pd.read_csv(file_path+ns_filename, sep=',')
        ns_df = ns_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        ns_df = ns_df.fillna(0)
        ns_df = ns_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_NS',
    'coverage': 'Coverage_NS',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except FileNotFoundError:
        print('Could not find sequencing metrics file "'+ ns_filename+ '" in', file_path, 'folder. Please double check path and filenames and try again.')
        ns_df = None  # return correct number of vals even if can't read
        all_dfs_read = False 

    try:
        np_df = pd.read_csv(file_path+np_filename, sep='\t')
        np_df = np_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        np_df = np_df.fillna(0)
        np_df = np_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_NP',
    'coverage': 'Coverage_NP',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except KeyError:
        np_df = pd.read_csv(file_path+np_filename, sep=',')
        np_df = np_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        np_df = np_df.fillna(0)
        np_df = np_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_NP',
    'coverage': 'Coverage_NP',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except FileNotFoundError:
        print('Could not find sequencing metrics file "'+ np_filename+ '" in', file_path, 'folder. Please double check path and filenames and try again.')
        np_df = None  # return correct number of vals even if can't read
        all_dfs_read = False 

    try:
        mp_df = pd.read_csv(file_path+mp_filename, sep='\t')
        mp_df = mp_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        mp_df = mp_df.fillna(0)
        mp_df = mp_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_MP',
    'coverage': 'Coverage_MP',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except KeyError:
        mp_df = pd.read_csv(file_path+mp_filename, sep=',')
        mp_df = mp_df[['ID', 'reads', 'coverage', 'depth', 'bam']]
        mp_df = mp_df.fillna(0)
        mp_df = mp_df.rename(columns={
    'ID': 'ID',
    'reads': 'Reads_MP',
    'coverage': 'Coverage_MP',
    'depth': 'mean_depth',
    'bam': 'BAM_File'
})
    except FileNotFoundError:
        print('Could not find sequencing metrics file "'+ mp_filename+ '" in', file_path, 'folder. Please double check path and filenames and try again.')
        mp_df = None  # return correct number of vals even if can't read
        all_dfs_read = False 

    try:
        metadata_id_df = pd.read_excel(file_path+meta_id_filename, engine='openpyxl')
        # if add_pns_year:
        #     metadata_id_df['PNS'] = metadata_id_df['PNS'].map(lambda x: x.replace('_2', '-2') if '_2' in x else x)
            #meta_df = meta_df[~meta_df.Country.str.contains("Lesotho")]  # filter out unwanted country
    except FileNotFoundError:
        print('Could not find metadata/ID file "'+ meta_id_filename+ '" in', file_path, 'folder. Please double check path and filenames and try again.')
        metadata_id_df = None
        all_dfs_read = False

    return ha_df, na_df, pa_df, pb1_df, pb2_df, ns_df, np_df, mp_df, metadata_id_df, all_dfs_read


# Extract just ID from ID column by removing known prefixes and suffixes
def standardise_id(df_to_clean, id_column_name, remove_ha_tag=True, remove_na_tag=True, remove_pa_tag=True, remove_pb1_tag=True, remove_pb2_tag=True, remove_ns_tag=True, remove_np_tag=True, remove_mp_tag=True):
    """Extract just ID from ID column by removing known prefixes and suffixes

    Parameters
    __________
    df_to_clean: pd.DataFrame
        Dataframe containing ID column and other required info
    id_column_name: str
        Name of column in dataframe containing IDs
    remove_ha_tag: bool
        True if need to remove _S tags (default: True)
    remove_na_tag: bool
        True if need to remove _S tags (default: True)
    remove_pa_tag: bool
        True if need to remove _S tags (default: True)
    remove_pb1_tag: bool
        True if need to remove _S tags (default: True)
    remove_pb2_tag: bool
        True if need to remove _S tags (default: True)
    remove_ns_tag: bool
        True if need to remove _S tags (default: True)
    remove_np_tag: bool
        True if need to remove _S tags (default: True)
    remove_mp_tag: bool
        True if need to remove _S tags (default: True)

    Operates in-place on dataframes and does not return anything.
    """
    if remove_ha_tag:
        df_to_clean['CRDM Number'] = df_to_clean[id_column_name].map(lambda x: x.split('-')[0])
        df_to_clean.drop(labels=id_column_name, axis=1, inplace=True)

    # elif remove_na_tag:
    #     df_to_clean['CRDM Number'] = df_to_clean[id_column_name].map(lambda x: x.split('_NA')[1])
    #     df_to_clean.drop(labels=id_column_name, axis=1, inplace=True)

    # elif remove_pa_tag:
    #     df_to_clean['CRDM Number'] = df_to_clean[id_column_name].map(lambda x: x.split('_PA')[2])
    #     df_to_clean.drop(labels=id_column_name, axis=1, inplace=True)

    # elif remove_pb1_tag:
    #     df_to_clean['CRDM Number'] = df_to_clean[id_column_name].map(lambda x: x.split('_PB1')[3])
    #     df_to_clean.drop(labels=id_column_name, axis=1, inplace=True)

    # elif remove_pb2_tag:
    #     df_to_clean['CRDM Number'] = df_to_clean[id_column_name].map(lambda x: x.split('_PB2')[4])
    #     df_to_clean.drop(labels=id_column_name, axis=1, inplace=True)

    # elif remove_ns_tag:
    #     df_to_clean['CRDM Number'] = df_to_clean[id_column_name].map(lambda x: x.split('_NS')[5])
    #     df_to_clean.drop(labels=id_column_name, axis=1, inplace=True)

    # elif remove_np_tag:
    #     df_to_clean['CRDM Number'] = df_to_clean[id_column_name].map(lambda x: x.split('_NP')[6])
    #     df_to_clean.drop(labels=id_column_name, axis=1, inplace=True)

    # elif remove_mp_tag:
    #     df_to_clean['CRDM Number'] = df_to_clean[id_column_name].map(lambda x: x.split('_MP')[7])
    #     df_to_clean.drop(labels=id_column_name, axis=1, inplace=True)

    # else:
    #     df_to_clean['CRDM Number'] = df_to_clean[id_column_name]
    #     df_to_clean.drop(labels=id_column_name, axis=1, inplace=True)

        
    print(df_to_clean.head())

# get info
ha_df, na_df, pa_df, pb1_df, pb2_df, ns_df, np_df, mp_df, meta_df, all_info_read = read_files_for_merge(path, ha_file, na_file, pa_file, pb1_file, pb2_file, np_file, ns_file, mp_file, metadata_file)

# df order: seq_df, lin_df, pango_df, nc_df
sample_col_names = ['ID', 'ID', 'ID', 'ID', 'ID', 'ID', 'ID', 'ID']
# remove_scf, add_year_for_pns, remove_gisaid - set for each df (in order given in line 149)
cleaning = [[True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True]]
dfs = [ha_df, na_df, pa_df, pb1_df, pb2_df, ns_df, np_df, mp_df]

# only proceed if all files present and read correctly
if all_info_read:
    for idx, (working_df, column_name) in enumerate(zip(dfs, sample_col_names)):
        standardise_id(working_df, column_name, cleaning[idx][0], cleaning[idx][1], cleaning[idx][2], cleaning[idx][3], cleaning[idx][4], cleaning[idx][5], cleaning[idx][6], cleaning[idx][7])

    # want metadata df as first columns, merge into this
    suffix = 1  # add suffix to prevent future MergeError
    for df in dfs:  # defined on line 120
        # left merge on sequencing number
        print(df.head())
        meta_df = meta_df.merge(df, how='left', left_on=merge_id_col, right_on='CRDM Number', suffixes=['', str(suffix)])
        suffix += 1

    meta_df.to_excel(path+outfile)

else:
    pass  # error message already printed in try-except blocks
