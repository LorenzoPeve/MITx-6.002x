import random
random.seed(41)

def flip(num_flips: int):
    heads = 0
    for _ in range(num_flips):
        if random.choice(['H', 'T']) == 'H':
            heads += 1

    return heads/num_flips

def flip_sim(num_flips_per_trial, num_trials):
    frac_heads = []
    for _ in range(num_trials):
        frac_heads.append(flip(num_flips_per_trial))
    mean = sum(frac_heads)/len(frac_heads)
    return mean

print('Using 10 flips for 1 trial')
print('Mean =', flip_sim(10, 1))
print('Mean =', flip_sim(10, 1))
print('Mean =', flip_sim(10, 1))

print('---------')
print('Using 10 flips for 100 trials')
print('Mean =', flip_sim(10, 100))
print('Mean =', flip_sim(10, 100))
print('Mean =', flip_sim(10, 100))

print('---------')
print('Using 100 flips 100,000 trials')
print('Mean =', flip_sim(100, 100000))

print('---------')
print('Using 100_000 flips 1 trials')
print('Mean =', flip_sim(100_000, 1))
print('Mean =', flip_sim(100_000, 1))