# MAGEnTa

## Installation instructions
 Install necessary software and python packages
### Recommended : New conda environment
python version: 3.7

### Python Packages
os (pre-set)
sys (pre-set)

### Software Installation
metaSPAdes : Follow metaspades instructions outlined here: https://ablab.github.io/spades/installation.html#downloading-sp$
The SPAdes library should be automatically added to your PATH after you compile.
Bowtie2 : install bowtie2 using instruction here (Conda method suggested): https://www.metagenomics.wiki/tools/bowtie2/ins$
add here: check if these softwares are available/installed


## Usage and Tutorial
### MAGs Database Build
Produces MAGs databases per donor and pre sample file.
```
./src/build_mag_db.sh -i INPUT_DIR -m MAPPING_FILE -o OUTPUT_DIR -t THREADS
```

### Alignment and Engraftment Estimation
Produces counts table and engrafted mags lists.
```
./src/align_source.sh -i INPUT_DIR -m MAPPING_FILE -o OUTPUT_DIR -t THREADS -s ALIGN_SCORE
```
note that "ALIGN_SCORE" can only be one of 3 choices for alignment score in the current implementation: 1.00, 0.99, 0.98
