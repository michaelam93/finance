# A simple program which uses the Black-Scholes model to calculates an indices European call option valuation at maturity by using a Monte Carlo simulation where an options risk factor obeys geometric Brownian motion
# Reference: Python for Finance by Yves Hilpisch (O’Reilly). Copyright 2015 Yves Hilpisch, 978-1-491-94528-5.

from numpy import *

S0 = 100		#initial stock index level
K = 105			#strike price
T = 1.0			#time to maturity in years
r = 0.05		#riskless short rate
sigma = 0.2		#constant volatility

I = 100000		#number of times we calculate

z = random.standard_normal(I)	#random numbers
ST = S0 * exp((r - 0.5 * sigma ** 2) * T + sigma * sqrt(T) * z)		#Black-Sholes-Merton (1973)
hT = maximum(ST - K, 0)			#inner values
C0 = exp(-r * T) * sum(hT)/I 	#Estimator for Monte Carlo simulation

print "Value of the European Call Option %5.3f" % C0