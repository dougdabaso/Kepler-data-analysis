# Removing systematic trends from photometry data with an EEMD-based method.

# Note: Package PTSA is required: https://github.com/compmem/ptsa.git

# This script compares the systematic trends estimated by the PDC component and 
# by an alternative trend filtering algorithm, based on the work of [trendEMF].
# Different from [trendEMF], the technique implemented here makes use of the
# Ensemble Empiricla Mode Decomposition (EEMD) to produce the IMFs, and employs
# only the energy approach of [trendEMF] to approximate the trend. 
# The testing light curve corresponding to Star ID 757076, Quarter 3.

# Author: Douglas David Baptista de Souza (douglas@linse.ufsc.br)
                                                          
# References:                            
# [trendEMF] "Trend filtering via empirical mode decompositions", A. Moghtaderi
# et al., Comp. Statistics Data Anal., vol. 58, pp. 114-126, feb. 2013.


# Importing required packages
import numpy as np
import matplotlib.pyplot as plt
import ptsa
from ptsa import emd 
from numpy import genfromtxt

# Reading data before and after entering the PDC

# Time vectors
time_before_PDC_starID_757076_quarter3 = genfromtxt('time_before_PDC_starID_757076_quarter3.csv', delimiter = ',')
time_after_PDC_starID_757076_quarter3 = genfromtxt('time_after_PDC_starID_757076_quarter3.csv', delimiter = ',')

# Photometry data, before PDC, containing systematic trends
before_PDC_starID_757076_quarter3 = genfromtxt('before_PDC_starID_757076_quarter3.csv', delimiter = ',')

# Photometry data, after PDC, systematic trends removed
after_PDC_starID_757076_quarter3 = genfromtxt('after_PDC_starID_757076_quarter3.csv', delimiter = ',')

# Applying Ensemble Empirical Mode Decomposition to obtain the IMFs
imfs_before_PDC_starID_757076_quarter3 = emd.eemd(before_PDC_starID_757076_quarter3,noise_std=1, num_ensembles=100)


# Trend approximated via SVD-based employed by Kepler PDC

approximated_PDC_trend = before_PDC_starID_757076_quarter3 - after_PDC_starID_757076_quarter3  


# Trend approximated via Empirical Mode Decomposition

# Computing the energy of each IMF obtained from the Empirical Mode Decomposition

number_of_modes_obtained = imfs_before_PDC_starID_757076_quarter3.shape[0] # Total number of IMFs obtained from the decomposition
energy_vector = [] # To store the energy of each IMF
change_sign_imf_energy = [] # To store the sign of change, check if the energy delta from (i-1)-th to the i-th IMF is positive or negative
sign_changed_flag = 0
                         
for i in range(0,number_of_modes_obtained):
    power_sig_imfs = imfs_before_PDC_starID_757076_quarter3[i,]**2
    energy_vector.append(power_sig_imfs.sum()) # Storing the energy value of each IMF
    
 
# Implementing the Energy approach for selecting IMFs described in [trendEMF]                       
    if i>0: sign_changed_flag = np.sign(energy_vector[i] - energy_vector[i-1]) # Checking whether the IMF energy has increased or decreased  
    if np.sign(energy_vector[i] - energy_vector[i-1]) > 0: change_sign_imf_energy.append(i)


# Obtaining the approximated EEMD trend as the sum of the chosen IMFs via 
# the energy approach
considered_ims_to_approx_trend = imfs_before_PDC_starID_757076_quarter3[change_sign_imf_energy,]
approx_trend_EEMD = considered_ims_to_approx_trend.sum(axis=0)



# Plot figure comparing the results
plt.figure()

# Original Light Curve at the PDC input
plt.subplot(231)
plt.plot(time_before_PDC_starID_757076_quarter3, before_PDC_starID_757076_quarter3)
plt.yscale('linear')
plt.title('Original Light Curve at the PDC input')
plt.grid(True)

# Corrected and detrended light curve
plt.subplot(232)
plt.plot(time_before_PDC_starID_757076_quarter3, after_PDC_starID_757076_quarter3)
plt.yscale('linear')
plt.title('Corrected and detrended light curve')
plt.grid(True)


# Approximated trend by PDC
plt.subplot(233)
plt.plot(time_after_PDC_starID_757076_quarter3, before_PDC_starID_757076_quarter3 - after_PDC_starID_757076_quarter3)
plt.yscale('linear')
plt.title('Approximated trend by PDC')
plt.grid(True)

# Approximated trend by EEMD
plt.subplot(234)
plt.plot(time_after_PDC_starID_757076_quarter3, approx_trend_EEMD)
plt.yscale('linear')
plt.title('Approximated trend by EEMD')
plt.grid(True)

# Detrended light curve by EEMD
plt.subplot(235)
plt.plot(time_after_PDC_starID_757076_quarter3,before_PDC_starID_757076_quarter3 - approx_trend_EEMD)
plt.yscale('linear')
plt.title('Detrended light curve by EEMD')
plt.grid(True)


