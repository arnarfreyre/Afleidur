import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq
import yfinance as yf

def black_scholes(S0, K, T, r,sigma):
    t = 0
    d1 = (np.log(S0 / K) + (r + (sigma ** 2) / 2) * (T - t)) / (sigma * np.sqrt(T - t))
    d2 = d1 - sigma * np.sqrt(T - t)
    call_price =  S0*norm.cdf(d1)-K*np.exp(-r*(T-t))*norm.cdf(d2)

    return call_price

def objective(sigma,S0, K, T, r, market_price):
    return black_scholes(S0, K, T, r,sigma)-market_price


def implied_volatility_bs(S0, K, T, r, market_price):
    implied_vol = brentq(objective, 0.01, 5.0, args=(S0, K, T, r, market_price))
    return implied_vol



S0 = 100
K = 105
T = 1
r = 0.05
market_price = 6.8


iv = implied_volatility_bs(S0, K, T, r, market_price)
print(f"Implied volatility: {iv:.4f}")

call = black_scholes(S0,K,T,r,iv)
print(f"Theoretical option price: {call:.4f}")
