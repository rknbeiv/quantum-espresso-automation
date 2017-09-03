#!/usr/bin/env python
#
#Sun Aug 27 09:20:48 IST 2017

#-------------------------------------------------
#
#

import numpy as np
import sys

cell=np.array([(0.0,0.0,0.0),(0.0,0.0,0.0),(0.0,0.0,0.0)])

atoms = []
coordinates = []

#testfile
#"20170903.test.Si.scf.out" ---Hard coded
#
vc_file = open(sys.argv[1],"r")
for line in vc_file:
	if "number of atoms/cell" in line:
		nat = line.split("=")[1]
	if "Begin final coordinates" in line:
		templine = next(vc_file)
		vol_au =  templine.split()[4]
		vol_ang = templine.split()[7]
		for nextline in vc_file:
			if "CELL_PARAMETERS" in nextline:
				celldm_1 = nextline.split()[2].split(")")[0]
				templine1 = next(vc_file)
				cell[0][0] = templine1.split()[0]
				cell[0][1] = templine1.split()[1]
				cell[0][2] = templine1.split()[2]
				templine2 = next(vc_file)
				cell[1][0] = templine2.split()[0]
				cell[1][1] = templine2.split()[1]
				cell[1][2] = templine2.split()[2]
				templine3 = next(vc_file)
				cell[2][0] = templine3.split()[0]
				cell[2][1] = templine3.split()[1]
				cell[2][2] = templine3.split()[2]
			
			if "ATOMIC_POSITIONS" in nextline:
				for i in range(int(nat)):
					templines = next(vc_file) 
					atom,x,y,z = templines.split()
					atoms.append(atom)
					coordinates.append([float(x),float(y),float(z)])
					
scf_file=open(sys.argv[2],"w")
#
#control
#	calculation,outdir,prefix,pseudo_dir,verbosity,tstress,tprnfor
#system
#	
#
#
#----------------------------------------------------------------------------------
calculation = "\tcalculation = 'scf'\n"
outdir = "\toutdir = './output'\n"
prefix = "\tprefix = Si\n"
pseudo_dir = "\tpseudo_dir = '/home/rajeshprashanth/pseudo'\n"
verbosity = "\tverbosity = 'high'\n"
tstress = "\ttstress = .true.\n"
tprnfor = "\ttprnfor = .true.\n"
#----------------------------------------------------------------------------------
scf_file.write("&CONTROL\n")
scf_file.write(calculation)
scf_file.write(outdir)
scf_file.write(prefix)
scf_file.write(pseudo_dir)
scf_file.write(verbosity)
scf_file.write(tstress)
scf_file.write(tprnfor)
scf_file.write("/\n")


					
vc_file.close()		
scf_file.close()			
			
			
			
			
			
	
print "\n----------------------------"		
print "cell volume (au^3)",vol_au,
print "\ncell volume (ang^3)",vol_ang,
print "\nnumber of atom :",nat,
print "celldm(1) = ",celldm_1,
print "\n----------------------------"		
print "----------------------------"	
for i in range(int(nat)):	
	print atoms[i],"\t",coordinates[i][0],"\t",coordinates[i][1],"\t",coordinates[i][2]


