from Mayasim.file_handling import read_fasta

def test_fasta_reader():
    tmp_fasta_path = 'tests/data/dummy-proteins.fasta'
    protein_map = read_fasta(tmp_fasta_path)
    
    # Replace the strings with your fasta content
    # which you expect to be now available as a dictionary
    assert protein_map["proteinid1"] == "HELLO"
    assert protein_map["proteinid2"] == "BYE"
