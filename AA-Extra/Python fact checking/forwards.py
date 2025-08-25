import math


"""---------------- Multi Formula Variables ----------------"""

F_0T = []

"""---------------- Variables ----------------"""
r = 0.01 #Continuously compounded risk-free rate
t = 1 # Time Today
T = 2 # Time at maturity


S_0 = 1 #Current spot price
S_T = 1 #Spot Price at Time T
F_0T.append(S_0*math.exp(r*T)) #S0*exp(r*T)


