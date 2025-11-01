import yfinance as yf
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt


def monte_carlo_call_price(S0, K, T, r, sigma, n_sim):
    """ Generating random values for monte carlo sim W

        Calculating the drift factor which is constant,
        Calculating the shock which represents stochastic elements

        Calculate S_T and take the average of all of them
    """
    random_vals = np.random.normal(0, 1, n_sim, )

    shock = sigma * np.sqrt(T) * random_vals
    drift = (r - (sigma ** 2) / 2)

    S_T = S0 * np.exp(drift * T + shock)

    call_payoff = np.maximum(S_T - K, 0)
    put_payoff = np.maximum(K - S_T, 0)

    call_price = np.average(call_payoff) * np.exp(-r * T)
    put_price = np.average(put_payoff) * np.exp(-r * T)

    return call_price, put_price


S0 = 100
K = 105
T = 1
r = 0.05
sigma = 0.2
n_sim = 100000

call, put = monte_carlo_call_price(S0, K, T, r, sigma, n_sim)

print("Using monte Carlo simulation")
print(f"Call price: {call:.4f}, Put price: {put:.4f}")