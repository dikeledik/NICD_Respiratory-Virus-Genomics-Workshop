#!/bin/zsh

WORKING_PATH="/Users/dikledikek/Desktop/NICD_work/FLU/Influenza_Runs/Influenza_fastQC/IRMA"

cd $WORKING_PATH

mkdir 'amended_consensus'

while read id
do
	echo ${id}
	cd $WORKING_PATH/$id/'amended_consensus'/
    cp *\.fa $WORKING_PATH/amended_consensus/
done < ids.txt
