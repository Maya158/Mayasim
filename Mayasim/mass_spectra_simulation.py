import numpy as np
import matplotlib.pyplot as plt

amino_acid_mass_dalton = {
    'A': 71.08, 'R': 156.19, 'N': 114.10, 'D': 115.09,
    'C': 103.15, 'E': 129.12, 'Q': 128.13, 'G': 57.05,
    'H': 137.14, 'I': 113.16, 'L': 113.16, 'K': 128.17,
    'M': 131.19, 'F': 147.18, 'P': 97.12, 'S': 87.08,
    'T': 101.11, 'W': 186.21, 'Y': 163.18, 'V': 99.13,
}

def calculate_mol_mass(peptide_seq, amino_acid_mass_dict):
    """takes peptide sequence and amino acid mass dictionary  to return a dictionary giving the neutral molecular mass of the peptide
    Add a short description here.

    Parameters
    ----------
    peptide_seq : str
        peptide sequence of amino acids
    amino_acid_mass_dict : dict
        dictionary of amino acids and their masses

    Returns
    -------
    peptide_mass : dict
        dictionary containinng the peptide sequence and its mass

    """
    peptide_mass = {}

    for aa in peptide_seq:
        if aa in amino_acid_mass_dict:
            mass = sum(amino_acid_mass_dict[aa] for aa in peptide_seq)
            peptide_mass[peptide_seq] = mass
        else:
            print(f'amino acid not found in dictionary')

    return peptide_mass


def calculate_mol_mass_collection(peptides, amino_acid_mass_dict):
    """gives a dictionary of peptides and their corresponding neutral mass after recieving the peptides and the mass of amino acids
    Add a short description here.
    
    Parameters
    ----------
    peptides : list
        list of peptides to be weighed
    amino_acid_mass_dict : dict
        dictionary containing the amino acids and their corresponding molecular weight
    
    Returns
    -------
    mol_mass_collection : dict
        dictionary containing peptides and thei neutral molecular weight

    """
    mol_mass_collection = {}

    for pep in peptides: 
        for pep in peptides:
            mol_mass_collection.update(calculate_mol_mass(pep, amino_acid_mass_dict))

    return mol_mass_collection


def calculate_mz_collection(peptide_mass_map, charge, proton_mass=1.007):
    """yields a dictionary of m/z values for given proteins
    Add a short description here.

    Parameters
    ----------
    peptide_mass_map : dictionary
        contains proteins and their neutral masses
    charge : float
        charge given by the caller explicitly
    proton_mass : float
        mass of a proton set to a default of 1.007

    Returns
    -------
    mz_collection : dict
        dictionary containing peptides and their m/z values

    """
    mz_collection = {}
    
    for peptide, mass in peptide_mass_map.items():
        mz_collection[peptide] = round((mass + charge * proton_mass) / charge, 2)

    return mz_collection



def plot_spectrum(mz_values, random_count_range=(0, 30000), seed=42):
    """draws random intensities and plots a bar chart of m/z values
    Add a short description here.

    Parameters
    ----------
    mz_values : dict
        dictionary containing proteins and their m/z values
    random_count_range : tuple, optional
        Minimum and maximum intensity values used to generate random counts, by default (0, 30000).
    seed : int, optional
        Random seed for reproducible results, by default 42.

    Returns
    -------
    Plot
        Displays a bar plot of the simulated mass spectrum.
    """
    np.random.seed(seed)

    mz = list(mz_values.values())

    intensities = np.random.randint(
        random_count_range[0],
        random_count_range[1] + 1,
        size=len(mz)
    )

    plt.figure()
    plt.bar(mz, intensities)
    plt.xlabel("m/z")
    plt.ylabel("Intensity")
    plt.title("Simulated Mass Spectrum")
    
    plt.show()



def fragment_peptide(peptide):
    """returns the combined list of b- and y-ion sequences for peptides
    Add a short description here.

    Parameters
    ----------
    peptide : str
        peptide sequence to be turned into the b- and y-ion sequences

    Returns
    -------
    fragmented : list
        list containing both the b- and y-ion sequences for the peptide input

    """
    fragmented = []

    b_ion = []
    y_ion = []


    for aa in range(1, len(peptide)):
        b_ion.append(peptide[:aa])
    for aa in range(1, len(peptide)):
        y_ion.append(peptide[aa:])

    fragmented = b_ion + y_ion

    return fragmented


