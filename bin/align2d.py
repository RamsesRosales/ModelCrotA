#!/Users/ramsesrosales/opt/anaconda3/envs/modeller_env/bin/python

import argparse

parser = argparse.ArgumentParser(description = "modified code from https://salilab.org/modeller/tutorial/basic.html to make alignment of your protein with a pdb refernce")
parser.add_argument("-a","--ali",
								type=str,
								help="ali file")
parser.add_argument("-p","--pdb",
								type=str,
								help="path to the pdb file  of the reference")

parser.add_argument("-c","--chain",
								type=str,
								default="A",
								help="which chain from the pdb file are you using, if you only use one you just need these flag")

parser.add_argument("-e","--end",
								type=str,
                                default= "SAME",
								help="the final chain to use from the pdb file, if you just use one chain dont set these variable")


args = parser.parse_args()

if not args.ali:
    print("give the path to the protein that you want to use in .ali format with the flag -a")
    quit()

if not args.pdb:
    print("give the path to the protein data base that you want to use as referemce format with the flag -p")
    quit()

from modeller import *

a = args.ali.split('.')[0]
p = args.pdb.split('.')[0]

aa= a.split("/")[-0]
pp= p.split("/")[-0]

c = args.chain
e = args.end


env = Environ()
aln = Alignment(env)

if e == "SAME":
    print("the chain to start and end will be the same")
    mdl = Model(env, file = pp, model_segment=(str('FIRST:'+c),str('LAST:'+c)))
    aln.append_model(mdl, align_codes= str(pp+c), atom_files=str(p+'.pdb'))
    aln.append(file= str(a+'.ali'), align_codes= aa)
    aln.align2d(max_gap_length=50)
    aln.write(file=str(aa + '-' + str(p+c)+ '.ali'), alignment_format='PIR')
    aln.write(file=str(aa + '-' + str(p+c)+ '.pap'), alignment_format='PAP')
    quit()


mdl = Model(env, file = pp, model_segment=(str('FIRST:'+c),str('LAST:'+e)))
aln.append_model(mdl, align_codes= str(pp+c+e), atom_files=str(p+'.pdb'))
aln.append(file= str(a+'.ali'), align_codes= aa)
aln.align2d(max_gap_length=50)
aln.write(file=str(aa + '-' + str(p+c+e)+ '.ali'), alignment_format='PIR')
aln.write(file=str(aa + '-' + str(p+c+e)+ '.pap'), alignment_format='PAP')





