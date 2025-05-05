# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import math

def get_era_diff(era, era_input):
    if era > era_input:
        return 0
    else:
        return era_input-era
    
def get_era_diff_perc_score(era_diff, era_input, score):
    return (era_diff/era_input) * score

def get_era_diff_log(era_diff_perc_score):
    if era_diff_perc_score <= 0:
        return 0
    else:
        return (math.log10(era_diff_perc_score)) * 10
    
def get_acc_score(acc, max_acc):
    return (acc/max_acc) * 100.0

def get_prime_rise(rs, ps):
    return (ps/rs) - 1

def get_prime_stats(rs, rs_input, ps, ps_input, lng):
    return (rs * rs_input) + (ps * ps_input) + (lng * 0.5)

def get_prime_stats_score(prime_stats, max_prime_stats):
    return (prime_stats/max_prime_stats) * 100.0

def get_prime_advanced_rise(rs, ps):
    return (ps/rs) - 1

def get_prime_advanced(rs, rs_input, ps, ps_input, corp, lng):
    return (rs * rs_input) + (ps * ps_input) + (corp * 6.5) + (lng * 1.85)

def get_prime_advanced_score(prime_advanced, max_prime_advanced):
    return (prime_advanced/max_prime_advanced) * 100.0

def get_overall_prime(prime_stats_score, box_score_input, prime_advanced_score, adv_input):
    return (prime_stats_score * box_score_input) + (prime_advanced_score * adv_input)

def get_peak_rise(rs, ps):
    return (ps/rs) - 1

def get_peak_stats(rs, rs_input, ps, ps_input):
    return (rs * rs_input) + (ps * ps_input)

def get_peak_stats_score(peak_stats, max_peak_stats):
    return (peak_stats/max_peak_stats) * 100.0

def get_peak_advanced_rise(rs, ps):
    return (ps/rs) - 1

def get_peak_advanced(rs, rs_input, ps, ps_input, corp):
    return (rs * rs_input) + (ps * ps_input) + (corp * 6.5)

def get_peak_advanced_score(peak_advanced, max_peak_advanced):
    return (peak_advanced/max_peak_advanced) * 100.0

def get_overall_peak(peak_stats_score, box_score_input, peak_advanced_score, adv_input):
    return (peak_stats_score * box_score_input) + (peak_advanced_score * adv_input)

def get_prime_b(pr_rise):
    return pr_rise * 2

def get_prime_a(pr_a_rise):
    return pr_a_rise

def get_peak_b(pe_rise):
    return pe_rise * 2

def get_peak_a(pe_a_rise):
    return pe_a_rise

def get_w_total(pr_b, box_score_input, pr_a, adv_input, pr_perc, pe_b, pe_a, pe_perc):
    return ((((pr_b * box_score_input) + (pr_a * adv_input)) * pr_perc) + ((((pe_b * box_score_input) + (pe_a * adv_input)) * pe_perc))/3) * 100.0

def get_rel_w_total(w_tot, avg_w_tot):
    return w_tot - avg_w_tot

def get_playoff_rise_score(rel_w_tot):
    if rel_w_tot > -1:
        return min(100, rel_w_tot + 80)
    else:
        return min(100, rel_w_tot + 60)
    
def get_leaderboard_score(leaderboard, max_leaderboard):
    return (leaderboard/max_leaderboard) * 100.0

def get_prime_2_way_score(pr_2_way, max_pr_2_way):
    return (pr_2_way/max_pr_2_way) * 100.0

def get_peak_2_way_score(pe_2_way, max_pe_2_way):
    return (pe_2_way/max_pe_2_way) * 100.0

def get_rs_2_way_score(rs_2_way, max_rs_2_way):
    return (rs_2_way/max_rs_2_way) * 100.0

def get_ps_2_way_score(ps_2_way, max_ps_2_way):
    return (ps_2_way/max_ps_2_way) * 100.0

def get_2_way_score(pr_2, pr_perc, pe_2, pe_perc, rs_2, rs_perc, ps_2, ps_perc):
    return (((pr_2 * pr_perc) + (pe_2 * pe_perc)) * 0.7) + (((rs_2 * rs_perc) + (ps_2 * ps_perc)) * 0.3)

def get_rs_winning_score(rs_winning, max_rs_winning):
    return (rs_winning/max_rs_winning) * 100.0

def get_ps_winning_score(ps_winning, max_ps_winning):
    return (ps_winning/max_ps_winning) * 100.0

def get_ovr_versatility(rsv, rs_perc, psv, ps_perc, dnr):
    return (rsv * rs_perc) + (psv * ps_perc) + dnr

def get_versatility_score(vers, max_vers):
    return (vers/max_vers) * 100.0

def get_raw_score(acc_score, acc_input, pr_o, pri, pe_o, pea, lead, lead_input, two_way, two_input, rs_w, rs_w_input, ps_w, ps_w_input, play_rise, play_rise_input, vers, vers_input, cul, cul_input, art, art_input):
    return ((acc_score * acc_input) + (pr_o * pri) + (pe_o * pea) + (lead * lead_input) + (two_way * two_input) + (rs_w * rs_w_input) + (ps_w * ps_w_input) + (play_rise * play_rise_input) + (vers * vers_input) + (cul * cul_input) + (art * art_input))/100

def get_raw_score_with_era(acc_score, acc_input, pr_o, pri, pe_o, pea, lead, lead_input, two_way, two_input, rs_w, rs_w_input, ps_w, ps_w_input, play_rise, play_rise_input, vers, vers_input, cul, cul_input, art, art_input, era_diff_log):
    return (((acc_score * acc_input) + (pr_o * pri) + (pe_o * pea) + (lead * lead_input) + (two_way * two_input) + (rs_w * rs_w_input) + (ps_w * ps_w_input) + (play_rise * play_rise_input) + (vers * vers_input) + (cul * cul_input) + (art * art_input))/100) - era_diff_log

def get_goat_score(raw, max_raw):
    return (raw/max_raw) * 100.0

def get_sort_df(df):
    sort_df = df.sort_values(by='goat_score', ascending=False)
    sort_df['Rank'] = np.arange(len(sort_df)) + 1
    sort_df['Goat Score'] = round(sort_df['goat_score'],3)
    final_df = sort_df[['Player', 'Goat Score', 'Rank']]
    return final_df 

def calculate_goat_evualation(raw_df, era, box_score, adv, rs, ps, accolades, prime, peak, prime_perc, peak_perc, leaderboard, two_way, playoff_rise, rs_winning, ps_winning, versatility, cultural, artistry):
    raw_df.fillna(0, inplace=True)
    raw_df['era_diff'] = [get_era_diff(a,era) for a in raw_df['Era']]
    raw_df['acc_score'] = [get_acc_score(a, max(raw_df['Accolades'])) for a in raw_df['Accolades']]
    raw_df['prime_rise'] = [get_prime_rise(a,b) for (a,b) in zip(raw_df['Prime_Rs'], raw_df['Prime_Ps'])]
    raw_df['prime_stats'] = [get_prime_stats(a,rs,c,ps,e) for (a,c,e) in zip(raw_df['Prime_Rs'], raw_df['Prime_Ps'], raw_df['Prime_Lng'])]
    raw_df['prime_stats_score'] = [get_prime_stats_score(a,max(raw_df['prime_stats'])) for a in raw_df['prime_stats']]
    raw_df['prime_advanced_rise'] = [get_prime_advanced_rise(a,b) for (a,b) in zip(raw_df['Prime_Rs_Adv'], raw_df['Prime_Ps_Adv'])]
    raw_df['prime_advanced'] = [get_prime_advanced(a,rs,b,ps,c,d) for (a,b,c,d) in zip(raw_df['Prime_Rs_Adv'], raw_df['Prime_Ps_Adv'], raw_df['Prime_Corp'], raw_df['Prime_Lng'])]
    raw_df['prime_advanced_score'] = [get_prime_advanced_score(a, max(raw_df['prime_advanced'])) for a in raw_df['prime_advanced']]
    raw_df['prime_overall'] = [get_overall_prime(a,box_score,b,adv) for (a,b) in zip(raw_df['prime_stats_score'], raw_df['prime_advanced_score'])]
    raw_df['peak_rise'] = [get_peak_rise(a,b) for (a,b) in zip(raw_df['Peak_Rs'], raw_df['Peak_Ps'])]
    raw_df['peak_stats'] = [get_peak_stats(a,rs,b,ps) for (a,b) in zip(raw_df['Peak_Rs'], raw_df['Peak_Ps'])]
    raw_df['peak_stats_score'] = [get_peak_stats_score(a, max(raw_df['peak_stats'])) for a in raw_df['peak_stats']]
    raw_df['peak_advanced_rise'] = [get_peak_advanced_rise(a,b) for (a,b) in zip(raw_df['Peak_Rs_Adv'], raw_df['Peak_Ps_Adv'])]
    raw_df['peak_advanced'] = [get_peak_advanced(a,rs,b,ps,c) for (a,b,c) in zip(raw_df['Peak_Rs_Adv'], raw_df['Peak_Ps_Adv'], raw_df['Peak_Corp'])]
    raw_df['peak_advanced_score'] = [get_peak_advanced_score(a,max(raw_df['peak_advanced'])) for a in raw_df['peak_advanced']]
    raw_df['peak_overall'] = [get_overall_peak(a,box_score,b,adv) for (a,b) in zip(raw_df['peak_stats_score'], raw_df['peak_advanced_score'])]
    raw_df['prime_b'] = [get_prime_b(a) for a in raw_df['prime_rise']]
    raw_df['prime_a'] = [get_prime_a(a) for a in raw_df['prime_advanced_rise']]
    raw_df['peak_b'] = [get_peak_b(a) for a in raw_df['peak_rise']]
    raw_df['peak_a'] = [get_peak_a(a) for a in raw_df['peak_advanced_rise']]
    raw_df['w_total'] = [get_w_total(a,box_score,b,adv,prime_perc,c,d,peak_perc) for (a,b,c,d) in zip(raw_df['prime_b'],raw_df['prime_a'],raw_df['peak_b'],raw_df['peak_a'])]
    raw_df['rel_w_total'] = [get_rel_w_total(a,raw_df['w_total'].mean()) for a in raw_df['w_total']]
    raw_df['playoff_rise_score'] = [get_playoff_rise_score(a) for a in raw_df['rel_w_total']]
    raw_df['leaderboard_score'] = [get_leaderboard_score(a,max(raw_df['Leaderboard'])) for a in raw_df['Leaderboard']]
    raw_df['prime_2_way_score'] = [get_prime_2_way_score(a,max(raw_df['Prime_2_Way'])) for a in raw_df['Prime_2_Way']]
    raw_df['peak_2_way_score'] = [get_peak_2_way_score(a,max(raw_df['Peak_2_Way'])) for a in raw_df['Peak_2_Way']]
    raw_df['rs_2_way_score'] = [get_rs_2_way_score(a,max(raw_df['Rs_2_Way'])) for a in raw_df['Rs_2_Way']]
    raw_df['ps_2_way_score'] = [get_ps_2_way_score(a,max(raw_df['Ps_2_Way'])) for a in raw_df['Ps_2_Way']]
    raw_df['2_way_score'] = [get_2_way_score(a,prime_perc,b,peak_perc,c,rs,d,ps) for (a,b,c,d) in zip(raw_df['prime_2_way_score'],raw_df['peak_2_way_score'],raw_df['rs_2_way_score'],raw_df['ps_2_way_score'])]
    raw_df['rs_winning_score'] = [get_rs_winning_score(a,max(raw_df['Rs_Winning'])) for a in raw_df['Rs_Winning']]
    raw_df['ps_winning_score'] = [get_ps_winning_score(a,max(raw_df['Ps_Winning'])) for a in raw_df['Ps_Winning']]
    raw_df['ovr_versatility'] = [get_ovr_versatility(a,rs,b,ps,c) for (a,b,c) in zip(raw_df['Rsv'],raw_df['Psv'],raw_df['Dnr'])]
    raw_df['versatility_score'] = [get_versatility_score(a,max(raw_df['ovr_versatility'])) for a in raw_df['ovr_versatility']]
    raw_df['raw_score'] = [get_raw_score(a,accolades,b,prime,c,peak,d,leaderboard,e,two_way,f,rs_winning,g,ps_winning,h,playoff_rise,i,versatility,j,cultural,k,artistry) 
                           for (a,b,c,d,e,f,g,h,i,j,k) in zip(raw_df['acc_score'],raw_df['prime_overall'],raw_df['peak_overall'],raw_df['leaderboard_score'],raw_df['2_way_score'],raw_df['rs_winning_score'],raw_df['ps_winning_score'],raw_df['playoff_rise_score'],raw_df['versatility_score'],raw_df['Culture'],raw_df['Artistry'])]
    raw_df['era_diff_perc_score'] = [get_era_diff_perc_score(a,era,b) for (a,b) in zip(raw_df['era_diff'],raw_df['raw_score'])]
    raw_df['era_diff_log'] = [get_era_diff_log(a) for a in raw_df['era_diff_perc_score']]
    raw_df['raw_score_with_era'] = [get_raw_score_with_era(a,accolades,b,prime,c,peak,d,leaderboard,e,two_way,f,rs_winning,g,ps_winning,h,playoff_rise,i,versatility,j,cultural,k,artistry,l) 
                           for (a,b,c,d,e,f,g,h,i,j,k,l) in zip(raw_df['acc_score'],raw_df['prime_overall'],raw_df['peak_overall'],raw_df['leaderboard_score'],raw_df['2_way_score'],raw_df['rs_winning_score'],raw_df['ps_winning_score'],raw_df['playoff_rise_score'],raw_df['versatility_score'],raw_df['Culture'],raw_df['Artistry'],raw_df['era_diff_log'])]
    raw_df['goat_score'] = [get_goat_score(a,max(raw_df['raw_score_with_era'])) for a in raw_df['raw_score_with_era']]
    final_df = get_sort_df(raw_df)
    return final_df

if __name__ == '__main__':
    era = 2.0
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
    df = pd.read_csv("../raw_data/Goat Evaluator Raw Data.csv")
    final_output_df = calculate_goat_evualation(df, era, box_score, adv, rs, ps, accolades, prime, peak, prime_perc, peak_perc, leaderboard, two_way, playoff_rise, rs_winning, ps_winning, versatility, cultural, artistry)