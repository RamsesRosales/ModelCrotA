#!/Users/ramsesrosales/opt/anaconda3/envs/modeller_env/bin/python

import argparse

parser = argparse.ArgumentParser(description = "modified code from https://salilab.org/modeller/tutorial/basic.html to make a sigle model")
parser.add_argument("-a","--ali",
								type=str,
								help="ali file")
parser.add_argument("-k","--known",
								type=str,
								help="path to the pdb file  of the reference")

parser.add_argument("-s","--sequence",
								type=str,
								default="A",
								help="which chain from the pdb file are you using, if you only use one you just need these flag")


args = parser.parse_args()

a = args.ali
k = args.known
s = args.sequence


from modeller import *
from modeller.automodel import *
#from modeller import soap_protein_od

env = Environ()
a = AutoModel(env, alnfile= a,
              knowns= k, sequence= s,
              assess_methods=(assess.DOPEHR,
                              #soap_protein_od.Scorer(),
                              assess.GA341))

a.library_schedule = autosched.slow
a.max_var_iterations = 500
a.md_level = refine.slow
a.repeat_optimization = 4
a.starting_model = 1
a.ending_model = 10
a.make()