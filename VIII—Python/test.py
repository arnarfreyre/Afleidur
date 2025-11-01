from functions import VIII_Solvers



S0 = 100
K = 105
T = 1
r = 0.05
sigma = 0.2
n_sim = 100000

market_price = 6.8

solver = VIII_Solvers(S0,K,T,r,sigma,n_sim)
gamma = solver.call_gamma()
print(gamma)


IV = solver.BSM_IV(market_price)


