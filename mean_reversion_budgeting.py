def mean_reversion_budgeting(log_likelihoods, mean_reversion_speeds, volatilities):
    # Calculate the normalized log-likelihood scores
    scaled_speeds = [a / b for a, b in zip(mean_reversion_speeds, volatilities)]
    min_ll = min(log_likelihoods)
    max_ll = max(log_likelihoods)
    normalized_ll = [(ll - min_ll) / (max_ll - min_ll) if max_ll != min_ll else 1.0 for ll in
                     log_likelihoods]

    # Calculate the normalized relative speed of mean reversion
    min_speed = min(scaled_speeds)
    max_speed = max(scaled_speeds)
    normalized_speeds = [(speed - min_speed) / (max_speed - min_speed) for speed in
                         scaled_speeds]

    # Calculate the portfolio weights
    weights = [speed / ll if ll != 0 else 0.0 for ll, speed in
               zip(normalized_ll, normalized_speeds)]
    total_weight = sum(weights)
    normalized_weights = [weight / total_weight for weight in weights]

    return normalized_weights
