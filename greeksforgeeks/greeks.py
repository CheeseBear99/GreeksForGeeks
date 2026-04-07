import math
from scipy.stats import norm
from scipy.optimize import brentq


def calc_d1(stock_price, strike, t, r, q, implied_vol):
    return (math.log(stock_price / strike) + (t * (r - q + ((implied_vol ** 2) / 2)))) / (implied_vol * math.sqrt(t))


def compute_blackscholes_price(stock_price, strike, t, r, q, implied_vol, is_call=True):
    d1 = calc_d1(stock_price, strike, t, r, q, implied_vol)
    d2 = d1 - implied_vol * math.sqrt(t)

    if is_call:
        return (stock_price * math.exp(-q * t) * norm.cdf(d1)) - (strike * math.exp(-r * t) * norm.cdf(d2))
    else:
        return (strike * math.exp(-r * t) * norm.cdf(-d2)) - (stock_price * math.exp(-q * t) * norm.cdf(-d1))


def get_implied_volatility(stock_price, strike, t, r, q, option_price, is_call=True):
    return brentq(
        lambda implied_vol:
        compute_blackscholes_price(stock_price, strike, t, r, q, implied_vol, is_call) - option_price, 1e-10, 10)


def get_option_delta(stock_price, strike, t, r, q, option_price, is_call=True):
    implied_vol = get_implied_volatility(stock_price, strike, t, r, q, option_price, is_call)
    d1 = calc_d1(stock_price, strike, t, r, q, implied_vol)

    if is_call:
        return norm.cdf(d1) * math.exp(-q * t)
    else:
        return (norm.cdf(d1) - 1) * math.exp(-q * t)


def get_option_gamma(stock_price, strike, t, r, q, option_price, is_call=True):
    implied_vol = get_implied_volatility(stock_price, strike, t, r, q, option_price, is_call)
    d1 = calc_d1(stock_price, strike, t, r, q, implied_vol)

    return (math.exp(-q * t) * norm.pdf(d1)) / (stock_price * implied_vol * math.sqrt(t))


def get_option_theta(stock_price, strike, t, r, q, d, option_price, is_call=True):
    implied_vol = get_implied_volatility(stock_price, strike, t, r, q, option_price, is_call)
    d1 = calc_d1(stock_price, strike, t, r, q, implied_vol)
    d2 = d1 - implied_vol * math.sqrt(t)

    if is_call:
        return (((-norm.pdf(d1) * stock_price * implied_vol * math.exp(-q * t)) / (2 * math.sqrt(t))) - (
                r * strike * math.exp(-r * t) * norm.cdf(d2)) + (
                        q * stock_price * math.exp(-q * t) * norm.cdf(d1))) / d
    else:
        return (((-norm.pdf(d1) * stock_price * implied_vol * math.exp(-q * t)) / (2 * math.sqrt(t))) + (
                r * strike * math.exp(-r * t) * norm.cdf(-d2)) - (
                        q * stock_price * math.exp(-q * t) * norm.cdf(-d1))) / d


def get_option_vega(stock_price, strike, t, r, q, option_price, is_call=True):
    implied_vol = get_implied_volatility(stock_price, strike, t, r, q, option_price, is_call)
    d1 = calc_d1(stock_price, strike, t, r, q, implied_vol)

    return 0.01 * stock_price * math.exp(-q * t) * math.sqrt(t) * norm.pdf(d1)


def get_option_rho(stock_price, strike, t, r, q, option_price, is_call=True):
    implied_vol = get_implied_volatility(stock_price, strike, t, r, q, option_price, is_call)
    d2 = calc_d1(stock_price, strike, t, r, q, implied_vol) - implied_vol * math.sqrt(t)

    if is_call:
        return 0.01 * strike * t * math.exp(-r * t) * norm.cdf(d2)
    else:
        return -0.01 * strike * t * math.exp(-r * t) * norm.cdf(-d2)
    