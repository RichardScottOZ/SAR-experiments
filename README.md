# SAR-experiments
Experiments related to things to do with SAR data that might be useful.
Seeing some LLMs go with answers as a starting point - generally for things not boilerplate, not going to do too well.  Even more so with science.
# IMPORTANT
DO NOT assume any of the code here will run - any of it does, will note and put in a ROBOTWORKING folder.
I will put anything I write into the src folder.

## Papers
- Deriving Surface Resistivity from Polarimetric SARData Using Dual-Input UNet : https://arxiv.org/pdf/2207.01811.pdf

## Data
### Sentinel-1
- AWS Stac catalogue https://github.com/awslabs/open-data-registry/blob/main/datasets/sentinel-1-rtc-indigo.yaml
### GSQ Open Data API
- https://github.com/RichardScottOZ/open-data-api
### Magnetotellurics
#### Cloncurry
- https://geoscience.data.qld.gov.au/data/report/cr124399
	- otherwise known as first survey I thought of online


## Processing
- https://github.com/RichardScottOZ/openSAR
- https://github.com/Narayana-Rao/PolSAR-tools [QGIS plugin mentioned in paper]
	- https://step.esa.int/main/toolboxes/polsarpro-v6-0-biomass-edition-toolbox/
- https://github.com/Narayana-Rao/polsartools	

## Experiments
### ChatGPT
- Can ChatGPT 3.5 lift an architecture out of a paper
	- likely yes
	- get it right, very little chance
	- 5 tries to correct an error to get an actual 'model'
		- Not a correct model, but a model that doesn't have actual errors
		
	
### Phind 34
- Produces a different code version
	- Same result of course
	- Gets stuck in a loop trying to fix a different error
	- https://www.phind.com/search?cache=wlvfrv0bddld5xahaeyko2j1
	
### Perplexity
- Perplexity free
#### DI-UNET
- Would expect same things
- Produced a no-error 'model' first try
- https://www.perplexity.ai/search/Please-turn-this-SeRVbVKQTlWMcZQSRCcong
- Most robots can do things like turn text into tables and perplexity got this first go
#### QLD Open Data API
- Asked for code there - get a generic requests request - as it doesn't actually know the api

		
		
## Features
### Table I: Details of the Polarimetric Parameters/Features Used in This Study

| Short Form | Description                                       |
|------------|---------------------------------------------------|
| σ◦HH       | Backscatter intensity (HH polarization)            |
| σ◦HV       | Backscatter intensity (HV polarization)            |
| σ◦VV       | Backscatter intensity (VV polarization)            |
| λ1, λ2, λ3 | Eigen values                                      |
| H, A, α    | Cloude decomposition parameters                   |
| β, δ, γ    | Polarimetric intercorrelation parameters          |
| mFP        | Barakat degree of polarization                    |
| θFP        | Scattering type parameter based on degree of polarization |
| Ps, Pd, Pv, Pc | Model-free decomposition powers                 |
| purity     | Scattering degree of purity                       |
| depolarization | Depolarization index                             |
| Span       | Total power                                       |
| HI, HP     | Shannon entropy parameters                        |

This table summarizes the various polarimetric parameters and features used in the study, providing a quick reference for their short form descriptions and corresponding details.
		

## DataLoader
- When asked about a dataloader, perplexity gave it a shot
	- Basically makes sense at a simple level		