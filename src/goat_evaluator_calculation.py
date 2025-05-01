# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import math

def era_diff(era, era_input):
    if era > era_input:
        return 0
    else:
        return era_input-era
    
def era_diff_perc_score(era_diff, era_input, score):
    return (era_diff/era_input) * score

def era_diff_log(era_diff_perc_score):
    if era_diff_perc_score <= 0:
        return 0
    else:
        return (math.log10(era_diff_perc_score)) * 10
    
def acc_score(acc, max_acc):
    return (acc/max_acc) * 100.0

def prime_rise(rs, ps):
    return (ps/rs) - 1

def prime_stats(rs, rs_input, ps, ps_input, lng):
    return (rs * rs_input) + (ps * ps_input) + (lng * 0.5)

def prime_stats_score(prime_stats, max_prime_stats):
    return (prime_stats/max_prime_stats) * 100.0

def prime_advanced_rise(rs, ps):
    return (ps/rs) - 1

def prime_advanced(rs, rs_input, ps, ps_input, corp, lng):
    return (rs * rs_input) + (ps * ps_input) + (corp * 6.5) + (lng * 1.85)

def prime_advanced_score(prime_advanced, max_prime_advanced):
    return (prime_advanced/max_prime_advanced) * 100.0

def overall_prime(prime_stats_score, box_score_input, prime_advanced_score, adv_input):
    return (prime_stats_score * box_score_input) + (prime_advanced_score * adv_input)

def peak_rise(rs, ps):
    return (ps/rs) - 1

def peak_stats(rs, rs_input, ps, ps_input):
    return (rs * rs_input) + (ps * ps_input)

def peak_stats_score(peak_stats, max_peak_stats):
    return (peak_stats/max_peak_stats) * 100.0

def peak_advanced_rise(rs, ps):
    return (ps/rs) - 1

def peak_advanced(rs, rs_input, ps, ps_input, corp):
    return (rs * rs_input) + (ps * ps_input) + (corp * 6.5)

def peak_advanced_score(peak_advanced, max_peak_advanced):
    return (peak_advanced/max_peak_advanced) * 100.0

def overall_peak(peak_stats_score, box_score_input, peak_advanced_score, adv_input):
    return (peak_stats_score * box_score_input) + (peak_advanced_score * adv_input)


if __name__ == '__main__':
    era = 1.0
    box_score = 30/100
    adv = 70/100
    rs = 35/100
    ps = 65/100
    accolades = 45
    prime = 5
    peak = 5
    prime_perc = (prime)/(prime+peak)
    peak_perc = (peak)/(prime+peak)
    leaderboard = 5
    two_way = 0
    playoff_rise = 5
    rs_winning = 10
    ps_winning = 20
    versatility = 5
    cultural = 0
    artistry = 0
    raw_df = pd.read_csv("../raw_data/Goat Evaluator Raw Data.csv")