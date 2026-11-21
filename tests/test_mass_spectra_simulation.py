from Mayasim.mass_spectra_simulation import (amino_acid_mass_dalton,
                                             calculate_mol_mass,
                                             calculate_mol_mass_collection,
                                             calculate_mz_collection,
                                             fragment_peptide)


def test_calculate_mol_mass():
    aa_mass_dict = amino_acid_mass_dalton
    test_peptide = 'AMINACIDS'
    expected_mass = {'AMINACIDS' : 919.09}
    calculated_mass = calculate_mol_mass(test_peptide, aa_mass_dict)
    print(calculated_mass)
    
    assert calculated_mass == expected_mass


def test_calculate_mol_mass_collection():
    aa_mass_dict = amino_acid_mass_dalton
    peptides = ["AC", "PEPS"]
    expected = {'AC' : 174.23000000000002, 'PEPS' : 410.44}
    actual = calculate_mol_mass_collection(peptides,aa_mass_dict)
    print(actual)

    assert actual == expected

def test_calculate_mz_collection():
    peptide_mass_map = {'pep1' : 1, 'pep2' : 20, 'pep3' : 300}
    actual = calculate_mz_collection(peptide_mass_map, charge=2)
    expected = {'pep1' : 1.51, 'pep2' : 11.01, 'pep3' : 151.01}

    assert actual == expected

def test_fragment_peptide():
    peptide = 'PEP'
    expected = 'P', 'PE', 'EP', 'P'
    actual = fragment_peptide(peptide)

    assert set(actual) == set(expected)
    assert 'PEP' not in expected  # which string should not be in the expected?

