#!/bin/bash
echo erase models of $1 from $2

rm ${2}/${1}.B*.pdb
rm ${2}/${1}.D*
rm ${2}/${1}.V*
rm ${2}/*.ini
rm ${2}/*.rsr
rm ${2}/*.sch
