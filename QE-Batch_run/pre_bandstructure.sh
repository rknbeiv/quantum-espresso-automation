#!/bin/bash
#
#VERSION       : 1.0.0
#PROGRAMMED BY : Rajesh Prashanth
#MODIFIED DATE : Mon Dec 25 06:08:06 IST 2017
#
#
###########################################################################################
# Global variables
# Please edit this section as required.For more info check env_path.sh script
###########################################################################################
#
. ./env_path.sh
###########################################################################################
# K-Points paths
###########################################################################################
cat > kpath << EOF
12
   0.0000000000     0.0000000000     0.0000000000     10
   0.5000000000     0.0000000000     0.5000000000     10
   0.5000000000     0.2500000000     0.7500000000     10
   0.3750000000     0.3750000000     0.7500000000     10
   0.0000000000     0.0000000000     0.0000000000     10
   0.5000000000     0.5000000000     0.5000000000     10
   0.6250000000     0.2500000000     0.6250000000     10
   0.5000000000     0.2500000000     0.7500000000     10
   0.5000000000     0.5000000000     0.5000000000     10
   0.3750000000     0.3750000000     0.7500000000     1
   0.6250000000     0.2500000000     0.6250000000     10
   0.5000000000     0.0000000000     0.5000000000     1
EOF
###########################################################################################
# NSCF FILE GENERATION
###########################################################################################
sed s/'scf'/'bands'/ $SCF_INP | sed s/{automatic}/crystal_b/ |sed '$d' > $BANDS_NSCF_INP
cat kpath >> $BANDS_NSCF_INP
###########################################################################################
# BANDS CALCULATION
###########################################################################################
#
cat > $BANDS_INP << EOF
&BANDS
outdir='./output',
filband = 'bands.dat',
no_overlap = .true.
/
EOF
