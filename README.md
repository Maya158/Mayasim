# Mayasim

## Proteosim knock-off 

### Purpose
This project contains an *in silico* mass spectrometry experiment. It aims to simulate the workflow from protein extraction to spectrum visualisation. 

### Requirements
The requirements and needed packages can be found in the 'requirements.txt' file.
The project requires:   numpy
                        pandas
                        matplotlib
                        pyteomics


### Usage
The python scripts can be used to:  Calculate peptide masses
                                    Calculate m/z values
                                    Generate fragments
                                    Plot simulated mass spectra
                                    Export results to TSV files


### Project Structure

proteosim/
├── data/
├── proteosim/
│   ├── __init__.py
│   ├── file_handling.py
│   ├── protein_digestion.py
│   ├── liquid_chromatography.py
│   └── mass_spectra_simulation.py
├── tests/
│   ├── __init__.py
│   ├── test_file_handling.py
│   ├── test_protein_digestion.py
│   ├── test_liquid_chromatography.py
│   └── test_mass_spectra_simulation.py
└── tutorials/
