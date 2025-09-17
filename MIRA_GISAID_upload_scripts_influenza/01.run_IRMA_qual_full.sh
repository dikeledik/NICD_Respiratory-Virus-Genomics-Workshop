#!/bin/zsh

WORKING_PATH="/Users/dikledikek/Desktop/NICD_work/FLU/Influenza_Runs/Influenza_fastQC/IRMA"

cd $WORKING_PATH

find "$WORKING_PATH" -depth -type d -name '*-*' -exec bash -c 'for d; do p=${d%/*}; b=${d##*/}; dst="$p/${b//-/_}"; [[ "$d" = "$dst" || -e "$dst" ]] || mv -n -- "$d" "$dst"; done' bash {} +

ls -d */ | sed 's:/$::' > ids.txt

mkdir $WORKING_PATH/"HA_all"
mkdir $WORKING_PATH/"NA_all"
mkdir $WORKING_PATH/"PA_all"
mkdir $WORKING_PATH/"PB1_all"
mkdir $WORKING_PATH/"PB2_all"
mkdir $WORKING_PATH/"MP_all"
mkdir $WORKING_PATH/"NS_all"
mkdir $WORKING_PATH/"NP_all"


while read id
do
    echo ${id}
    cd $WORKING_PATH/$id/
   
    mkdir $WORKING_PATH/HA_all/${id}-HA
    qualimap bamqc -nt 12 -bam *_HA*.bam -c -nw 400 -hm 3 -outdir $WORKING_PATH/HA_all/${id}-HA
    

    mkdir $WORKING_PATH/NA_all/${id}-NA
    qualimap bamqc -nt 12 -bam *_NA*.bam -c -nw 400 -hm 3 -outdir $WORKING_PATH/NA_all/${id}-NA
    
   
    mkdir $WORKING_PATH/NP_all/${id}-NP
    qualimap bamqc -nt 12 -bam *_NP.bam -c -nw 400 -hm 3 -outdir $WORKING_PATH/NP_all/${id}-NP
    
 
    mkdir $WORKING_PATH/NS_all/${id}-NS
    qualimap bamqc -nt 12 -bam *_NS.bam -c -nw 400 -hm 3 -outdir $WORKING_PATH/NS_all/${id}-NS
    
    mkdir $WORKING_PATH/PA_all/${id}-PA
    qualimap bamqc -nt 12 -bam *_PA.bam -c -nw 400 -hm 3 -outdir $WORKING_PATH/PA_all/${id}-PA
    
   
    mkdir $WORKING_PATH/PB1_all/${id}-PB1
    qualimap bamqc -nt 12 -bam *_PB1.bam -c -nw 400 -hm 3 -outdir $WORKING_PATH/PB1_all/${id}-PB1
    

    mkdir $WORKING_PATH/PB2_all/${id}-PB2
    qualimap bamqc -nt 12 -bam *_PB2.bam -c -nw 400 -hm 3 -outdir $WORKING_PATH/PB2_all/${id}-PB2
    
    
    mkdir $WORKING_PATH/MP_all/${id}-MP
    qualimap bamqc -nt 12 -bam *_MP.bam -c -nw 400 -hm 3 -outdir $WORKING_PATH/MP_all/${id}-MP
    
done < ids.txt

