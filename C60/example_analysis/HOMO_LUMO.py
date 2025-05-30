# Code Based on the SISL - SIESTA tutorial
# Create a cube file for HOMO and LUMO to allow visualtization in VMD and other programs
# https://sisl.readthedocs.io/en/latest/tutorials/tutorial_siesta_1.html
# It assumes that you did first the calculation reported in the tutorial
# 

import numpy as np
from sisl import *
import matplotlib.pyplot as plt

#Function integrate
def integrate(g):
    print('Real space integrated wavefunction: {:.4f}'.format((np.absolute(g.grid) ** 2).sum() * g.dvolume))

# -----------------------------
# MAIN CODE
# -----------------------------
# Read Data 

#Read fdf file (input file of SIESTA calculation)
fdf = get_sile('RUN.fdf')
#Read hamiltonian obtained in SIESTA calculation
H = fdf.read_hamiltonian()
molecule = H.geometry

#Show results
print("Hamiltonian:")
print(H)

#Eigenstates (NOT ordered)
es = H.eigenstate()

# We specify an origin to center the molecule in the grid
molecule.lattice.origin = [-7, -7, -7]

# Reduce the contained eigenstates to only the HOMO and LUMO
# Find the index of the smallest positive eigenvalue
idx_lumo = (es.eig > 0).nonzero()[0][0]
es = es.sub([idx_lumo - 1, idx_lumo])

# Ordered eigenstates (show only HOMO LUMO)
print("Ordered Eigenstates")
#print(es)

print("Energies")
print(es.eig)

#Create a grid to project the density
g = Grid(0.2, lattice=molecule.lattice)

#HOMO
es.sub(0).wavefunction(g)
integrate(g)
g.write('HOMO.cube')

g.fill(0) # reset the grid values to 0

#LUMO
es.sub(1).wavefunction(g)
integrate(g)
g.write('LUMO.cube')
