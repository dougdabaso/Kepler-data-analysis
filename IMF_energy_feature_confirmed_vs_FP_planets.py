#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:58:04 2017

@author: douglas
"""

# Importing required packages
import os

os.chdir('/Users/douglas/Documents/Douglas - arquivos/Vida academica/Kepler-data-analysis/ptsa')

import ptsa

os.chdir('/Users/douglas/Documents/Douglas - arquivos/Vida academica/Kepler-data-analysis/Kepler-data-analysis')

import numpy as np
import matplotlib.pyplot as plt
import ptsa
from ptsa import emd 
from numpy import genfromtxt
from scipy.stats import mode



# Analyzing the energy of the most relevant IMFs for confirmed and FP cases

# Note: Package PTSA is required: https://github.com/compmem/ptsa.git

# For a set of light curves from stars whose transit data have been confirmed 
# as a planet case, and also for false positive cases, this script carries out
# an analysis on using the energy of the most relevant IFMs resulting from the
# Empirical Mode Decomposition (EMD). For computing the most relevant IMFs, the
# approach described in [1] is performed.

# Author: Douglas David Baptista de Souza (douglas@linse.ufsc.br)
                                                          
# References: 

  # [1] IEEE ICASSP 2014 - International Conference on Acoustic, Speech and
    # Signal Processing, "On selecting relevant intrinsic mode functions in em-
    # pirical mode decompositions: an energy-based approach",D. B. Souza et al.
   





###############################################################################
## SELECTING MOST SIGNIFICANT IMFs ACCORDING TO THE CRITERION OF [1] ##########
###############################################################################

# Considered cases:
        
# Star ID 2571238 (confirmed), long cadence time series (quarters 1 to 3)     
# Star ID 3231341 (confirmed), long cadence time series (quarters 1 to 3)                                   

# Star ID: 2166206 (false positive), long cadence time series (quarters 1 to 3)    
# Star ID: 1722276 (false positive), long cadence time series (quarters 1 to 3)    

# This script below reads the light curve data from csv files
exec(open('reading_csv_files_and_computing_IMFs.py').read())

thresh_range = np.linspace(0.01,1,100) # This is the range of threshold considered
# for computing the most relevant IMFs


# Star ID 2571238 - Quarter 1 to 3 (Confirmed)
current_IMFs = IMFs_starID_2571238_confirmed_quarter1
current_signal = yaxis_starID_2571238_confirmed_quarter1
relevant_IMFs(current_IMFs, current_signal, thresh_range)
most_relevant_IMFs_2571238_quarter1 = selected_mode
      
current_IMFs = IMFs_starID_2571238_confirmed_quarter2
current_signal = yaxis_starID_2571238_confirmed_quarter2
relevant_IMFs(current_IMFs, current_signal, thresh_range)
most_relevant_IMFs_2571238_quarter2 = selected_mode

current_IMFs = IMFs_starID_2571238_confirmed_quarter3
current_signal = yaxis_starID_2571238_confirmed_quarter3
relevant_IMFs(current_IMFs, current_signal, thresh_range)
most_relevant_IMFs_2571238_quarter3 = selected_mode

# Star ID 3231341 - Quarter 1 to 3 (Confirmed)
current_IMFs = IMFs_starID_3231341_confirmed_quarter1
current_signal = yaxis_starID_3231341_confirmed_quarter1
relevant_IMFs(current_IMFs, current_signal, thresh_range)
most_relevant_IMFs_3231341_quarter1 = selected_mode
      
current_IMFs = IMFs_starID_3231341_confirmed_quarter2
current_signal = yaxis_starID_3231341_confirmed_quarter2
relevant_IMFs(current_IMFs, current_signal, thresh_range)
most_relevant_IMFs_3231341_quarter2 = selected_mode

current_IMFs = IMFs_starID_3231341_confirmed_quarter3
current_signal = yaxis_starID_3231341_confirmed_quarter3
relevant_IMFs(current_IMFs, current_signal, thresh_range)
most_relevant_IMFs_3231341_quarter3 = selected_mode

# Star ID 2166206 - Quarter 1 to 3 (false_positive)
current_IMFs = IMFs_starID_2166206_false_positive_quarter1
current_signal = yaxis_starID_2166206_false_positive_quarter1
relevant_IMFs(current_IMFs, current_signal, thresh_range)
most_relevant_IMFs_2166206_quarter1 = selected_mode
      
current_IMFs = IMFs_starID_2166206_false_positive_quarter2
current_signal = yaxis_starID_2166206_false_positive_quarter2
relevant_IMFs(current_IMFs, current_signal, thresh_range)
most_relevant_IMFs_2166206_quarter2 = selected_mode

current_IMFs = IMFs_starID_2166206_false_positive_quarter3
current_signal = yaxis_starID_2166206_false_positive_quarter3
relevant_IMFs(current_IMFs, current_signal, thresh_range)
most_relevant_IMFs_2166206_quarter3 = selected_mode

# Star ID 1722276 - Quarter 1 to 3 (false_positive)
current_IMFs = IMFs_starID_1722276_false_positive_quarter1
current_signal = yaxis_starID_1722276_false_positive_quarter1
relevant_IMFs(current_IMFs, current_signal, thresh_range)
most_relevant_IMFs_1722276_quarter1 = selected_mode    
 
current_IMFs = IMFs_starID_1722276_false_positive_quarter2
current_signal = yaxis_starID_1722276_false_positive_quarter2
relevant_IMFs(current_IMFs, current_signal, thresh_range)
most_relevant_IMFs_1722276_quarter2 = selected_mode

current_IMFs = IMFs_starID_1722276_false_positive_quarter3
current_signal = yaxis_starID_1722276_false_positive_quarter3
selected_mode = relevant_IMFs(current_IMFs, current_signal, thresh_range)
most_relevant_IMFs_1722276_quarter3 = selected_mode


         



def relevant_IMFs (current_IMF, current_signal, thresh_range):
        
    # This function executes the energy based approach proposed in [1] for 
    # computing the group of most relevant IMFs obtained from the EMD algorithm
    
    # By Douglas David Baptista de Souza
    
    # [1] IEEE ICASSP 2014 - International Conference on Acoustic, Speech and
    # Signal Processing, "On selecting relevant intrinsic mode functions in em-
    # pirical mode decompositions: an energy-based approach",D. B. Souza et al.
    
    number_of_modes_obtained = current_IMFs.shape[0] # Total number of IMFs obtained from the decomposition
    energy_vector = [] # To store the energy of each IMF
    epsilon_vector = [] # epsilon value of each IMF  
    outside_array_relevant_IMFs_vector = []
    selected_mode = []
                     
  # 1) Computing the energy of each IMF obtained from EMD and computing the 
  # epsilon for the energy-based criterion
                     
    # The residual is stored in the last row of the IMF array                 
    for i in range(0,number_of_modes_obtained-2):
        power_sig_imfs = current_IMFs[i,]**2
        energy_vector.append(power_sig_imfs.sum()) # Storing the energy value of each IMF
        cov_vector = [] # To store the covariance between the i-th and the j-th IMFs  
        for j in range(0,number_of_modes_obtained-1):                     
            if i!=j: cov_matrix = np.cov(current_IMFs[i,],current_IMFs[j,])   
            if i!=j: cov_vector.append(cov_matrix[0,1]) # covariance is the off-diag. terms          
        
        cov_matrix_residual = np.cov(current_IMFs[i,],current_IMFs[number_of_modes_obtained-1,]) # computing the covariance between the residual and the current IMF
        epsilon_vector.append(np.sum(cov_vector) + cov_matrix_residual[0,1])
     

    # 2) Computing the threshold using the energy-criterion
    
    energy_x_p = np.sum((current_signal - np.mean(current_signal))**2)
    epsilon_final = np.sum(epsilon_vector)
    
    
    # 3) For the collection of all possible thresh values, check the most frequent
    # modes, i.e., the most relevant IMFs
    
    #outside_array_relevant_IMFs_vector = np.zeros((np.size(thresh_range),number_of_modes_obtained-2))
    outside_array_relevant_IMFs_vector = []
    
    for i_thresh in range(0,np.size(thresh_range)-1):
       
        thresh = thresh_range[i_thresh]
         
        relevant_IMF_vector = []
        
        # Verifyign the condition for the i-th IMF
        for i in range(0,number_of_modes_obtained-2):
            
            if (np.sqrt(energy_vector[i])*((np.sqrt(energy_x_p)*thresh) - np.sqrt(energy_vector[i]))) < epsilon_final: relevant_IMF_vector.append(1)
            if (np.sqrt(energy_vector[i])*((np.sqrt(energy_x_p)*thresh) - np.sqrt(energy_vector[i]))) > epsilon_final: relevant_IMF_vector.append(0)
               
        outside_array_relevant_IMFs_vector.append(np.transpose(relevant_IMF_vector))
      
    # Computing the most frequent group of IMFs
    selected_mode = mode(outside_array_relevant_IMFs_vector,0)
   
    return(selected_mode.mode)
                                          
                        
