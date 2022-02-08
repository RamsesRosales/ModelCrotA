Models of Crotoxin like molecules from Cerrophidion.
================
Ramses A. Rosales-Garcia, Rhett M. Rautsaw , Erich P. Hofmann, Christoph
I. Grunwald, Jason M. Jones, Hector Franz-Chavez, Ivan T.
Ahumada-Carrillo, Ricardo Ramirez-Chaparro, Miguel Angel De la
Torre-Loranca, Jason L. Strickland, Andrew J. Mason, Matthew L. Holding,
Miguel Borja, Gamaliel Castaneda-Gaytan, Darin R. Rokyta, Tristan D.
Schramer, N. Jade Mellor, Edward A. Myers, Christopher Parkinson
2022 February 07

  - [Crotoxin-like Subunit](#crotoxin-like-subunit)
      - [CgCrotB](#cgcrotb)
      - [Crotoxin-like Acidic Subunit](#crotoxin-like-acidic-subunit)

Models were made following modeller basic tutorial using especifications
from Wintingtton et al.

# Crotoxin-like Subunit

General pipeline was to print the translated sequence in ali format:

``` bash
cat CgCrotB/CgCrotB.ali
```

    ## >P1;CgCrotB
    ## sequence:CgCrotB:::::::0.00: 0.00
    ## MRTLWIVAVLLVVVEGNLLQFNKMIKLETKKNAVPFYSFYGCYCGWGGRGKPMDATDRCCFEHDCCYGKLTKCNTKSDIYSYSWKSGFIMCGKGSWCEEHICECDRIAAACLRRSLSTYKYGYMFYLDSYCKGPSEKC*

To set the right format you have to substitute the name of you protein
and the sequence, but let the other stuff you have to set a \* as stop
at the end

The general pipeline is two python scripts taken from the modeller basic
tutorial that are present in the bin file

``` bash
ls bin
```

    ## align2d.py
    ## build_profile.py
    ## model-single.py

I used parallel to make several model at onece

``` bash
parallel -a list -j 2 --verbose " echo {}
mkdir {}_1
cd {}_1
cp ../{}/{}.ali .
cp ../Crotoxin/3r0l.pdb .
python ../bin/align2d.py -a {}.ali -p 3r0l.pdb -c D
python ../bin/model-single.py -a {}-3r0lD.ali -k 3r0lD -s {} > model-single.log
rm 3r0l.pdb"
```

## CgCrotB

Beta subunit modeled with D chain of the crotoxin pdb corresponding to
the B subunit

## Crotoxin-like Acidic Subunit

#### CgSCrotA

Alfa subunit from the south population without cleavage modeled with D
chain of the crotoxin pdb corresponding to the B subunit

#### CgNCrotA

Alfa subunit from the North population without cleavage modeled with D
chain of the crotoxin pdb corresponding to the B subunit

#### CgSCrotA1

Alfa subunit from the South population with cleavage on sites 1,4,5
modeled with D chain of the crotoxin pdb corresponding to the B subunit

#### CgNCrotA1

Alfa subunit from the North population with cleavage on sites 1,4,5
modeled with D chain of the crotoxin pdb corresponding to the B subunit

#### CgSCrotA2

Alfa subunit from the South population with cleavage on sites 1,4,5 and
2,3 modeled with A,B,D chains of the crotoxin pdb corresponding to the A
subunit

#### CgNCrotA2

Alfa subunit from the South population with cleavage on sites 1,4,5, and
2,3 modeled with A,B,D chains of the crotoxin pdb corresponding to the A
subunit
