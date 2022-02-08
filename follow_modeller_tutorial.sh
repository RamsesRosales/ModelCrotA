###follow tutorial on  https://salilab.org/modeller/tutorial/basic.html

#example of tutorial 

>P1;TvLDH
sequence:TvLDH:::::::0.00: 0.00
MSEAAHVLITGAAGQIGYILSHWIASGELYGDRQVYLHLLDIPPAMNRLTALTMELEDCAFPHLAGFVATTDPKA
AFKDIDCAFLVASMPLKPGQVRADLISSNSVIFKNTGEYLSKWAKPSVKVLVIGNPDNTNCEIAMLHAKNLKPEN
FSSLSMLDQNRAYYEVASKLGVDVKDVHDIIVWGNHGESMVADLTQATFTKEGKTQKVVDVLDHDYVFDTFFKKI
GHRAWDILEHRGFTSAASPTKAAIQHMKAWLFGTAPGEVLSMGIPVPEGNPYGIKPGVVFSFPCNVDKEGKIHVV
EGFKVNDWLREKLDFTEKDLFHEKEIALNHLAQGG*


###replace TVLDH by our name 

#my names are: 
#Cerrophidion godmani North Crotoxin A (CgNCrotA) Cgodm_PLA2_19
#Cerrophidion godmani South Crotoxin A (CgSCrotA) Cgodm_PLA2_10


nano CgNCrotA.ali
>P1;CgNCrotA
sequence:CgNCrotA:::::::0.00: 0.00
MRTLWIVAVLLVGVEGSLMQFETLIMKIAGRSGVWYYGSYGCYCGAGGQGRPQDASDRCCFVHDCCYGKVTDCDPKKDVYTYSEENGAIVCGGDDPCKKQVCECDKDAAICFRDNKDTYDNKYWFFPAKKCQEESEPC*

nano CgSCrotA.ali

>P1;CgSCrotA
sequence:CgSCrotA:::::::0.00: 0.00
MRTLWIVAVLLVVVEGSPVEFETLIMKIAGRSGVWYYGSYGCYCGAGGQGWPQDASDRCCFEHDCCYRKVTGCDPKLDVYTYREENGDMICGGDDPCEKQICECDKAAAICFRDNKDTYDIKYWFFPAKECQEESEPC*

#make a directory for each one
mkdir CgNCrotA
mkdir CgSCrotA
mv CgN*.ali CgNCrotA
mv CgS*.ali CgSCrotA

###start with the CgNcrotA

>P1;CgCrotB
sequence:CgCrotB:::::::0.00: 0.00
MRTLWIVAVLLVVVEGNLLQFNKMIKLETKKNAVPFYSFYGCYCGWGGRGKPMDATDRCCFEHDCCYGKLTKCNTKSDIYSYSWKSGFIMCGKGSWCEEHICECDRIAAACLRRSLSTYKYGYMFYLDSYCKGPSEKC*


##### make a file assuming that sites 1,4 and 5 where cleaved

nano CgNCrotA1.ali
>P1;CgNCrotA1
sequence:CgNCrotA:::::::0.00: 0.00
GCYCGAGGQGRPQDASDRCCFVHDCCYGKVTDCDPKKDVYTYSEENGAIVCGGDDPCKKQVCECDKDAAICFRDNKDTY*

nano CgSCrotA1.ali

>P1;CgSCrotA1
sequence:CgSCrotA:::::::0.00: 0.00
YGCYCGAGGQGWPQDASDRCCFEHDCCYRKVTGCDPKLDVYTYREENGDMICGGDDPCEKQICECDKAAAICFRDNKDTY*


#run modeller in the two cleaved sequences using the cleavead acidic subunit as reference

parallel -a list -j 2 --verbose " echo {}
cd {}
cp ../Crotoxin/3r0l.pdb .
python ../bin/align2d.py -a {}.ali -p 3r0l.pdb -c A -e C
python ../bin/model-single.py -a {}-3r0lAC.ali -k 3r0lAC -s {} > model-single.log
rm 3r0l.pdb"

parallel -a list -j 2 --verbose " echo {}
mkdir {}_1
cd {}_1
cp ../{}/{}.ali .
cp ../Crotoxin/3r0l.pdb .
python ../bin/align2d.py -a {}.ali -p 3r0l.pdb -c D
python ../bin/model-single.py -a {}-3r0lD.ali -k 3r0lD -s {} > model-single.log
rm 3r0l.pdb"


######### cleaveage of the sites 2 and 3 

nano CgNCrotA2.ali
>P1;CgNCrotA2
sequence:CgNCrotA:::::::0.00: 0.00
GCYCGAGGQGRPQDASDRCCFVHDCCYGKVTDCDPKKDVSEENGAIVCGGDDPCKKQVCECDKDAAICFRDNKDTY*

nano CgSCrotA2.ali

>P1;CgSCrotA2
sequence:CgSCrotA2:::::::0.00: 0.00
YGCYCGAGGQGWPQDASDRCCFEHDCCYRKVTGCDPKLEENGDMICGGDDPCEKQICECDKAAAICFRDNKDTY*

###### modified the list to just have the base name, I have to add the 1 or 2 or 1_1 
parallel -a list -j 2 --verbose " echo {}
cd {}2
cp ../Crotoxin/3r0l.pdb .
python ../bin/align2d.py -a {}2.ali -p 3r0l.pdb -c A -e C
python ../bin/model-single.py -a {}2-3r0lAC.ali -k 3r0lAC -s {} > model-single.log
rm 3r0l.pdb"