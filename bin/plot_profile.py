#!/bin/env  python

import argparse
from pickle import FALSE, TRUE
from re import S


parser = argparse.ArgumentParser(description = "modified code from https://salilab.org/modeller/tutorial/basic.html to plot DOPE profile")
parser.add_argument("-a","--ali",
								type=str,
								help="aligment of the two sequences to compare")

parser.add_argument("-k","--known",
								type=str,
								help="name of the known profile, the profile should be written as <known>.profile")

parser.add_argument("-s","--sequence",
								type=str,
								help="name of the target profile, the profile should be written as <sequence>.profile")
parser.add_argument("-c","--chain",
								type=str,
                                default="A",
								help="chains")

args = parser.parse_args()

if not args.ali:
    print("missing argument --ali")
    quit()
if not args.known:
    print("missing argument --known")
    quit()
if not args.sequence:
    print("missing argument --sequence")
    quit()


ali = args.ali
k = args.known
s = args.sequence
c = args.chain


import pylab
import modeller

def r_enumerate(seq):
    """Enumerate a sequence in reverse order"""
    # Note that we don't use reversed() since Python 2.3 doesn't have it
    num = len(seq) - 1
    while num >= 0:
        yield num, seq[num]
        num -= 1

def get_profile(profile_file, seq):
    """Read `profile_file` into a Python array, and add gaps corresponding to
       the alignment sequence `seq`."""
    # Read all non-comment and non-blank lines from the file:
    f = open(profile_file)
    vals = []
    for line in f:
        if not line.startswith('#') and len(line) > 10:
            spl = line.split()
            vals.append(float(spl[-1]))
    # Insert gaps into the profile corresponding to those in seq:
    for n, res in r_enumerate(seq.residues):
        for gap in range(res.get_leading_gaps()):
            vals.insert(n, None)
    # Add a gap at position '0', so that we effectively count from 1:
    vals.insert(0, None)
    return vals

e = modeller.Environ()
a = modeller.Alignment(e, file=ali)

template = get_profile(str(k + '.profile'), a[str(k+c)])
model = get_profile(str(s+ '.profile'), a[s])

# Plot the template and model profiles in the same plot for comparison:
pylab.figure(1, figsize=(10,6))
pylab.xlabel('Alignment position')
pylab.ylabel('DOPE per-residue score')
pylab.plot(model, color='red', linewidth=2, label='Model')
pylab.plot(template, color='green', linewidth=2, label='Template')
pylab.legend()
pylab.savefig('dope_profile.png', dpi=65)