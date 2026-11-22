# Mayasim

## Proteosim Knock-off 

### Purpose
Mayasim is an *in silico* mass spectrometry simulation tool designed to replicate the workflow from protein extraction to spectrum visualization. It provides a comprehensive pipeline for protein digestion, peptide mass calculation, liquid chromatography retention time prediction, and mass spectra simulation.

---

### Features
- **Protein Digestion**: Simulate enzymatic digestion of proteins into peptides using customizable cleavage patterns.
- **Peptide Mass Calculation**: Calculate molecular masses and m/z values for peptides.
- **Fragmentation**: Generate peptide fragments for mass spectra analysis.
- **Retention Time Prediction**: Predict liquid chromatography retention times for peptides.
- **Mass Spectra Simulation**: Simulate and visualize mass spectra for peptides.
- **Export Results**: Export results to TSV files for further analysis.

---

### Requirements
The project requires the following Python packages:
- `numpy`
- `pandas`
- `matplotlib`
- `pyteomics`

You can find all dependencies in the `requirements.txt` file.

---

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Mayasim.git
   cd Mayasim

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

3. Install the package in editable mode:
    ```bash
    pip install -e .



### Usage
#### Input:
- Protein sequences in FASTA format.
#### Workflow:
- Protein Digestion:
    Digest proteins into peptides using enzymes like Trypsin, LysC, or ArgC.

- Peptide Mass Calculation:
    Calculate molecular masses and m/z values for peptides.

- Retention Time Prediction:
    Predict liquid chromatography retention times for peptides.

- Mass Spectra Simulation:
    Simulate and visualize mass spectra for peptides.


### Project Structure

Mayasim/
├── data/                           # Example data files (e.g., FASTA files)
├── Mayasim/                        # Source code
│   ├── __init__.py                 # Package initialization
│   ├── file_handling.py            # File I/O utilities
│   ├── protein_digestion.py        # Protein digestion logic
│   ├── liquid_chromatography.py    # Retention time prediction
│   ├── mass_spectra_simulation.py  # Mass spectra simulation
├── tests/                          # Unit tests
│   ├── __init__.py
│   ├── test_file_handling.py
│   ├── test_protein_digestion.py
│   ├── test_liquid_chromatography.py
│   ├── test_mass_spectra_simulation.py
└── tutorials/                      
    └── ms_experiment_final.ipynb   # Example Jupyter notebook

### Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

