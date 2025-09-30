# RSV-GenoScan Analysis Workflow

## 1. Introduction

- RSV-GenoScan is a tool for analysing RSV genomes sequenced by Illumina (single-read or Paired-end) or Nanopore platforms (https://github.com/AlexandreD-bio/RSV-GenoScan)
- The workflow generates whole genome sequence, can determine viral group (and subgroup), and identify mutations in F and G glycoproteins (including drug resistance mutations).

## 2. Download and Installation

- **Note** Save RSV-GenoScan workflow in a directory that has enough storage and **NOT** your `home` directory.

- Open your terminal and download the RSV-GenoScan Github repository in your working directory e.g. `/home/usr/Downloads`

```bash
cd ~/Downloads
git clone https://github.com/AlexandreD-bio/RSV-GenoScan.git
```


### 3. Conda Environment Setup
- Conda is an open source tool for managing software packages and their dependencies across different operating systems.
- It allows users to easily install, update, and switch between multiple versions of software and environments.
-  Choose the appropriate file based on your computer operating system.

### 3.1 Installing Conda
- Conda is an open source package management system and environment management system.

- **Miniconda** is a minimal installer for Conda. It is recommended for most users 

- Download **Miniconda** installer for your operating system from [https://www.anaconda.com/docs/getting-started/miniconda/install#macos-terminal-installer].

- Open the terminal and navigate to your `home` directory.

#### 3.1.1 To install Miniconda on Linux

```bash
cd ~

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-Linux-x86_64.sh
```

#### 3.1.2 To install Miniconda on macOS

```bash
cd ~

curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh

bash Miniconda3-latest-MacOSX-arm64.sh

```
- Follow the installation prompts and enter yes to all yes/no propmts.

#### 3.1.3 Verify installation

```bash
conda --version
```

- **Note:** Always make sure you select the correct version for your OS.
- **Tip:** Always install Conda in your home directory to avoid permission issues.
---


### 3.2 Create a conda environment for RSV-GenoScan
- To create a conda environment with specific tools using a text file, follow these steps:

- Below is a yaml file with a list of libraries and packages required to run RSV-GenoScan.

```bash
name: rsv_genoscan_env

# The channels are ordered by priority
# The bioconda channel is used for bioinformatics tools.
# The conda-forge channel is used for general-purpose packages.

channels:
  - conda-forge
  - bioconda

dependencies:
  - snakemake >=9.6.0
  - python >=3.10,<3.12
  - setuptools
  - biopython
  - pandas 
  - numpy
  - bwa
  - samtools
  - bcftools
  - bedtools
  - fastp
  - fastqc
  - multiqc
  - mafft
  - ete3
  - iqtree
  - raxml
  - firefox
  - geckodriver
  - bokeh
  - selenium
  - seaborn
  - matplotlib
  - openpyxl
  - pip
  

  - pip:
    - pysam ==0.22
```

#### 3.2.1 Create the yaml file

```bash
touch rsv_genoscan_env.yaml
```

- Open the `rsv_genoscan_env.yaml` using your favourite text editor or on the terminal using `nano` or `vim` and copy the the yaml content above to rsv_genoscan_env.yaml

#### 3.2.2 Create and activate `rsv_genoscan_env` conda environment

- On the terminal, with conda activated, create the environment to run RSV-GenoScan

```bash
conda activate

conda env create -f genoscan_conda_env.yaml

conda activate rsv_genoscan_env
```

## 4. Running RSV-GenoScan

### 4.1 Set up your working directory

- On the terminal, create a working directory `RSV_Analysis` in e.g. `Documents` folder 

```bash
cd ~/Documents
mkdir RSV_Analysis
cd RSV_Analysis
```
- Copy the RSV-GenoScan repository from `~/Downloads` to your working directory `~/Documents/RSV_Analysis`.

```bash
cp -r ~/Downloads/RSV-GenoScan .
```
- Copy your `fastq` files into the to `~/Documents/RSV_Analysis`.

### 4.2 Launch RSV-GenoScan

- To launch RSV-GenoScan, run `bash Bash_struct.sh` from within `RSV-GenoScan/Script`

```bash
cd RSV-GenoScan/Script
bash Bash_struct.sh
```

- RSV-GenoScan will prompt you to provide the following information.

1. Number of cores to use - This will be provided as a range based on your computer.
2. Sequencing platform - Illumina () or ONT (2); Choose 1 for Illumina and 2 for ONT.
3. Are your fastq files in `_Input_Dir`. Copy the fastq files to `_Input_Dir` and respond with "Y" when completed.

```bash
cp *.gz RSV-GenoScan/Input_Dir
```
4. library type - Single reads (1) or paired reads (2). Select 1 for single reads and 2 for paired reads

- If all input parameters are correct, the workflow will start genome assembly process.

## 5. Retrieving assembly results
- The assembled genomes are in the folder `RSV-GenoScan/2-FASTA_result_folder`
- the assembly statistics and RSV grouping results are saved in a file `RSV-GenoScan/2.1-Pileup_result_csv_Folder/resume_pileup.csv`

## 5.1 Separating RSVA and RSVB genome sequences to separate folders

- RSV ouputs all genome assemblies in a single folder. For downstrean analysis, RSVA and RSVB sequences are analysed separately.

- The bash script `Analysis/separate_rsv.sh` separates RSVA and RSVB sequences into separate forlder

### 5.1.1 Create the script
- The script is provided below. 

```bash
#!/bin/bash

## Script to separate RSV A and B 
## fasta files into different folders
## Usage: bash separate_rsv.sh <2-FASTA_result_folder>

# get current date and time
today=$(date +"%Y-%m-%d %H:%M")

# get input dir (2-FASTA_result_folder)
input_dir="$1"

if [ $# -eq 0 ]; then
    echo "Usage: bash separate_rsv.sh <path/to/RSV-GenoScan/2-FASTA_result_folder>"
    exit 1
fi

# create directories
mkdir -p $input_dir/RSVA
mkdir -p $input_dir/RSVB

echo "INFO: $today Starting fasta separation"
for rsv_fasta in "$input_dir"/*_A.fasta "$input_dir"/*_B.fasta
do
    case "$rsv_fasta" in
        *_A.fasta)
            cp "$rsv_fasta" "$input_dir/RSVA/"
            ;;
        *_B.fasta)
            cp "$rsv_fasta" "$input_dir/RSVB/"
            ;;
    esac
done
echo "INFO: $today Separation complete!"

```

- In your terminal open a file `separate_fasta.sh` 
```bash
touch separate_fasta.sh
```

- Copy the provided script into `separate_fasta.sh` using your favourite text editor or on the terminal using vim/nano.


- To separete RSVA and RSVB fasta files, run

```bash
bash separate_fasta.sh RSV-GenoScan/2-FASTA_result_folder
```

- This script will create two folders RSVA and RSVB within `RSV-GenoScan/2-FASTA_result_folder` containing the respective fasta sequences.

```bash
RSV-GenoScan/2-FASTA_result_folder/RSVA
RSV-GenoScan/2-FASTA_result_folder/RSVB
```
### 5.1.2 Assembly Statistics

- The assembly statistics are writen to a file `RSV-GenoScan/2.1-Pileup_result_csv_Folder/resume_pileup.csv` 

- RSV-GenoScan produces other output files, however, the genome assemblies and the assembly statistics are the main outputs that you will need for downstream analysis.





