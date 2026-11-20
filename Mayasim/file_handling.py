def read_fasta(filepath : str) -> dict:
    """reads fasta file and returns proteins as as a dictionary

    Parameters
    ---------
    filepath : str
        Path to the FASTA file.
    Returns
    ---------
    dict
        A dictionary mapping protein IDs to their corresponding amino acid sequences.
    """
    fasta_path = filepath #find document

    protein_map = {}  #empty data frame 
    current_id = None
    current_sequence = [] #empty list

    with open(fasta_path, 'r') as fasta_handle:
        for line in fasta_handle:
            stripped = line.strip()   #.strip() removes whitespaces before and after from a string
            if not stripped:
                continue
            if stripped.startswith('>'):  #check if the line starts with our hint at new protein
                if current_id is not None: #if the> is there
                    protein_map[current_id] = ''.join(current_sequence) 
                    current_sequence = []
                current_id = stripped.split('|')[1] #splits the line at the character |
            else:
                current_sequence.append(stripped) #if the line does not start with > it is added to the current sequence

    if current_id is not None:
        protein_map[current_id] = ''.join(current_sequence) #adds the id

    return protein_map
