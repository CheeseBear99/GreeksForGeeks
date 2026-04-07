# GreeksForGeeks
A simple python library that calculates accurate options greeks from market derived implied volatility by reversing the black-scholes-merton equation.

INSTALLATION: ```pip install greeksforgeeks```<br>
Link to PyPi: https://pypi.org/project/greeksforgeeks/

Calculates the following options metrics:
- Delta
- Gamma
- Vega/Kappa
- Theta
- Rho
- Implied Volatility

## Examples:



```python
from greeksforgeeks import greeks
```

```python
delta = greeks.get_options_delta(S, K, t, r, q, P, is_call)
```

```python
theta = greeks.get_options_theta(S, K, t, r, q, d, P, is_call)
```

```python
gamma = greeks.get_options_gamma(same as get_options_delta)
```

```python
vega = greeks.get_options_vega(same as get_options_delta)
```

```python
rho = greeks.get_options_rho(same as get_options_delta)
```

```python
implied_volatility = greeks.get_implied_volatility(same as get_options_delta)
```

Method Parameter Definitions:

- S = Current stock price
- K = Strike price of option
- t = Time until maturity in years (for example for option expiring in 3 days t = 3/365)
- r = Risk free rate
- q = Dividend rate (minor impact for short term options so you can leave as 0 if you would like)
- d = Amount of days to annualize theta by (use either 252 or 365, i recommend 365)
- P = Current price of the option (use midpoint)
- is_call = Boolean value (true if you are solving for a call, false if put)
 







