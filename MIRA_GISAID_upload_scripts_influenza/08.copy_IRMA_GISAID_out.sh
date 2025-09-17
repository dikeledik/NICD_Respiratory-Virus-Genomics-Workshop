#!/bin/zsh

WORKING_PATH="/Users/dikledikek/Desktop/NICD_work/FLU/Influenza_Runs/Influenza_fastQC/IRMA/amended_consensus"

cd $WORKING_PATH

mkdir 'GISAID'

while read id
do
	echo ${id}
    cp ${id}.fa $WORKING_PATH/GISAID/
done < ids_GISAID.txt

cd $WORKING_PATH/GISAID/
cat *\.fa > GISAID_250805.fasta
