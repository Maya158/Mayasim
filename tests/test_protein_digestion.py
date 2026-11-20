from Mayasim.protein_digestion import digest_protein_sequence
from Mayasim.protein_digestion import digest_protein_collection
from Mayasim.protein_digestion import compute_sequence_coverage

def test_digest_protein_sequence():
    dummy_seq_1 = 'BINGO'
    cleave_pattern_1 = r'(?=O)'
    dummy_seq_2 = 'BONGO'
    cleave_pattern_2 = r'(?=O)'
    dummy_seq_3 = 'BINGOBONGOBINGOBONGO'
    cleave_pattern_3 = r'(?<=O)(?!N)'
    
    peptides_1 = digest_protein_sequence(dummy_seq_1, cleave_pattern_1, min_pep_len=2)
    peptides_2 = digest_protein_sequence(dummy_seq_2, cleave_pattern_2, min_pep_len=2)
    peptides_3 = digest_protein_sequence(dummy_seq_3, cleave_pattern_3, min_pep_len=2)

    assert peptides_1 == ['BING']
    assert peptides_2 == ['ONG']
    assert peptides_3 == ['BINGO', 'BONGO', 'BINGO', 'BONGO']



def test_digest_protein_collection():
    dummy_proteins = {
        "PROTEIN_1": "BINGOBONGO",
        "PROTEIN_2": "HELLOHELLO",
        "PROTEIN_3": "BINGOBINGOBONGO",
        "PROTEIN_4": "THISISALONGERPROTEINSEQUENCEWITHMULTIPLECLEAVAGES",
        "PROTEIN_5": "SHORT",
    }

    cleave_pattern = r'(?<=O)(?!N)'

    digested_proteins = digest_protein_collection(dummy_proteins, cleave_pattern, min_pep_len=1)
    print(digested_proteins)
    print(len('TEINSEQUENCEWITHMULTIPLECLEAVAGES'))

    assert digested_proteins == {'PROTEIN_1': ['BINGO', 'BONGO'],
                         'PROTEIN_2': ['HELLO', 'HELLO'], 
                         'PROTEIN_3': ['BINGO', 'BINGO', 'BONGO'], 
                         'PROTEIN_4': ['THISISALONGERPRO'], 
                         'PROTEIN_5': ['SHO', 'RT']
    }


def test_compute_sequence_coverage():
    dummy_prot_seq = "THISISALONGERPROTEINSEQUENCEWITHMULTIPLECLEAVAGES"
    dummy_peps = ['THISISAL', 'ONGERPR', 'OTEINSEQUENCEWITHMULTIPLECLEAVAGES']

    coverage_dummy = compute_sequence_coverage(dummy_prot_seq, dummy_peps)
    print(coverage_dummy)
    assert coverage_dummy == 100
