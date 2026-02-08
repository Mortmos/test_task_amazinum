def calculation(test_chosen_coin, prob, prior):
    result = []

    for outcome in test_chosen_coin:
        likelihoods = [p if outcome == 'H' else 1.0 - p for p in prob]
        posterior = [pr * lik for pr, lik in zip(prior, likelihoods)]

        total_weight = sum(posterior)
        prior = [p / total_weight for p in posterior]

        next_h = sum(p * pr for p, pr in zip(prob, prior))
        result.append(round(next_h, 2))

    return result


def main():
    config = {
        "prob": [0.12, 0.27, 0.21, 0.96],
        "test_chosen_coin": ['H', 'H', 'H', 'T', 'H', 'T', 'H', 'H', 'H'],
        "prior": [0.25, 0.25, 0.25, 0.25]
    }

    result = calculation(**config)
    print(result)


if __name__ == '__main__':
    main()