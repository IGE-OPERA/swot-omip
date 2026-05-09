from concurrent.futures import ProcessPoolExecutor, as_completed
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt


def plot_psd(ax, freqs, psds, unit, psd_labels, title=None,legend=True,loc_leg="best",bba_leg=(1,1), xtick_show=True, ytick_show=True, xlabel_upper=True,xlabel_lower=True, ylabel=True, savefig=False, filename=None,plot_transparent=False, colors=None, max_horizontal_gridsize=None, wavelength_ticks = np.array([5, 10, 25, 50, 100, 1000])):
    """
    Plots the Power Spectral Density (PSD) on a logarithmic scale.
    
    The function plots the PSD on the given axes, `ax`. The plot is on a logarithmic scale 
    for both x and y axes. The function can handle one or two PSD arrays. If provided, 
    it adds labels and a title to the plot. It also includes reference lines for $k^{-2}$ 
    and $k^{-5}$ slopes.

    The function adds grid lines, legends, and adjusts axis labels and ticks for better readability.

    If `freqs` or `psd1` are empty, the function prints an error message and returns 
    without plotting.
    
    Parameters
    ------------
    ax: matplotlib.axes.Axes
        The axes on which to plot the PSD. 
    freqs: np.ndarray
        A numpy array containing frequency values.
    psds: [np.ndarray, ...] | np.ndarray
        A list of numpy array or a single numpy array of PSD values corresponding to `freqs`.
    unit: str
        Unit of the physical quantity for which the PSD was computed.
    psd_labels: [str, ...] | str, optional
        A list of labels or a single label for the PDS array(s).
    title: str, optional
        Title of the plot.
    savefig: bool 
        True to save the figure, False otherwise
    filename: str or None
        Name of the file to save the figure, default is 'figure.png'
    plot_transparent: bool
        True to display the figure with a transparent background, False otherwise
    """
    if isinstance(psds, np.ndarray):
        psds = [psds]
        psd_labels = [psd_labels]
    if psd_labels is None:
        psd_labels = [None] * len(psds)

    n_psds = psds.shape[0] if isinstance(psds, np.ndarray) else len(psds)
        # Normalize colors
    if colors is None:
        colors = [None] * n_psds
    elif isinstance(colors, str):
        colors = [colors] * n_psds
    elif len(colors) != n_psds:
        raise ValueError("Length of 'colors' must match number of PSDs")


    # Validate grid size list
    if max_horizontal_gridsize is not None and len(max_horizontal_gridsize) != len(psds):
        raise ValueError("Length of 'max_horizontal_gridsize' must match number of PSDs")

    # --- Plot PSDs ---
    for i, (psd, label, color) in enumerate(zip(psds, psd_labels, colors)):
        psd = np.array(psd)
        if max_horizontal_gridsize is not None:
            mask = (1 / freqs) >= (2 * max_horizontal_gridsize[i])
            freqs_to_plot = freqs[mask]       
            psd_to_plot = psd[mask]
        else:
            freqs_to_plot = freqs
            psd_to_plot = psd

            # --- for SWOT as reference---
        if i == len(psds) - 1:
            ax.loglog(freqs_to_plot, psd_to_plot, label=label, color='black',
                      linewidth=2, zorder=5)  # plus épais et noir
        else:
            ax.loglog(freqs_to_plot, psd_to_plot, label=label, color=color,
                      linewidth=1.2, alpha=0.9)

    ax.set_ylim(1e-7, 1e2)
    if ylabel==True:
        ax.set_ylabel(f"PSD [${unit}/(cy/km)$]", fontsize=8, fontweight="bold", color="black")

    ax.xaxis.set_label_position("top")
    ax.xaxis.tick_top()
    if xlabel_lower==True:
        ax.set_xlabel("Wavenumber [$cy/km$]", fontsize=8, fontweight="bold", color="black")

    # filters out zero frequencies
    non_zero_freqs = freqs[freqs != 0]

    # k^-2 & k^-5
    k_2 = non_zero_freqs ** -2 * (psds[0][0] / (non_zero_freqs[0] ** -2))  # Scale according to the first PSD value
    k_5 = non_zero_freqs ** -5 * (psds[0][0] / (non_zero_freqs[0] ** -5))

    ax.loglog(non_zero_freqs, k_2*30, "k--", label="$k^{-2}$")  # 30 to fix the line
    ax.loglog(non_zero_freqs, k_5*1e6, "b--", label="$k^{-5}$")  # 1e6 to fix the line

    ax2 = ax.secondary_xaxis("bottom", functions=(lambda x: 1 / x, lambda x: 1 / x))
    if xlabel_upper==True:
        ax2.set_xlabel("Wave-length [$km$]", fontsize=8, fontweight="bold", color="black")

   #wavelength_ticks = np.array([5, 10, 25, 50, 100, 200, 500, 1000])
    ax2.set_xticks(wavelength_ticks)
    ax2.set_xticklabels(wavelength_ticks, fontsize=8)
    ax.grid(True, which="both")
    if legend==True:
        ax.legend(loc=loc_leg, bbox_to_anchor=bba_leg)

    # Set the title if provided
    if title:
        ax.set_title(title, fontsize=15, fontweight="bold", color="black")

    if xtick_show==False:
        ax.set_xticks([])
        ax2.set_xticks([])

    if ytick_show==False:
        ax.set_yticks([])
    
    # Handle saving the figure if savefig is True
    if savefig:
        if filename is None:
            # Use default filename if none is provided
            filename = "figure.png"
        if plot_transparent:
            plt.savefig(filename,dpi=300,transparent=plot_transparent)
        else:
            plt.savefig(filename,dpi=300)