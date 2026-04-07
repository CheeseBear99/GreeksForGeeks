# GreeksForGeeks
A simple python library that calculates accurate options greeks from market derived implied volatility by reversing the black-scholes-merton equation.

INSTALLATION: ```pip install greeksforgeeks```<br>
USAGE: ```python from greeksforgeeks import greeks```

Calculates the following options metrics:
-Delta
-Gamma
-Vega/Kappa
-Theta
-Rho
-Implied Volatility

##Examples:

```python from greeksforgeeks import greeks

   delta = greeks.get_options_delta(S, K, t, r, q, P, is_call)
   theta = greeks.get_options_theta(S, K, t, r, q, d, P, is_call)
   gamma = greeks.get_options_gamma(same as get_options_delta)
   vega = greeks.get_options_vega(same as get_options_delta)
   rho = greeks.get_options_rho(same as get_options_delta)
   implied_volatility = greeks.get_implied_volatility(same as get_options_delta)
```

 







