# lauzhack19

## Importing the conda environment

If the environment isn't created yet, run:

`conda env create -f environment.yml -n lauzhack`

To activate the created environment, run:

`conda activate lauzhack`

To update the already created environment, run with the environment activated:

`conda env update --file environment.yml`

To create a new env file if you added packages, run:

`conda env export --name lauzhack > environment.yml`
