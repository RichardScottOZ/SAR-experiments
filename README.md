# SAR-experiments
Experiments related to things to do with SAR data that might be useful.

## Processing
- https://github.com/RichardScottOZ/openSAR

## Papers
- Deriving Surface Resistivity from Polarimetric SARData Using Dual-Input UNet : https://arxiv.org/pdf/2207.01811.pdf

## Experiments
- Can ChatGPT 3.5 lift an architecture out of a paper
	- likely yes
	- get it right, very little chance
	- 5 tries to correct an error to get an actual 'model'
		- Not a correct model, but a model that doesn't have actual errors
		
		
- Phind 34
- Produces a different code version
	- Same result of course
	- Gets stuck in a loop trying to fix a different error
	- https://www.phind.com/search?cache=wlvfrv0bddld5xahaeyko2j1
	
- Perplexity free
		- Would expect same things
		- Produced a no-error 'model' first try
		- https://www.perplexity.ai/search/Please-turn-this-SeRVbVKQTlWMcZQSRCcong
		
		
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