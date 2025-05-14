# SIESTA Examples

## Description
This repo contains examples and files useful for tutorials and teaching using SIESTA code, including analysis using python and visualization with VMD.

## Reference Websites
[SIESTA](https://siesta-project.org/siesta/) is both a method and its computer program implementation, to perform efficient electronic structure calculations and ab initio molecular dynamics simulations of molecules and solids.

The python codes require to import standard numpy and matplotlib and also the python library [SISL](https://sisl.readthedocs.io/en/latest/index.html) for electronic structure calculations

The visualization program VMD can be found [here](https://www.ks.uiuc.edu/Research/vmd/)

## Manuals and Tutorials

SIESTA 5.2.2 [Manual](https://gitlab.com/siesta-project/siesta/-/releases/5.2.2/downloads/siesta-5.2.2.pdf)

For offical SIESTA tutorials check out here:
https://sisl.readthedocs.io/en/latest/tutorials.html#siesta-transiesta-support
https://docs.siesta-project.org/projects/siesta/en/latest/tutorials/index.html

Note:
Here the input structures are provided in fdf format (native format for SIESTA) and xyz.
The conversion between both formats can be done easily using the sgeom command in sisl as described [here](https://sisl.readthedocs.io/en/latest/scripts/sgeom.html)
