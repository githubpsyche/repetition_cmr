# AUTOGENERATED! DO NOT EDIT! File to edit: notebooks/model_evaluation/helpers.ipynb (unless otherwise specified).

__all__ = ['repetition_connectivity_by_lag', 'latent_mfc_mcf_mff', 'mixed_connectivity_by_lag']

# Cell
import numpy as np


def repetition_connectivity_by_lag(item_connections, presentation, minimum_lag=6, max_repeats=2):

    item_count = np.max(presentation)+1
    lag_range = len(presentation) - 1
    total_connectivity = np.zeros((max_repeats, lag_range * 2 + 1))
    total_possible_lags = np.zeros((max_repeats, lag_range * 2 + 1))
    item_positions = np.arange(len(presentation), dtype=int)

    for item in range(item_count):

        # only consider items that are repeated
        current_positions = np.nonzero(presentation == item)[0]
        if len(current_positions) < max_repeats:
            continue

        # only consider items with repeats of lag >= minimum_lag
        assert(current_positions[1] > current_positions[0])
        if current_positions[1] - current_positions[0] < minimum_lag:
            continue

        # we consider each study position of repeated items separately
        for position_index in range(max_repeats):

            # lag of each item from current item is item_positions - current_position,
            # and will always be in range [-lag_range, lag_range] so we keep position by adding lag_range
            item_lags = item_positions - current_positions[position_index] + lag_range
            total_connectivity[position_index, item_lags] += item_connections[item, presentation]
            total_possible_lags[position_index, item_lags] += 1

    # divide by possible lags to get average connectivity
    total_possible_lags[total_connectivity == 0] += 1
    connectivity = total_connectivity / total_possible_lags
    return connectivity

# Cell

from numpy.linalg import norm

def latent_mfc_mcf_mff(model, items=None, postprocessing=True):

    #TODO: Make sure variable item representations explored in TR-CMR are being handled right!

    if items is None:
        items = model.items

    # start by finding latent mfc: the contextual representation cued when each orthogonal $f_i$ is cued
    latent_mfc = np.zeros((model.item_count, len(model.context)))
    for i in range(model.item_count):
        latent_mfc[i] = model.echo(items[i])[len(model.context):]
        if postprocessing:
            latent_mfc[i] /= norm(latent_mfc[i])

    # then latent mcf: the item feature representation cued when each orthogonal $c_i$ is cued
    # no extra normalization is applied after echo retrieval in the model, but results are subsetted differently
    latent_mcf = np.zeros((model.item_count, model.item_count))
    context_units = np.hstack(
        (np.zeros((model.item_count, len(model.context))),
         np.eye(model.item_count, len(model.context), 1))
         )
    for i in range(model.item_count):
        latent_mcf[i] = model.echo(context_units[i])[1:model.item_count+1]
        if postprocessing:
            latent_mcf[i] = np.power(latent_mcf[i], model.choice_sensitivity)
            latent_mcf[i] /= np.sum(latent_mcf[i])

    # then latent mff: the item feature representation cued as a result of reinstating each orthogonal $f_i$
    # TODO: add version for CMR
    latent_mff = np.zeros((model.item_count, model.item_count))
    context_units = np.hstack(
        (np.zeros((model.item_count, len(model.context))),
         latent_mfc)
         )
    for i in range(model.item_count):
        if not postprocessing:
            context_units[i, len(model.context):] /= norm(context_units[i, len(model.context):])

        latent_mff[i] = model.echo(context_units[i])[1:model.item_count+1]
        if postprocessing:
            latent_mff[i] = np.power(latent_mff[i], model.choice_sensitivity)
            latent_mff[i] /= np.sum(latent_mff[i])

    return latent_mfc, latent_mcf, latent_mff

# Cell

def mixed_connectivity_by_lag(item_connections, presentation):
    item_count = np.max(presentation)+1
    lag_range = len(presentation) - 1
    total_connectivity = np.zeros(lag_range * 2 + 1)
    total_possible_lags = np.zeros(lag_range * 2 + 1)
    item_positions = np.arange(len(presentation), dtype=int)

    for item in range(item_count):

        # only consider items that are repeated
        current_positions = np.nonzero(presentation == item)[0]

        # we consider each study position of repeated items separately
        for position_index in range(len(current_positions)):

            # lag of each item from current item is item_positions - current_position,
            # and will always be in range [-lag_range, lag_range] so we keep position by adding lag_range
            item_lags = item_positions - current_positions[position_index] + lag_range
            total_connectivity[item_lags] += item_connections[item, presentation]
            total_possible_lags[item_lags] += 1

    # divide by possible lags to get average connectivity
    total_possible_lags[total_connectivity == 0] += 1
    connectivity = total_connectivity / total_possible_lags
    return connectivity