# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 16:23:25 2016

@author: Admin_1
"""
from pylab import *


from scipy.signal import butter, lfilter
from scipy.signal import freqz
import matplotlib.pyplot as plt
import numpy as np

def butter_hp_filter(data, fgu=1000, fs=44100, order=5):
    b, a = butter_hp(fgu, fs, order=order)
    y = lfilter(b, a, data)
    return y

def butter_lp_filter(data, fgo=1000, fs=44100, order=5):
    b, a = butter_lp(fgo, fs, order=order)
    y = lfilter(b, a, data)
    return y


def filter_fgang(fs=44100, fgu=1000,  fgo=1000, order=5, typ='lp'):
    nyq = 0.5 * fs
    low = fgu / nyq
    high = fgo / nyq
    fig = plt.figure(figsize=(16,4))
    if typ == 'lp':
        b, a = butter(order, [high])
    elif typ == 'hp':
        b, a = butter(order, [low], btype='highpass')
    elif typ == 'bp':
        b, a = butter(order, [low, high], btype='bandpass')
    elif typ == 'bs':
        b, a = butter(order, [low, high], btype='bandstop')
    else:
        print('Filtertyp nicht bekannt.')
        return
    w, h = freqz(b, a, worN=None)
    plt.plot((fs * 0.5 / np.pi) * w, abs(h))
    plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)], 
             '--')    
    plt.xlabel('Frequenz (Hz)')
    plt.ylabel('Verstärkung')
    plt.grid(True)
    plt.axis([8,8000,0,1.5])
    plt.title('Frequenzgang Butterworth-Filter Ordnung %s' %order)
    return fig

def filter_appl(fs, data_in, fgu=1000, fgo=1000, order=5, typ='lp'):
    nyq = 0.5 * fs
    low = fgu / nyq
    high = fgo / nyq
    if typ == 'lp':
        b, a = butter(order, [high])
    elif typ == 'hp':
        b, a = butter(order, [low], btype='highpass')
    elif typ == 'bp':
        b, a = butter(order, [low, high], btype='bandpass')
    elif typ == 'bs':
        b, a = butter(order, [low, high], btype='bandstop')
    else:
        print('Filtertyp nicht bekannt.')
        return
    data_out = lfilter(b, a, data_in)
    return data_out
    
def bandfilter(fgu=1000, fgo=1000, order=5):
    fs = 44100
    b_lp, a_lp = butter_lp(fgo, fs, order)
    b_hp, a_hp = butter_hp(fgu, fs, order)
    w_lp, h_lp = freqz(b_lp, a_lp, worN=None)
    w_hp, h_hp = freqz(b_hp, a_hp, worN=None)
    w_bp = w_lp
    if fgu > fgo:
        h_bp = (h_lp + h_hp)
        #typ = 'Bandsperre'
    else:
        h_bp = h_lp * h_hp
        #typ = 'Bandpass'
        
    plt.plot((fs * 0.5 / np.pi) * w_bp, abs(h_bp))

    plt.plot([fs, 0.5 * 1], [np.sqrt(0.5), np.sqrt(0.5)],
             '--')
    plt.xlabel('Frequenz (Hz)')
    plt.ylabel('Verstärkung')
    plt.grid(True)
    plt.axis([0,4000,0,1.5])
    plt.title('Bandfilter Ordnung %s' %order)    


