# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 18:34:47 2016

@author: Admin_1

Funktionen:
sprung, rampe, exponent, gauss, impulsfolge, oszi_simple, 
exp_oszi, plot_signal, plot_sigfolge
"""


import matplotlib.pyplot as plt
import numpy as np

def sprung(shift=0, abs_n = 10, weight = 1, mirr = False):
    """
    Berechnung von Werten der Sprungfunktion für -10<=n<=10
    Aufruf:
        sprung(shift=0, abs_n = 10, weight = 1, mirr = False)
    Parameter: 
        shift - Verschiebung (default 0)
        abs_n - Index der ATW (default 10)
        weight - Bewertung der Sprungfunktion (default 1)
        mirr - Spiegelung (default False)
    Rückgabe:
        data - Datenfeld
        typ - Funktionstyp
    """
    nmin = -abs_n
    nmax = abs_n
    nanz = nmax - nmin + 1
    s_n = np.zeros(nanz)
    for i in np.linspace(nmin, nmax, nanz, dtype=int):
        if np.sign(i-shift)<0:
            s_n[i+int((nanz-1)/2)] = 0
        else:
            s_n[i+int((nanz-1)/2)] = weight*1
    if shift == 0:
        typ = 'sprung'
    else:
        typ = 'sprung_shift'

    if mirr == True:
        s_n = s_n[::-1]
    return s_n, typ        

    
def rampe(shift=0, abs_n = 10, weight = 1, mirr = False):
    """
    Berechnung von Werten der Rampenfunktion für -10<=n<=10
    Aufruf:
        rampe(shift=0, abs_n = 10, weight = 1, mirr = False)
    Parameter: 
        shift - Verschiebung (default 0)
        abs_n - Index der ATW (default 10)
        weight - Bewertung der Sprungfunktion (default 1)
        mirr - Spiegelung (default False)
    Rückgabe:
        data - Datenfeld
        typ - Funktionstyp
    """
    nmin = -abs_n
    nmax = abs_n
    nanz = nmax - nmin + 1
    s_n = np.zeros(nanz)
    for i in np.linspace(nmin, nmax, nanz, dtype=int):
        if np.sign(i-shift) < 0:
            s_n[i+int((nanz-1)/2)] = 0
        else:
            s_n[i+int((nanz-1)/2)] = weight*(i-shift)
    if shift == 0:
        typ = 'rampe'
    else:
        typ = 'rampe_shift'
        
    if mirr == True:
        s_n = s_n[::-1]

    return s_n, typ       

def exponent(type=1, a=1, abs_n = 10, weight=1, mirr = False):
    """
    Berechnung von Werten der Exponentialfunktion für -10<=n<=10
    Aufruf:
        exponent(type=1, a=1, abs_n = 10, weight=1, mirr = False)
    Parameter: 
        type - einseitig/zweiseitig  (default 1)
        a - Exponentenbewertung (default 1)
        weight - Bewertung (default 1)
        abs_n - Index der ATW (default 10)
        mirr - Spiegelung (default False)
    Rückgabe:
        data - Datenfeld
        typ - Funktionstyp
    """
    nmin = -abs_n
    nmax = abs_n
    nanz = nmax - nmin + 1
    s_n = np.zeros(nanz)
    for i in np.linspace(nmin, nmax, nanz, dtype=int):
        if type == 1:
            if np.sign(i)<0:
                s_n[i+int((nanz-1)/2)] = 0
            else:
                s_n[i+int((nanz-1)/2)] = weight*a**i
            typ = 'exp1'
        else:
            s_n[i+int((nanz-1)/2)] = weight*a**abs(i)
            typ = 'exp2'

    if mirr == True:
        s_n = s_n[::-1]

    return s_n, typ       

def gauss(abs_n = 10, a=-1, weight=1):
    """
    Berechnung von Werten der Gaussfunktion für -10<=n<=10
    Aufruf:
       gauss(abs_n = 10, a=-1, weight=1) 
    Parameter: Exponent
        abs_n - Index der ATW (default 10)
        a - Exponentenbewertung (default 1)
        weight - Bewertung (default 1)
    Rückgabe:
        data - Datenfeld
        typ - Funktionstyp
    """
    nmin = -abs_n
    nmax = abs_n
    nanz = nmax - nmin + 1
    s_n = np.zeros(nanz)
    for i in np.linspace(-abs_n, abs_n, nanz, dtype=int):
        s_n[i+abs_n] = weight*np.exp(a*i**2)
    typ = 'gauss'
    return s_n, typ       

def impulsfolge(abs_n = 10, periode=1, weight=1):
    """
    Berechnung von Werten der Impulsfolge für -10<=n<=10
    Aufruf: 
        impulsfolge(abs_n = 10, periode=1, weight=1)
    Parameter: 
        abs_n - Index der ATW (default 10)
        periode - Periodendauer der Folge in ATW (default )
        weight - Bewertung (default 1)
    Rückgabe:
        data - Datenfeld
        typ - Funktionstyp
    """
    n = np.linspace(-abs_n,abs_n, 2*abs_n+1, dtype=int)
    data = np.zeros(2*abs_n+1)
    for i in range(0,len(n)//(2*periode)+1):
        data[abs_n-i*periode] = weight * 1
        data[abs_n+i*periode] = weight * 1
    typ = 'if'
    return data, typ
            
def oszi_simple(abs_n = 10, weight=1):
    """
    Berechnung von Werten des einfachsten oszillierenden Signals
    Aufruf:
        oszi_simple(abs_n = 10, weight=1)
    Parameter: 
        abs_n - Index der ATW (default 10)
        weight - Bewertung (default 1)
    Rückgabe:
        data - Datenfeld
        typ - Funktionstyp
    """
    n = np.linspace(-abs_n,abs_n, 2*abs_n+1, dtype=int)
    data = np.zeros(2*abs_n+1)
    for i in range(0,len(n)):
        data[i] = weight * (-1)**i
    typ = 'oszi_s'
    return data, typ

def exp_oszi(abs_n = 10, pd=1, weight=1, mirr = False):
    """
    Berechnung von Werten der komplexen Exponentialschwingung
    Aufruf: 
        exp_oszi(abs_n = 10, pd=1, weight=1, mirr = False)
    Parameter: 
        abs_n - Index der ATW (default 10)
        pd - Periodendauer in ATW  (default 1)
        weight - Bewertung (default 1)
        mirr - Spiegelung (default False)
    Rückgabe:
        data - Datenfeld
        typ - Funktionstyp
    """
    nmin = -abs_n
    nmax = abs_n
    nanz = nmax - nmin + 1
    n = np.linspace(nmin, nmax, nanz, dtype=int)
    data = np.zeros(nanz,dtype=complex)
    theta_0=2*np.pi/pd
    for i in range(0,len(n)//2+1):
        data[int((nanz-1)/2)-i] = weight * np.exp(1j*theta_0*i)
        data[int((nanz-1)/2)+i] = weight * np.exp(1j*theta_0*i)
    if mirr == True:
        data = data[::-1]
    typ = 'exp_oszi'
        
    return data, typ

        
def plot_signal(data=[], sig_typ=''):
    """
    Darstellung von Signalfunktionen für -10<=n<=10
    Aufruf: plot_signal(data=[], sig_typ='')
    Parameter: 
        data  - Datenfeld
        sig_typ - Funktionstyp
    Rückgabe:
    """
    
    n = np.linspace(-(len(data-1)/2), len(data-1)/2, len(data), dtype=int)
    plt.stem(n, data)
    plt.axis([-(len(data-1)/2), len(data-1)/2, min(data)-1, max(data)+1])
    plt.grid(True)
    if sig_typ == 'sprung':
        plt.title('Ausschnitt aus Sprungfunktion')
    if sig_typ == 'sprung_shift':
        plt.title('Ausschnitt aus verschobener Sprungfunktion')
    if sig_typ == 'rampe':
        plt.title('Ausschnitt aus Rampenfunktion')
    if sig_typ == 'rampe_shift':
        plt.title('Ausschnitt aus verschobener Rampenfunktion')
    if sig_typ == 'exp1':
        plt.title('Ausschnitt aus einseitiger Exponentialfunktion')
    if sig_typ == 'exp2':
        plt.title('Ausschnitt aus zweiseitiger Exponentialfunktion')
    if sig_typ == 'gauss':
       plt. title('Ausschnitt aus Gaussfunktion')
    if sig_typ == 'if':
        plt.title('Ausschnitt aus Impulsfolge')
    if sig_typ == 'oszi_s':
        plt.title('Ausschnitt aus einfachstem oszillierenden Signal')
    if sig_typ == 'exp_oszi':
        plt.title('Ausschnitt aus komplexer Exponentialschwingung')
    if sig_typ == 'kombi':
        plt.title('Ausschnitt aus kombiniertem Signal')
    else:
        plt.title('Lösung Aufgabe ' + sig_typ)        
    plt.xlabel('n')
    plt.ylabel('x(n)')
    plt.show()
    
def plot_sigfolge(data=[], mytitle=''):
    """
    Darstellung von Signalfunktionen für -10<=n<=10
    Parameter: 
        data  - Datenfeld
        mytitle (default '') - Titel für Darstellung
    Rückgabe:
    """
    n = np.linspace(-10,10, 21, dtype=int)
    plt.stem(n, data)
    plt.grid(True)
    plt.axis([-10, 10, min(data)-1, max(data)+1])
    plt.title(mytitle)
    plt.xlabel('n')
    plt.ylabel('x(n)')
    plt.show()
    


