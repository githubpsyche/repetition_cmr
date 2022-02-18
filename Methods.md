## Methods
How are we evaluating retrieved context theory here? We'll present datasets, model, and the new-ish evaluation/fitting technique. We may rename this section ("Evaluating RCT at the Level of the Recall Sequence") and/or blend it with the next to emphasize what's new about our approach additionally use it to review benchmark phenomena in context of our technique, similarly to how Lynn does in her 2014 paper. Won't introduce the deficient repetition contiguity effect just yet.

### Datasets

#### Lohnas2014

#### HowaKaha2005

### Sequence-Based Model Evaluation and Fitting
<!--c/ped from icmr; must revise for this paper-->
To evaluate how effectively each model accounts for the responses in our datasets, we applied a likelihood-based model comparison technique introduced by @kragel2015neural that assesses model variants based on how accurately they can predict the specific sequence in which items are recalled. According to this method, repeated items and intrusions (responses naming items not presented in the list) are included from participants' recall sequences. Given an arbitrary parameter configuration and sequences of recalls to predict, a model simulates encoding of each item presented in the corresponding study list in its respective order. Then, beginning with the first item the participant recalled in the trial, the probability assigned by the model to the recall event is recorded. Next, the model simulates retrieval of that item, and given its updated state is used to similarly predict the next event in the recall sequence - either retrieval of another item, or termination of recall - and so on until retrieval terminates. The probability that the model assigns to each event in the recall sequence conditional on previous trial events are thus all recorded. These recorded probabilities are then log-transformed and summed to obtain the log-likelihood of the entire sequence. Across an entire dataset containing multiple trials, sequence log-likelihoods can be summed to obtain a log-likelihood of the entire dataset given the model and its parameters. Higher log-likelihoods assigned to datasets by a model correspond to better effectiveness accounting for those datasets.

### CMR
Model specification blended with details of how it realizes repetition effects.