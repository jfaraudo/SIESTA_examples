# Geometry optimization
## fdf Scripts
Example fdf files suitable for geometry optimization (energy minimization) of molecules and crystals:
- **geometry optimization of an isolated molecule**: *optimization.fdf* . The script assumes that simulation box is fixed and it contains enough space around the molecule to avoid periodic image interactions.
- **structure relaxation (variable cell) of a crystal**: *relaxation.fdf* . The script modifies the simulation box during the simulation to relaxe the system to (eventually) zero pressure and zero stress.

In both cases the script expects a structure.fdf file with the coordinates.
Initial structures can be build with software such VMD or Avogadro, saved in xyz and later on transformed to fdf format using [sgeom](https://sisl.readthedocs.io/en/latest/scripts/sgeom.html) or in python using sisl library.

## Pseudopotentials
Pseudopotentials for SIESTA v5 in psml format can be downloaded from [pseudo-dojo](https://www.pseudo-dojo.org/)

## Further Information

More information about geometry optimization in SIESTA from the official tutorials is available [here](https://docs.siesta-project.org/projects/siesta/en/latest/tutorials/basic/structure-optimization/).

More information about optimizing aspects of SIESTA calculations (basis set, level of theory,...) from the official tutorials is available [here](https://docs.siesta-project.org/projects/siesta/en/stable/tutorials/basic/first-encounter-theorylevel/index.html#tutorial-basic-first-encounter-theorylevel)

A good presentation about the concepts involved can be found [here](https://siesta.icmab.es/siesta/events/SIESTA_School-2024/Geometry_Optimization+MD-2024.pdf).
