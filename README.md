
<p align="center">
  <img src="./img/swot-omip-logo.png" width="150">
</p>

# SWOT Ocean Model Intercomparison Project

This repository is the entry point for a collaborative project aiming at assessing the representation of ocean mesoscales in ocean models using SWOT altimeter data.

## What this repository provides

This repository serves three purposes:

1. **A collaboration protocol** — A structured framework for the community to contribute ocean model outputs and jointly assess seas surface height variability using SWOT altimeter data. The protocol covers terms of use, data requirements, and contribution workflows coordinated openly through GitHub.

2. **A workflow for generating and sharing pseudo-SWOT data** — Step-by-step instructions for interpolating ocean model outputs onto the SWOT satellite grid using [Synthocean](https://github.com/Amine-ouhechou/synthocean), and for submitting the resulting pseudo-SWOT datasets via a standardised format and metadata schema.

3. **Analysis codes and metrics** — Ready-to-use notebooks and scripts for computing wavenumber spectra and other diagnostics from both SWOT observations and simulated pseudo-SWOT data (see [`Analysis/`](./Analysis/)).

## Science objective

We propose a model intercomparison project to:
* Describe the seasonal variability of SSH variance over the global ocean from SWOT altimeter.
* Evaluate the performance of a variety of numerical ocean models in capturing this variability.
* Better understand the main mechanisms driving the space and time variability of ocean dynamics.

## Motivation

Mesoscale ocean dynamics (O(100 km) and O(10–100 days)) play an important role in ocean circulation, air-sea interactions, global tracer transport and climate. In situ observations, satellite altimetry and ocean numerical models show significant spatial and seasonal variability at this scale.

Despite significant progress over the last decade, it is still unclear whether the simulations adequately reproduce mesoscale variability, as well as the main mechanisms controlling spatial and temporal variability. The Surface Water and Ocean Topography (SWOT) altimeter mission offers an unprecedented opportunity to document (sub)mesoscale variability and assess the ability of models to capture it.


## Data pipeline

The overall data flow is:

```
Ocean model output  →  Synthocean interpolation  →  Pseudo-SWOT dataset  →  Spectral metrics
       ↑                      on SWOT grid               ↑                      ↑
  (contributor)         (processing instructions)      (S3 storage)    (Analysis notebooks)
```

1. **Contributors** run their ocean model and prepare the outputs.
2. Model outputs are **interpolated onto the SWOT grid** using [Synthocean](https://github.com/Amine-ouhechou/synthocean) (see [processing instructions](./processing-instructions.md)).
3. The resulting **pseudo-SWOT datasets** are shared via an S3 endpoint, with metadata submitted through GitHub (see [submission instructions](./submission-instructions.md)).
4. The **analysis codes** compute wavenumber spectra and other metrics from both the real SWOT and pseudo-SWOT data (see [`Analysis/`](./Analysis/)).

## Repository structure

| Path | Description |
|------|-------------|
| [`Agreements.rst`](./Agreements.rst) | Terms and conditions for contributors |
| [`ocean-model-requirements.md`](./ocean-model-requirements.md) | Minimum requirements for simulations |
| [`processing-instructions.md`](./processing-instructions.md) | How to interpolate model data onto the SWOT grid |
| [`submission-instructions.md`](./submission-instructions.md) | How to submit your dataset and metadata |
| [`Dataset_template/`](./Dataset_template/) | Metadata YAML template and filled example for new contributions |
| [`Analysis/`](./Analysis/) | Notebooks and scripts for computing wavenumber spectra and diagnostics |
| [`status_contribution.md`](./status_contribution.md) | Current status of all contributions |

## How this works

Interested research groups are invited to provide ocean model data following our data request.

Our group at IGE (Grenoble, France) and CNES (Toulouse, France) will lead the analysis and share the results. All the communications will be orchestrated openly through GitHub. The end result of this effort will be a collective paper involving all contributors.

## How to contribute

If you are interested, please follow these steps:
1. Check the [Terms and conditions of the agreements](./Agreements.rst).
2. Verify that your simulations meet the [requirements](./ocean-model-requirements.md).
3. Raise a GitHub [issue](https://github.com/meom-group/swot-ocean-model-intercomparison-project/issues/new/choose) to let us know that you are interested.
4. Prepare your data following these [processing instructions](./processing-instructions.md).
5. Prepare one metadata file for each dataset you would like to submit (following this [template](./Dataset_template/metadata_template.yaml)).
6. Submit your dataset(s) following these [submission instructions](./submission-instructions.md).

## Contribution status

[Here](./status_contribution.md) you will find information about the status of your contribution.

## Analysis code

The analysis code in [`Analysis/`](./Analysis/) provides:
- **Wavenumber spectral computation** — Notebooks for computing along-track SSH wavenumber spectra from SWOT and pseudo-SWOT data (e.g., [`Example_of_Wavenumber_Spectra_Computation.ipynb`](./Analysis/Example_of_Wavenumber_Spectra_Computation.ipynb)).
- **Regional analysis** — Tools for defining ocean regions and computing regional diagnostics (e.g., [`Region_definition.ipynb`](./Analysis/Region_definition.ipynb)).
- **Global-scale analysis** — Scripts and notebooks for computing and plotting spectra across global boxes (see [`Analysis/GLOBAL/`](./Analysis/GLOBAL/)).

## Contact

Questions, comments, or suggestions should be submitted by opening a [new issue](https://github.com/meom-group/swot-ocean-model-intercomparison-project/issues).

## Organizers

Marcela Contreras, Micael Aguedjou, Amine Ouhechou, Julien Le Sommer, Takaya Uchida

## Licence

CC-BY
