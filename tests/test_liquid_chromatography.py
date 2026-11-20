from pyteomics import achrom
import matplotlib.pyplot as plt

from Mayasim.liquid_chromatography import (
    predict_lc_retention_times,
    plot_retention_time,
    select_retention_time_window
)

def test_predict_lc_retention_times():
    peptides = [
        'ACDEFGHIK',
        'LMNPQRSTVWY',
        'ACDEFGHIKLMNPQRSTVWY'
]
    expected = {
        'ACDEFGHIK': round(achrom.calculate_RT('ACDEFGHIK', achrom.RCs_guo_ph7_0), 2),
        'LMNPQRSTVWY': round(achrom.calculate_RT('LMNPQRSTVWY', achrom.RCs_guo_ph7_0), 2),
        'ACDEFGHIKLMNPQRSTVWY': round(achrom.calculate_RT('ACDEFGHIKLMNPQRSTVWY', achrom.RCs_guo_ph7_0), 2)
    } 

    actual = predict_lc_retention_times(peptides)
    assert actual == expected

    print(actual)
    print(expected)



def test_select_retention_time_window():
    peptide_rt_map = {
        'ACDEFGHIK' : 2,
        'LMNPQRSTVWY' : 15,
        'ACDEFGHIKLMNPQRSTVWY' : 25
}
    dummy_rt_map = {'ACDEFGHIK' : 2, 'LMNPQRSTVWY' : 15}
    selected = select_retention_time_window(peptide_rt_map, lower_ret_time=0, upper_ret_time=20)

    assert selected == dummy_rt_map



  