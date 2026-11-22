from pyteomics import achrom

import matplotlib.pyplot as plt



def predict_lc_retention_times(peptides):
    """maps each peptide in a list of peptide sequences and maps it relatively to its predicted retention time.
    Add a short description here.

    Parameters
    ----------
    peptides : list
        list of peptide sequences 

    Returns
    -------
    retention_times : dict
        dictionary mapping all peptides from the list to their predicted retention times
    """

    retention_times = {}

    for peptide in peptides:
        retention_times[peptide] = round(achrom.calculate_RT(peptide, achrom.RCs_guo_ph7_0), 2)

    return retention_times



def plot_retention_time(retention_times, resolution=30):
    """creates a histogram of predicted retention times for a given list or values of a dictionary of proteins
    Add a short description here.

    Parameters
    ----------
    retention_times : dict / list
        dictionary or list containing predicted retention times of peptides
    resolution : int
        number of bins set for the histogram

    Returns
    -------
    histogram : figure to display the distributioin of predicted retention times
    """
    plt.hist(retention_times, bins=resolution)
    plt.xlabel('Predicted REtentinon Times')
    plt.ylabel('Frequency')

    plt.show()


def select_retention_time_window(peptide_rt_map, lower_ret_time, upper_ret_time):
    """sorts/filters out peptides that fall outside a window of given times
        Add a short description here.

    Parameters
        ----------
        peptide-rt_map : dict
            dictionary containing peptides and their predicted retention times
        lower_ret_time : float
            lower limit for the retention time window
        upper_ret_time : float
            upper limit for the retention time window
        Returns
        -------
        filtered_rt_peptides : dict
            dictionary containing remaining peptides and their retention times

    """
    filtered_rt_peptides = {}

    for peptide, rt in peptide_rt_map.items():
        if lower_ret_time <= rt <= upper_ret_time:
            filtered_rt_peptides[peptide] = rt

    return filtered_rt_peptides