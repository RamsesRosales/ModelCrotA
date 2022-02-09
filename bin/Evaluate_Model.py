#!/Users/ramsesrosales/opt/anaconda3/envs/modeller_env/bin/python

import argparse
from pickle import FALSE, TRUE


parser = argparse.ArgumentParser(description = "modified code from https://salilab.org/modeller/tutorial/basic.html to evaluate a model")
parser.add_argument("-m","--model",
								type=str,
								help="model file to evaluate in pdb format")

parser.add_argument("-o","--output",
								type=str,
								default="model",
								help="name for the output, will be <name>.profile")

parser.add_argument("-r","--dopehr",
								type=bool,
								default=FALSE,
								help="set true to use dopehd instead of dope")

args = parser.parse_args()

if not args.model:
    print("give a input pdb file to evaluate, use flag -m")
    quit()


m = args.model
output = args.output


from modeller import *
from modeller.scripts import complete_pdb

log.verbose()    # request verbose output
env = Environ()
env.libs.topology.read(file='$(LIB)/top_heav.lib') # read topology
env.libs.parameters.read(file='$(LIB)/par.lib') # read parameters

# read model file
mdl = complete_pdb(env, m)

# Assess with DOPE:


if args.dopehr == FALSE:
    s = Selection(mdl)   # all atom selection
    s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file=str(output + ".profile"),
              normalize_profile=True, smoothing_window=15)

if args.dopehr == TRUE:
    s = Selection(mdl)   # all atom selection
    s.assess_dopehr(output='ENERGY_PROFILE NO_REPORT', file=str(output + ".profile"),
              normalize_profile=True, smoothing_window=15)

