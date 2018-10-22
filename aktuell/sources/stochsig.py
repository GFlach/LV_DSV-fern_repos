# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 14:03:20 2016

@author: Flach
"""

from pylab import *
from random import gauss,triangular
import matplotlib.pyplot as plt
import statistics

def generate_signals(nx,ny,nz):
    X = []
    Y = []
    Z = []
    for i in range(nx):
        X.append(round(gauss(0,1)*100))

    for i in range(ny):
        Y.append(round(triangular(-0.5,0.5)*100))
        

    for i in range(nz):
        Z.append(round(uniform(-100,100)))

    return(X,Y,Z)
    
def generate_corrsignals(nx):
    X = []
    Y = []
    Z = []
    for i in range(nx):
        X.append(round(gauss(0,1)*100))
    Y = list(array(X) + 5)
    Z = list(-array(X))
    return(X,Y,Z)

    
def show_signals(x,y,z):
    fig = plt.figure(figsize=(15,4))
    fig.add_subplot(131)
    plot(x, '.')
    grid()
    title('Datenreihe 1')
    fig.add_subplot(132)
    plot(y, '.')
    grid()
    title('Datenreihe 2')
    fig.add_subplot(133)
    plot(z, '.')
    grid()
    title('Datenreihe 3')

def show_histograms(x,y,z):
    fig = plt.figure(figsize=(15,4))
    fig.add_subplot(131)
    n, bins, patches = plt.hist(x, 10, normed=0, facecolor='blue', alpha=0.5)
    grid()
    title('Histogramm 1')
    fig.add_subplot(132)
    n, bins, patches = plt.hist(y, 10, normed=0, facecolor='blue', alpha=0.5)
    grid()
    title('Histogramm 2')
    fig.add_subplot(133)
    n, bins, patches = plt.hist(z, 10, normed=0, facecolor='blue', alpha=0.5)
    grid()
    title('Histogramm 3')

def mean_var(x,y,z):
    mw = mean(x)
    var = statistics.pvariance(x) 
    print('Datenreihe 1:\nMittelwert: ' + str(round(mw,2)) +' Varianz: ' + str(round(var,2)) + '\n')
    mw = mean(y)
    var = statistics.pvariance(y) 
    print('Datenreihe 2:\nMittelwert: ' + str(round(mw,2)) +' Varianz: ' + str(round(var,2)) + '\n')
    mw = mean(z)
    var = statistics.pvariance(z) 
    print('Datenreihe 3:\nMittelwert: ' + str(round(mw,2)) +' Varianz: ' + str(round(var,2)) + '\n')

def show_dependency(x,y,z):
    if len(x) != len(y) != len(z):
        print('Datenreihen müssen gleiche Länge haben')
        return 0
    fig = plt.figure(figsize=(15,4))
    fig.add_subplot(131)
    plot(x,y, '.')
    grid()
    xlabel('Datenreihe 1')
    ylabel('Datenreihe 2')
    title('DR 1 - DR 2')
    fig.add_subplot(132)
    plot(x,z, '.')
    grid()
    xlabel('Datenreihe 1')
    ylabel('Datenreihe 3')
    title('DR 1 - DR 3')
    fig.add_subplot(133)
    plot(y,z, '.')
    grid()
    xlabel('Datenreihe 2')
    ylabel('Datenreihe 3')
    title('DR 2 - DR 3')

def covariance_matrix(x,y,z):
    if (len(x) != len(y) != len(z)):
        print('Datenreihen müssen gleiche Länge haben')
        return 0
    A = array(x + y + z)
    B = A.reshape(3,len(x))
    C = cov(B, bias=True).round(2)
    print('Kovarianzmatrix:')
    print(C)

def gen_ssn(anz, mu, sigma, fak):
        D = []
        seed()
        for i in range(anz):
            D.append(round(gauss(mu/fak,sigma)*fak))
        return(D)

def show_ssn(x):
    plot(x, '.')
    grid()
    title('normalverteilte Daten')

def show_hist_ssn(x, bins):
    plt.hist(x, bins, normed=0, facecolor='blue', alpha=0.5)
    grid()
    title('Histogramm')
    
    
    
    

