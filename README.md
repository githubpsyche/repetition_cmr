# repetition_cmr
> a closer look at the retrieved context account of repetition and spacing effects in free recall

Retrieved-context theory (RCT) accounts for free recall of item lists by asserting that 1) studied items are associated with a gradually changing, recency-weighted representation of temporal context, 2) the contexts retrieved from studying (or recalling) items update the current state of context, and 3) the current state of context is the proximate cue for each item recall. 
These mechanisms help account for many repetition effects in free recall, including the mnemonic advantage of spaced over massed item repetition and tendencies to successively recall items that follow a shared repeated item [@lohnas2014retrieved]. 
Here, though, we present evidence that this account has significant deficiencies. 

To re-evaluate RCT, we analyzed two datasets previously collected to study repetition effects in free recall [@lohnas2014retrieved; @kahana2005spacing]. 
We applied likelihood-based fitting [@morton2016predictive] to a computational model embodying RCT, the context maintenance and retrieval model [CMR; @polyn2009context]. 
Across datasets, the model underpredicted the mnemonic benefit of spaced over massed repetition. 
It also poorly generalized between task conditions that included or excluded item repetitions in study lists [@busemeyer2000model].

We additionally report a novel analysis identifying a deficient repetition contiguity effect after participants recalled an item repeatedly presented in a list. 
Participants transitioned more often to neighbors of the item's initial, rather than successive, presentation(s).
The model cannot account for this pattern, even after adding mechanisms to either reduce learning for items' successive presentations or enhance memory for neighbors of items' initial presentations. 
Contrary to previous reports, these results suggest repetition effects may present a significant challenge for retrieved-context theory.