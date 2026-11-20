import re

def digest_protein_sequence(protein_seq, cleave_pattern, min_pep_len=5, max_pep_len=30):
    """digests proteins sequence based on a cleavage pattern and filters out peptides smaller than min_pep_len(default is 5) and peptides larger than max_pep_len(default is 30)
    Add a short description here.

    Parameters
    ----------
    protein_seq : str
        peptide sequence
    cleave_pattern : str
        the recognition sequence 
    min_pep_len : int, optional(default is set to 5)
        minimum lenght of peptide kept
    max_pep_len : int, optional(default is set to 30)
        maximum lenth of peptide kept
    Returns
    -------
    list of peptides resulting from the cleavage but only between the minimum and maximum length
    """

    peptides = re.split(cleave_pattern, protein_seq)

    #print(peptides)
    #print(f'Nr. of digested peptides: {len(peptides)}')


    filtered = []

    for peptide in peptides:
        if len(peptide) < min_pep_len or len(peptide) > max_pep_len:
            continue
        else:
            filtered.append(peptide)


    return filtered


def digest_protein_collection(protein_map, cleave_pattern, min_pep_len=5, max_pep_len=30):
    """takes a dictionary of protein sequences and digests them based on a given cleavage pattern. It also filters peptides based on length, default is set to 5-30
    Add a short description here.

    Parameters
    ----------
    protein_map : dict
        A dictionary containing many protein sequences
    cleave_pattern : str
        recogntiion sequence for protein cleavage
    min_pep_len : int, optional(defualt set to 5)
        minimum length of peptides
    max_pep_len : int, optional(default set to 30)
        maximum length of peptides
    Returns
    -------
    returns a new dictionary containing the peptides after digestion and filtering
    """
    peptide_collection = {}

    for protein_id, protein_seq in protein_map.items():
        peptides = digest_protein_sequence(protein_seq, cleave_pattern, min_pep_len, max_pep_len)
        peptide_collection[protein_id] = peptides

    return peptide_collection



def compute_sequence_coverage(protein_seq, peptides):
    """calculates the coverage of a protein sequence based on the peptides created after digestion and the original protein sequence. 
    Add a short description here.

    Parameters
    ----------
    protein_seq : str
        protein sequence before digestion
    peptides : list
        peptides after digestion
    Returns
    -------
    coverage : float
        sequence coverage calclated by dividing the peptides by the original protein
    """
    
    coverage = 0.0
    sequence_lengthn =len(protein_seq)
    for peptide in peptides:
        if peptide in protein_seq:
            coverage = coverage + ((len(peptide) / sequence_lengthn) * 100)
        else:
            continue
    return coverage


enzyme_cleavage_patterns = {
    'LysC': r'(?<=K)',
    'LysN': r'(?=K)',
    'ArgC': r'(?<=R)',
    'Trypsin': r'(?<=[KR])(?!P)',
}
