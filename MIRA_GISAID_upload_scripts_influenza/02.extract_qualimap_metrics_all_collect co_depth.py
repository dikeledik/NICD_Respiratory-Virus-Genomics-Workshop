import os
import shutil
import pandas as pd
from pathlib import Path

# List of directories to process
all_dirs = ['NS_all', 'HA_all', 'NA_all', 'PB1_all',
            'PB2_all', 'NP_all', 'MP_all', 'PA_all']

# Directory to collect all cov_results files
collection_dir = '/Users/dikledikek/Desktop/NICD_work/FLU/Influenza_Runs/Influenza_fastQC/IRMA/'

# Create the collection directory if it doesn't exist
if not os.path.exists(collection_dir):
    os.makedirs(collection_dir)

for qualimap_dir in all_dirs:
    # Set the current directory path
    qualimap_dir_path = collection_dir + qualimap_dir
    os.chdir(qualimap_dir_path)

    # Initialize lists to store data
    ids = []
    cov = []
    reads = []
    depth = []
    bam = []

    # Process each subdirectory within the current directory
    for filename in os.listdir('.'):
        if filename != '.DS_Store' and os.path.isdir(filename):
            subdirectory_path = os.path.join(qualimap_dir_path, filename)
            genome_results_path = os.path.join(subdirectory_path, 'genome_results.txt')

            if os.path.exists(genome_results_path):
                ids.append(filename)  # Sample ID from folder name
                os.chdir(subdirectory_path)
                read = False
                co = False
                deep = False
                bams = False

                # Read the genome_results.txt file
                with open('genome_results.txt') as f:
                    for line in f.readlines():
                        line = line.strip()
                        if 'number of reads' in line:
                            reads.append(line.split(' = ')[1].replace(',', ''))
                            read = True
                        elif '>= 50X' in line:
                            cov.append(line.split(' a ')[1].split(' of')[0])
                            co = True
                        elif 'mean coverageData' in line:
                            depth.append(line.split(' = ')[1].replace(',', ''))
                            deep = True
                        elif 'bam file' in line:
                            bam.append(line.split(' = ')[1].replace(',', ''))
                            bams = True

                    # Print status for the current sample
                    print(filename, read, co, deep, bams)
                    
                    # Handle missing data
                    if not read:
                        reads.append('None')
                    if not co:
                        cov.append('None')
                    if not deep:
                        depth.append('None')
                    if not bams:
                        bam.append('None')

                # Return to the main directory
                os.chdir(qualimap_dir_path)

    # Verify that all lists are of the same length
    print(len(ids), len(cov), len(reads), len(depth), len(bam))
    print(reads)

    # Write the results to a CSV file
    output_file = f'cov_results_{os.path.basename(qualimap_dir)}.csv'
    with open(output_file, 'w') as f:
        f.write("ID\treads\tcoverage\tdepth\tbam\n")
        for idx, val in enumerate(ids):
            try:
                f.write(f"{val}\t{reads[idx]}\t{cov[idx]}\t{depth[idx]}\t{bam[idx]}\n")
            except IndexError:
                print('Error at:', idx, val)

    # Move the output file to the collection directory
    shutil.move(output_file, os.path.join(collection_dir, output_file))

print(f"All cov_results files have been moved to {collection_dir}")

#########this part of the script will convert your ids file into a excel file which you will need for the next script

txt_path = Path(collection_dir+"ids.txt")

# Read lines, strip whitespace, drop empties
samples = [ln.strip() for ln in txt_path.read_text(encoding="utf-8").splitlines()]
samples = [s for s in samples if s]

# Build DataFrame and write Excel
df = pd.DataFrame({"sample": samples})
df.to_excel(collection_dir+"cov.xlsx", index=False)

print(f"Wrote samples.xlsx with {len(df)} rows.")
