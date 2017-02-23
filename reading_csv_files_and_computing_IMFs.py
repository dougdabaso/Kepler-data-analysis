import numpy as np
import os
import matplotlib.pyplot as plt
import ptsa
from ptsa import emd 
from numpy import genfromtxt

chosen_noise_std = 0.1
chosen_num_realizations = 100


###############################################################################
# READING TIME VECTORS AND DATA FROM CSV FILES ################################
###############################################################################

os.chdir('csv_files_confirmed_fp_stars') # changing to the subfolder where the *.csv files are located

        
## TIME SERIES FOR QUARTER 1 TO 10 FROM COMFIRMED CASES #######################        
        
# Star ID 2571238 (confirmed), long cadence time series
        
xaxis_starID_2571238_confirmed_quarter1 = genfromtxt('star_id_2571238_confirmed_quarter1_xaxis.csv', delimiter = ',')
xaxis_starID_2571238_confirmed_quarter2 = genfromtxt('star_id_2571238_confirmed_quarter2_xaxis.csv', delimiter = ',')
xaxis_starID_2571238_confirmed_quarter3 = genfromtxt('star_id_2571238_confirmed_quarter3_xaxis.csv', delimiter = ',')
#xaxis_starID_2571238_confirmed_quarter4 = genfromtxt('star_id_2571238_confirmed_quarter4_xaxis.csv', delimiter = ',')
#xaxis_starID_2571238_confirmed_quarter5 = genfromtxt('star_id_2571238_confirmed_quarter5_xaxis.csv', delimiter = ',')
#xaxis_starID_2571238_confirmed_quarter6 = genfromtxt('star_id_2571238_confirmed_quarter6_xaxis.csv', delimiter = ',')
#xaxis_starID_2571238_confirmed_quarter7 = genfromtxt('star_id_2571238_confirmed_quarter7_xaxis.csv', delimiter = ',')
#xaxis_starID_2571238_confirmed_quarter8 = genfromtxt('star_id_2571238_confirmed_quarter8_xaxis.csv', delimiter = ',')
#xaxis_starID_2571238_confirmed_quarter9 = genfromtxt('star_id_2571238_confirmed_quarter9_xaxis.csv', delimiter = ',')
#xaxis_starID_2571238_confirmed_quarter10 = genfromtxt('star_id_2571238_confirmed_quarter10_xaxis.csv', delimiter = ',')

yaxis_starID_2571238_confirmed_quarter1 = genfromtxt('star_id_2571238_confirmed_quarter1_yaxis.csv', delimiter = ',')
yaxis_starID_2571238_confirmed_quarter2 = genfromtxt('star_id_2571238_confirmed_quarter2_yaxis.csv', delimiter = ',')
yaxis_starID_2571238_confirmed_quarter3 = genfromtxt('star_id_2571238_confirmed_quarter3_yaxis.csv', delimiter = ',')
#yaxis_starID_2571238_confirmed_quarter4 = genfromtxt('star_id_2571238_confirmed_quarter4_yaxis.csv', delimiter = ',')
#yaxis_starID_2571238_confirmed_quarter5 = genfromtxt('star_id_2571238_confirmed_quarter5_yaxis.csv', delimiter = ',')
#yaxis_starID_2571238_confirmed_quarter6 = genfromtxt('star_id_2571238_confirmed_quarter6_yaxis.csv', delimiter = ',')
#yaxis_starID_2571238_confirmed_quarter7 = genfromtxt('star_id_2571238_confirmed_quarter7_yaxis.csv', delimiter = ',')
#yaxis_starID_2571238_confirmed_quarter8 = genfromtxt('star_id_2571238_confirmed_quarter8_yaxis.csv', delimiter = ',')
#yaxis_starID_2571238_confirmed_quarter9 = genfromtxt('star_id_2571238_confirmed_quarter9_yaxis.csv', delimiter = ',')
#yaxis_starID_2571238_confirmed_quarter10 = genfromtxt('star_id_2571238_confirmed_quarter10_yaxis.csv', delimiter = ',')

print('star ID 2571238 data read from csv file')


# Star ID 3231341 (confirmed), long cadence time series

xaxis_starID_3231341_confirmed_quarter1 = genfromtxt('star_id_3231341_confirmed_quarter1_xaxis.csv', delimiter = ',')
xaxis_starID_3231341_confirmed_quarter2 = genfromtxt('star_id_3231341_confirmed_quarter2_xaxis.csv', delimiter = ',')
xaxis_starID_3231341_confirmed_quarter3 = genfromtxt('star_id_3231341_confirmed_quarter3_xaxis.csv', delimiter = ',')
#xaxis_starID_3231341_confirmed_quarter4 = genfromtxt('star_id_3231341_confirmed_quarter4_xaxis.csv', delimiter = ',')
#xaxis_starID_3231341_confirmed_quarter5 = genfromtxt('star_id_3231341_confirmed_quarter5_xaxis.csv', delimiter = ',')
#xaxis_starID_3231341_confirmed_quarter6 = genfromtxt('star_id_3231341_confirmed_quarter6_xaxis.csv', delimiter = ',')
#xaxis_starID_3231341_confirmed_quarter7 = genfromtxt('star_id_3231341_confirmed_quarter7_xaxis.csv', delimiter = ',')
#xaxis_starID_3231341_confirmed_quarter8 = genfromtxt('star_id_3231341_confirmed_quarter8_xaxis.csv', delimiter = ',')
#xaxis_starID_3231341_confirmed_quarter9 = genfromtxt('star_id_3231341_confirmed_quarter9_xaxis.csv', delimiter = ',')
#xaxis_starID_3231341_confirmed_quarter10 = genfromtxt('star_id_3231341_confirmed_quarter10_xaxis.csv', delimiter = ',')

yaxis_starID_3231341_confirmed_quarter1 = genfromtxt('star_id_3231341_confirmed_quarter1_yaxis.csv', delimiter = ',')
yaxis_starID_3231341_confirmed_quarter2 = genfromtxt('star_id_3231341_confirmed_quarter2_yaxis.csv', delimiter = ',')
yaxis_starID_3231341_confirmed_quarter3 = genfromtxt('star_id_3231341_confirmed_quarter3_yaxis.csv', delimiter = ',')
#yaxis_starID_3231341_confirmed_quarter4 = genfromtxt('star_id_3231341_confirmed_quarter4_yaxis.csv', delimiter = ',')
#yaxis_starID_3231341_confirmed_quarter5 = genfromtxt('star_id_3231341_confirmed_quarter5_yaxis.csv', delimiter = ',')
#yaxis_starID_3231341_confirmed_quarter6 = genfromtxt('star_id_3231341_confirmed_quarter6_yaxis.csv', delimiter = ',')
#yaxis_starID_3231341_confirmed_quarter7 = genfromtxt('star_id_3231341_confirmed_quarter7_yaxis.csv', delimiter = ',')
#yaxis_starID_3231341_confirmed_quarter8 = genfromtxt('star_id_3231341_confirmed_quarter8_yaxis.csv', delimiter = ',')
#yaxis_starID_3231341_confirmed_quarter9 = genfromtxt('star_id_3231341_confirmed_quarter9_yaxis.csv', delimiter = ',')
#yaxis_starID_3231341_confirmed_quarter10 = genfromtxt('star_id_3231341_confirmed_quarter10_yaxis.csv', delimiter = ',')

print('star ID 3231341 data read from csv file')

# Star ID: 3323887 (confirmed), long cadence time series

                   
#xaxis_starID_323887_confirmed_quarter1 = genfromtxt('star_id_323887_confirmed_quarter1_xaxis.csv', delimiter = ',')
#xaxis_starID_323887_confirmed_quarter2 = genfromtxt('star_id_323887_confirmed_quarter2_xaxis.csv', delimiter = ',')
#xaxis_starID_323887_confirmed_quarter3 = genfromtxt('star_id_323887_confirmed_quarter3_xaxis.csv', delimiter = ',')
#xaxis_starID_323887_confirmed_quarter4 = genfromtxt('star_id_323887_confirmed_quarter4_xaxis.csv', delimiter = ',')
#xaxis_starID_323887_confirmed_quarter5 = genfromtxt('star_id_323887_confirmed_quarter5_xaxis.csv', delimiter = ',')
#xaxis_starID_323887_confirmed_quarter6 = genfromtxt('star_id_323887_confirmed_quarter6_xaxis.csv', delimiter = ',')
#xaxis_starID_323887_confirmed_quarter7 = genfromtxt('star_id_323887_confirmed_quarter7_xaxis.csv', delimiter = ',')
#xaxis_starID_323887_confirmed_quarter8 = genfromtxt('star_id_323887_confirmed_quarter8_xaxis.csv', delimiter = ',')
#xaxis_starID_323887_confirmed_quarter9 = genfromtxt('star_id_323887_confirmed_quarter9_xaxis.csv', delimiter = ',')
#xaxis_starID_323887_confirmed_quarter10 = genfromtxt('star_id_323887_confirmed_quarter10_xaxis.csv', delimiter = ',')

#yaxis_starID_323887_confirmed_quarter1 = genfromtxt('star_id_323887_confirmed_quarter1_yaxis.csv', delimiter = ',')
#yaxis_starID_323887_confirmed_quarter2 = genfromtxt('star_id_323887_confirmed_quarter2_yaxis.csv', delimiter = ',')
#yaxis_starID_323887_confirmed_quarter3 = genfromtxt('star_id_323887_confirmed_quarter3_yaxis.csv', delimiter = ',')
#yaxis_starID_323887_confirmed_quarter4 = genfromtxt('star_id_323887_confirmed_quarter4_yaxis.csv', delimiter = ',')
#yaxis_starID_323887_confirmed_quarter5 = genfromtxt('star_id_323887_confirmed_quarter5_yaxis.csv', delimiter = ',')
#yaxis_starID_323887_confirmed_quarter6 = genfromtxt('star_id_323887_confirmed_quarter6_yaxis.csv', delimiter = ',')
#yaxis_starID_323887_confirmed_quarter7 = genfromtxt('star_id_323887_confirmed_quarter7_yaxis.csv', delimiter = ',')
#yaxis_starID_323887_confirmed_quarter8 = genfromtxt('star_id_323887_confirmed_quarter8_yaxis.csv', delimiter = ',')
#yaxis_starID_323887_confirmed_quarter9 = genfromtxt('star_id_323887_confirmed_quarter9_yaxis.csv', delimiter = ',')
#yaxis_starID_323887_confirmed_quarter10 = genfromtxt('star_id_323887_confirmed_quarter10_yaxis.csv', delimiter = ',')

#print('star ID 323887 data read from csv file')


                   
# Star ID: 3632418 (confirmed), long cadence time series

                  
#xaxis_starID_3632418_confirmed_quarter1 = genfromtxt('star_id_3632418_confirmed_quarter1_xaxis.csv', delimiter = ',')
#xaxis_starID_3632418_confirmed_quarter2 = genfromtxt('star_id_3632418_confirmed_quarter2_xaxis.csv', delimiter = ',')
#xaxis_starID_3632418_confirmed_quarter3 = genfromtxt('star_id_3632418_confirmed_quarter3_xaxis.csv', delimiter = ',')
#xaxis_starID_3632418_confirmed_quarter4 = genfromtxt('star_id_3632418_confirmed_quarter4_xaxis.csv', delimiter = ',')
#xaxis_starID_3632418_confirmed_quarter5 = genfromtxt('star_id_3632418_confirmed_quarter5_xaxis.csv', delimiter = ',')
#xaxis_starID_3632418_confirmed_quarter6 = genfromtxt('star_id_3632418_confirmed_quarter6_xaxis.csv', delimiter = ',')
#xaxis_starID_3632418_confirmed_quarter7 = genfromtxt('star_id_3632418_confirmed_quarter7_xaxis.csv', delimiter = ',')
#xaxis_starID_3632418_confirmed_quarter8 = genfromtxt('star_id_3632418_confirmed_quarter8_xaxis.csv', delimiter = ',')
#xaxis_starID_3632418_confirmed_quarter9 = genfromtxt('star_id_3632418_confirmed_quarter9_xaxis.csv', delimiter = ',')
#xaxis_starID_3632418_confirmed_quarter10 = genfromtxt('star_id_3632418_confirmed_quarter10_xaxis.csv', delimiter = ',')

#yaxis_starID_3632418_confirmed_quarter1 = genfromtxt('star_id_3632418_confirmed_quarter1_yaxis.csv', delimiter = ',')
#yaxis_starID_3632418_confirmed_quarter2 = genfromtxt('star_id_3632418_confirmed_quarter2_yaxis.csv', delimiter = ',')
#yaxis_starID_3632418_confirmed_quarter3 = genfromtxt('star_id_3632418_confirmed_quarter3_yaxis.csv', delimiter = ',')
#yaxis_starID_3632418_confirmed_quarter4 = genfromtxt('star_id_3632418_confirmed_quarter4_yaxis.csv', delimiter = ',')
#yaxis_starID_3632418_confirmed_quarter5 = genfromtxt('star_id_3632418_confirmed_quarter5_yaxis.csv', delimiter = ',')
#yaxis_starID_3632418_confirmed_quarter6 = genfromtxt('star_id_3632418_confirmed_quarter6_yaxis.csv', delimiter = ',')
#yaxis_starID_3632418_confirmed_quarter7 = genfromtxt('star_id_3632418_confirmed_quarter7_yaxis.csv', delimiter = ',')
#yaxis_starID_3632418_confirmed_quarter8 = genfromtxt('star_id_3632418_confirmed_quarter8_yaxis.csv', delimiter = ',')
#yaxis_starID_3632418_confirmed_quarter9 = genfromtxt('star_id_3632418_confirmed_quarter9_yaxis.csv', delimiter = ',')
#yaxis_starID_3632418_confirmed_quarter10 = genfromtxt('star_id_3632418_confirmed_quarter10_yaxis.csv', delimiter = ',')

#print('star ID 3632418 data read from csv file')       
                               

## TIME SERIES FOR QUARTER 1 TO 10 FROM FALSE POSITIVE CASES ##################  


# Star ID: 2166206 (false positive), long cadence time series

xaxis_starID_2166206_false_positive_quarter1 = genfromtxt('star_id_2166206_false_positive_quarter1_xaxis.csv', delimiter = ',')
xaxis_starID_2166206_false_positive_quarter2 = genfromtxt('star_id_2166206_false_positive_quarter2_xaxis.csv', delimiter = ',')
xaxis_starID_2166206_false_positive_quarter3 = genfromtxt('star_id_2166206_false_positive_quarter3_xaxis.csv', delimiter = ',')
#xaxis_starID_2166206_false_positive_quarter4 = genfromtxt('star_id_2166206_false_positive_quarter4_xaxis.csv', delimiter = ',')
#xaxis_starID_2166206_false_positive_quarter5 = genfromtxt('star_id_2166206_false_positive_quarter5_xaxis.csv', delimiter = ',')
#xaxis_starID_2166206_false_positive_quarter6 = genfromtxt('star_id_2166206_false_positive_quarter6_xaxis.csv', delimiter = ',')
#xaxis_starID_2166206_false_positive_quarter7 = genfromtxt('star_id_2166206_false_positive_quarter7_xaxis.csv', delimiter = ',')
#xaxis_starID_2166206_false_positive_quarter8 = genfromtxt('star_id_2166206_false_positive_quarter8_xaxis.csv', delimiter = ',')
#xaxis_starID_2166206_false_positive_quarter9 = genfromtxt('star_id_2166206_false_positive_quarter9_xaxis.csv', delimiter = ',')
#xaxis_starID_2166206_false_positive_quarter10 = genfromtxt('star_id_2166206_false_positive_quarter10_xaxis.csv', delimiter = ',')

yaxis_starID_2166206_false_positive_quarter1 = genfromtxt('star_id_2166206_false_positive_quarter1_yaxis.csv', delimiter = ',')
yaxis_starID_2166206_false_positive_quarter2 = genfromtxt('star_id_2166206_false_positive_quarter2_yaxis.csv', delimiter = ',')
yaxis_starID_2166206_false_positive_quarter3 = genfromtxt('star_id_2166206_false_positive_quarter3_yaxis.csv', delimiter = ',')
#yaxis_starID_2166206_false_positive_quarter4 = genfromtxt('star_id_2166206_false_positive_quarter4_yaxis.csv', delimiter = ',')
#yaxis_starID_2166206_false_positive_quarter5 = genfromtxt('star_id_2166206_false_positive_quarter5_yaxis.csv', delimiter = ',')
#yaxis_starID_2166206_false_positive_quarter6 = genfromtxt('star_id_2166206_false_positive_quarter6_yaxis.csv', delimiter = ',')
#yaxis_starID_2166206_false_positive_quarter7 = genfromtxt('star_id_2166206_false_positive_quarter7_yaxis.csv', delimiter = ',')
#yaxis_starID_2166206_false_positive_quarter8 = genfromtxt('star_id_2166206_false_positive_quarter8_yaxis.csv', delimiter = ',')
#yaxis_starID_2166206_false_positive_quarter9 = genfromtxt('star_id_2166206_false_positive_quarter9_yaxis.csv', delimiter = ',')
#yaxis_starID_2166206_false_positive_quarter10 = genfromtxt('star_id_2166206_false_positive_quarter10_yaxis.csv', delimiter = ',')

print('star ID 2166206 data read from csv file')


# Star ID: 1722276 (false positive), long cadence time series
                   
xaxis_starID_1722276_false_positive_quarter1 = genfromtxt('star_id_1722276_false_positive_quarter1_xaxis.csv', delimiter = ',')
xaxis_starID_1722276_false_positive_quarter2 = genfromtxt('star_id_1722276_false_positive_quarter2_xaxis.csv', delimiter = ',')
xaxis_starID_1722276_false_positive_quarter3 = genfromtxt('star_id_1722276_false_positive_quarter3_xaxis.csv', delimiter = ',')
#xaxis_starID_1722276_false_positive_quarter4 = genfromtxt('star_id_1722276_false_positive_quarter4_xaxis.csv', delimiter = ',')
#xaxis_starID_1722276_false_positive_quarter5 = genfromtxt('star_id_1722276_false_positive_quarter5_xaxis.csv', delimiter = ',')
#xaxis_starID_1722276_false_positive_quarter6 = genfromtxt('star_id_1722276_false_positive_quarter6_xaxis.csv', delimiter = ',')
#xaxis_starID_1722276_false_positive_quarter7 = genfromtxt('star_id_1722276_false_positive_quarter7_xaxis.csv', delimiter = ',')
#xaxis_starID_1722276_false_positive_quarter8 = genfromtxt('star_id_1722276_false_positive_quarter8_xaxis.csv', delimiter = ',')
#xaxis_starID_1722276_false_positive_quarter9 = genfromtxt('star_id_1722276_false_positive_quarter9_xaxis.csv', delimiter = ',')
#xaxis_starID_1722276_false_positive_quarter10 = genfromtxt('star_id_1722276_false_positive_quarter10_xaxis.csv', delimiter = ',')

yaxis_starID_1722276_false_positive_quarter1 = genfromtxt('star_id_1722276_false_positive_quarter1_yaxis.csv', delimiter = ',')
yaxis_starID_1722276_false_positive_quarter2 = genfromtxt('star_id_1722276_false_positive_quarter2_yaxis.csv', delimiter = ',')
yaxis_starID_1722276_false_positive_quarter3 = genfromtxt('star_id_1722276_false_positive_quarter3_yaxis.csv', delimiter = ',')
#yaxis_starID_1722276_false_positive_quarter4 = genfromtxt('star_id_1722276_false_positive_quarter4_yaxis.csv', delimiter = ',')
#yaxis_starID_1722276_false_positive_quarter5 = genfromtxt('star_id_1722276_false_positive_quarter5_yaxis.csv', delimiter = ',')
#yaxis_starID_1722276_false_positive_quarter6 = genfromtxt('star_id_1722276_false_positive_quarter6_yaxis.csv', delimiter = ',')
#yaxis_starID_1722276_false_positive_quarter7 = genfromtxt('star_id_1722276_false_positive_quarter7_yaxis.csv', delimiter = ',')
#yaxis_starID_1722276_false_positive_quarter8 = genfromtxt('star_id_1722276_false_positive_quarter8_yaxis.csv', delimiter = ',')
#yaxis_starID_1722276_false_positive_quarter9 = genfromtxt('star_id_1722276_false_positive_quarter9_yaxis.csv', delimiter = ',')
#yaxis_starID_1722276_false_positive_quarter10 = genfromtxt('star_id_1722276_false_positive_quarter10_yaxis.csv', delimiter = ',')

print('star ID 1722276 data read from csv file')
                   

# Star ID: 2157247 (false positive), long cadence time series     

                   
#xaxis_starID_2157247_false_positive_quarter1 = genfromtxt('star_id_2157247_false_positive_quarter1_xaxis.csv', delimiter = ',')
#xaxis_starID_2157247_false_positive_quarter2 = genfromtxt('star_id_2157247_false_positive_quarter2_xaxis.csv', delimiter = ',')
#xaxis_starID_2157247_false_positive_quarter3 = genfromtxt('star_id_2157247_false_positive_quarter3_xaxis.csv', delimiter = ',')
#xaxis_starID_2157247_false_positive_quarter4 = genfromtxt('star_id_2157247_false_positive_quarter4_xaxis.csv', delimiter = ',')
#xaxis_starID_2157247_false_positive_quarter5 = genfromtxt('star_id_2157247_false_positive_quarter5_xaxis.csv', delimiter = ',')
#xaxis_starID_2157247_false_positive_quarter6 = genfromtxt('star_id_2157247_false_positive_quarter6_xaxis.csv', delimiter = ',')
#xaxis_starID_2157247_false_positive_quarter7 = genfromtxt('star_id_2157247_false_positive_quarter7_xaxis.csv', delimiter = ',')
#xaxis_starID_2157247_false_positive_quarter8 = genfromtxt('star_id_2157247_false_positive_quarter8_xaxis.csv', delimiter = ',')
#xaxis_starID_2157247_false_positive_quarter9 = genfromtxt('star_id_2157247_false_positive_quarter9_xaxis.csv', delimiter = ',')
#xaxis_starID_2157247_false_positive_quarter10 = genfromtxt('star_id_2157247_false_positive_quarter10_xaxis.csv', delimiter = ',')

#yaxis_starID_2157247_false_positive_quarter1 = genfromtxt('star_id_2157247_false_positive_quarter1_yaxis.csv', delimiter = ',')
#yaxis_starID_2157247_false_positive_quarter2 = genfromtxt('star_id_2157247_false_positive_quarter2_yaxis.csv', delimiter = ',')
#yaxis_starID_2157247_false_positive_quarter3 = genfromtxt('star_id_2157247_false_positive_quarter3_yaxis.csv', delimiter = ',')
#yaxis_starID_2157247_false_positive_quarter4 = genfromtxt('star_id_2157247_false_positive_quarter4_yaxis.csv', delimiter = ',')
#yaxis_starID_2157247_false_positive_quarter5 = genfromtxt('star_id_2157247_false_positive_quarter5_yaxis.csv', delimiter = ',')
#yaxis_starID_2157247_false_positive_quarter6 = genfromtxt('star_id_2157247_false_positive_quarter6_yaxis.csv', delimiter = ',')
#yaxis_starID_2157247_false_positive_quarter7 = genfromtxt('star_id_2157247_false_positive_quarter7_yaxis.csv', delimiter = ',')
#yaxis_starID_2157247_false_positive_quarter8 = genfromtxt('star_id_2157247_false_positive_quarter8_yaxis.csv', delimiter = ',')
#yaxis_starID_2157247_false_positive_quarter9 = genfromtxt('star_id_2157247_false_positive_quarter9_yaxis.csv', delimiter = ',')
#yaxis_starID_2157247_false_positive_quarter10 = genfromtxt('star_id_2157247_false_positive_quarter10_yaxis.csv', delimiter = ',')

#print('star ID 2157247 data read from csv file')


# Star ID: 2305866 (false positive), long cadence time series       

                   
#xaxis_starID_2305866_false_positive_quarter1 = genfromtxt('star_id_2305866_false_positive_quarter1_xaxis.csv', delimiter = ',')
#xaxis_starID_2305866_false_positive_quarter2 = genfromtxt('star_id_2305866_false_positive_quarter2_xaxis.csv', delimiter = ',')
#xaxis_starID_2305866_false_positive_quarter3 = genfromtxt('star_id_2305866_false_positive_quarter3_xaxis.csv', delimiter = ',')
#xaxis_starID_2305866_false_positive_quarter4 = genfromtxt('star_id_2305866_false_positive_quarter4_xaxis.csv', delimiter = ',')
#xaxis_starID_2305866_false_positive_quarter5 = genfromtxt('star_id_2305866_false_positive_quarter5_xaxis.csv', delimiter = ',')
#xaxis_starID_2305866_false_positive_quarter6 = genfromtxt('star_id_2305866_false_positive_quarter6_xaxis.csv', delimiter = ',')
#xaxis_starID_2305866_false_positive_quarter7 = genfromtxt('star_id_2305866_false_positive_quarter7_xaxis.csv', delimiter = ',')
#xaxis_starID_2305866_false_positive_quarter8 = genfromtxt('star_id_2305866_false_positive_quarter8_xaxis.csv', delimiter = ',')
#xaxis_starID_2305866_false_positive_quarter9 = genfromtxt('star_id_2305866_false_positive_quarter9_xaxis.csv', delimiter = ',')
#xaxis_starID_2305866_false_positive_quarter10 = genfromtxt('star_id_2305866_false_positive_quarter10_xaxis.csv', delimiter = ',')

#yaxis_starID_2305866_false_positive_quarter1 = genfromtxt('star_id_2305866_false_positive_quarter1_yaxis.csv', delimiter = ',')
#yaxis_starID_2305866_false_positive_quarter2 = genfromtxt('star_id_2305866_false_positive_quarter2_yaxis.csv', delimiter = ',')
#yaxis_starID_2305866_false_positive_quarter3 = genfromtxt('star_id_2305866_false_positive_quarter3_yaxis.csv', delimiter = ',')
#yaxis_starID_2305866_false_positive_quarter4 = genfromtxt('star_id_2305866_false_positive_quarter4_yaxis.csv', delimiter = ',')
#yaxis_starID_2305866_false_positive_quarter5 = genfromtxt('star_id_2305866_false_positive_quarter5_yaxis.csv', delimiter = ',')
#yaxis_starID_2305866_false_positive_quarter6 = genfromtxt('star_id_2305866_false_positive_quarter6_yaxis.csv', delimiter = ',')
#yaxis_starID_2305866_false_positive_quarter7 = genfromtxt('star_id_2305866_false_positive_quarter7_yaxis.csv', delimiter = ',')
#yaxis_starID_2305866_false_positive_quarter8 = genfromtxt('star_id_2305866_false_positive_quarter8_yaxis.csv', delimiter = ',')
#yaxis_starID_2305866_false_positive_quarter9 = genfromtxt('star_id_2305866_false_positive_quarter9_yaxis.csv', delimiter = ',')
#yaxis_starID_2305866_false_positive_quarter10 = genfromtxt('star_id_2305866_false_positive_quarter10_yaxis.csv', delimiter = ',')


#print('star ID 2305866 data read from csv file')
                                
os.chdir('../') # returnig to the main folder

        

###############################################################################
# Applying emd to obtain the IMFs of all signals ############################
###############################################################################

        
## TIME SERIES FOR QUARTER 1 TO 10 FROM COMFIRMED CASES #######################        
        
# Star ID 2571238 (confirmed), long cadence time series
        

IMFs_starID_2571238_confirmed_quarter1 = emd.emd(yaxis_starID_2571238_confirmed_quarter1)
IMFs_starID_2571238_confirmed_quarter2 = emd.emd(yaxis_starID_2571238_confirmed_quarter2)
IMFs_starID_2571238_confirmed_quarter3 = emd.emd(yaxis_starID_2571238_confirmed_quarter3)
#IMFs_starID_2571238_confirmed_quarter4 = emd.emd(yaxis_starID_2571238_confirmed_quarter4)
#IMFs_starID_2571238_confirmed_quarter5 = emd.emd(yaxis_starID_2571238_confirmed_quarter5)
#IMFs_starID_2571238_confirmed_quarter6 = emd.emd(yaxis_starID_2571238_confirmed_quarter6)
#IMFs_starID_2571238_confirmed_quarter7 = emd.emd(yaxis_starID_2571238_confirmed_quarter7)
#IMFs_starID_2571238_confirmed_quarter8 = emd.emd(yaxis_starID_2571238_confirmed_quarter8)
#IMFs_starID_2571238_confirmed_quarter9 = emd.emd(yaxis_starID_2571238_confirmed_quarter9)
#IMFs_starID_2571238_confirmed_quarter19 = emd.emd(yaxis_starID_2571238_confirmed_quarter10)

print('IMFs computed for star ID 2571238')


# Star ID 3231341 (confirmed), long cadence time series


IMFs_starID_3231341_confirmed_quarter1 = emd.emd(yaxis_starID_3231341_confirmed_quarter1)
IMFs_starID_3231341_confirmed_quarter2 = emd.emd(yaxis_starID_3231341_confirmed_quarter2)
IMFs_starID_3231341_confirmed_quarter3 = emd.emd(yaxis_starID_3231341_confirmed_quarter3)
#IMFs_starID_3231341_confirmed_quarter4 = emd.emd(yaxis_starID_3231341_confirmed_quarter4)
#IMFs_starID_3231341_confirmed_quarter5 = emd.emd(yaxis_starID_3231341_confirmed_quarter5)
#IMFs_starID_3231341_confirmed_quarter6 = emd.emd(yaxis_starID_3231341_confirmed_quarter6)
#IMFs_starID_3231341_confirmed_quarter7 = emd.emd(yaxis_starID_3231341_confirmed_quarter7)
#IMFs_starID_3231341_confirmed_quarter8 = emd.emd(yaxis_starID_3231341_confirmed_quarter8)
#IMFs_starID_3231341_confirmed_quarter9 = emd.emd(yaxis_starID_3231341_confirmed_quarter9)
#IMFs_starID_3231341_confirmed_quarter19 = emd.emd(yaxis_starID_3231341_confirmed_quarter10)

print('IMFs computed for star ID 3231341')


# Star ID: 3323887 (confirmed), long cadence time series

                   
#IMFs_starID_3323887_confirmed_quarter1 = emd.emd(yaxis_starID_3323887_confirmed_quarter1)
#IMFs_starID_3323887_confirmed_quarter2 = emd.emd(yaxis_starID_3323887_confirmed_quarter2)
#IMFs_starID_3323887_confirmed_quarter3 = emd.emd(yaxis_starID_3323887_confirmed_quarter3)
#IMFs_starID_3323887_confirmed_quarter4 = emd.emd(yaxis_starID_3323887_confirmed_quarter4)
#IMFs_starID_3323887_confirmed_quarter5 = emd.emd(yaxis_starID_3323887_confirmed_quarter5)
#IMFs_starID_3323887_confirmed_quarter6 = emd.emd(yaxis_starID_3323887_confirmed_quarter6)
#IMFs_starID_3323887_confirmed_quarter7 = emd.emd(yaxis_starID_3323887_confirmed_quarter7)
#IMFs_starID_3323887_confirmed_quarter8 = emd.emd(yaxis_starID_3323887_confirmed_quarter8)
#IMFs_starID_3323887_confirmed_quarter9 = emd.emd(yaxis_starID_3323887_confirmed_quarter9)
#IMFs_starID_3323887_confirmed_quarter19 = emd.emd(yaxis_starID_3323887_confirmed_quarter10)

print('IMFs computed for star ID 3323887')

                 
# Star ID: 3632418 (confirmed), long cadence time series

#IMFs_starID_3632418_confirmed_quarter1 = emd.emd(yaxis_starID_3632418_confirmed_quarter1)
#IMFs_starID_3632418_confirmed_quarter2 = emd.emd(yaxis_starID_3632418_confirmed_quarter2)
#IMFs_starID_3632418_confirmed_quarter3 = emd.emd(yaxis_starID_3632418_confirmed_quarter3)
#IMFs_starID_3632418_confirmed_quarter4 = emd.emd(yaxis_starID_3632418_confirmed_quarter4)
#IMFs_starID_3632418_confirmed_quarter5 = emd.emd(yaxis_starID_3632418_confirmed_quarter5)
#IMFs_starID_3632418_confirmed_quarter6 = emd.emd(yaxis_starID_3632418_confirmed_quarter6)
#IMFs_starID_3632418_confirmed_quarter7 = emd.emd(yaxis_starID_3632418_confirmed_quarter7)
#IMFs_starID_3632418_confirmed_quarter8 = emd.emd(yaxis_starID_3632418_confirmed_quarter8)
#IMFs_starID_3632418_confirmed_quarter9 = emd.emd(yaxis_starID_3632418_confirmed_quarter9)
#IMFs_starID_3632418_confirmed_quarter19 = emd.emd(yaxis_starID_3632418_confirmed_quarter10)

print('IMFs computed for star ID 3632418')
                                      

## TIME SERIES FOR QUARTER 1 TO 10 FROM FALSE POSITIVE CASES ##################  


# Star ID: 2166206 (false positive), long cadence time series

IMFs_starID_2166206_false_positive_quarter1 = emd.emd(yaxis_starID_2166206_false_positive_quarter1)
IMFs_starID_2166206_false_positive_quarter2 = emd.emd(yaxis_starID_2166206_false_positive_quarter2)
IMFs_starID_2166206_false_positive_quarter3 = emd.emd(yaxis_starID_2166206_false_positive_quarter3)
#IMFs_starID_2166206_false_positive_quarter4 = emd.emd(yaxis_starID_2166206_false_positive_quarter4)
#IMFs_starID_2166206_false_positive_quarter5 = emd.emd(yaxis_starID_2166206_false_positive_quarter5)
#IMFs_starID_2166206_false_positive_quarter6 = emd.emd(yaxis_starID_2166206_false_positive_quarter6)
#IMFs_starID_2166206_false_positive_quarter7 = emd.emd(yaxis_starID_2166206_false_positive_quarter7)
#IMFs_starID_2166206_false_positive_quarter8 = emd.emd(yaxis_starID_2166206_false_positive_quarter8)
#IMFs_starID_2166206_false_positive_quarter9 = emd.emd(yaxis_starID_2166206_false_positive_quarter9)
#IMFs_starID_2166206_false_positive_quarter10 = emd.emd(yaxis_starID_2166206_false_positive_quarter10)
                                                       
                                       
print('IMFs computed for star ID 2166206')   
              

# Star ID: 1722276 (false positive), long cadence time series
                   
IMFs_starID_1722276_false_positive_quarter1 = emd.emd(yaxis_starID_1722276_false_positive_quarter1)
IMFs_starID_1722276_false_positive_quarter2 = emd.emd(yaxis_starID_1722276_false_positive_quarter2)
IMFs_starID_1722276_false_positive_quarter3 = emd.emd(yaxis_starID_1722276_false_positive_quarter3)
#IMFs_starID_1722276_false_positive_quarter4 = emd.emd(yaxis_starID_1722276_false_positive_quarter4)
#IMFs_starID_1722276_false_positive_quarter5 = emd.emd(yaxis_starID_1722276_false_positive_quarter5)
#IMFs_starID_1722276_false_positive_quarter6 = emd.emd(yaxis_starID_1722276_false_positive_quarter6)
#IMFs_starID_1722276_false_positive_quarter7 = emd.emd(yaxis_starID_1722276_false_positive_quarter7)
#IMFs_starID_1722276_false_positive_quarter8 = emd.emd(yaxis_starID_1722276_false_positive_quarter8)
#IMFs_starID_1722276_false_positive_quarter9 = emd.emd(yaxis_starID_1722276_false_positive_quarter9)
#IMFs_starID_1722276_false_positive_quarter10 = emd.emd(yaxis_starID_1722276_false_positive_quarter10)
                                 
print('IMFs computed for star ID 1722276')                                                                 

# Star ID: 2157247 (false positive), long cadence time series     

#IMFs_starID_2157247_false_positive_quarter1 = emd.emd(yaxis_starID_2157247_false_positive_quarter1)
#IMFs_starID_2157247_false_positive_quarter2 = emd.emd(yaxis_starID_2157247_false_positive_quarter2)
#IMFs_starID_2157247_false_positive_quarter3 = emd.emd(yaxis_starID_2157247_false_positive_quarter3)
#IMFs_starID_2157247_false_positive_quarter4 = emd.emd(yaxis_starID_2157247_false_positive_quarter4)
#IMFs_starID_2157247_false_positive_quarter5 = emd.emd(yaxis_starID_2157247_false_positive_quarter5)
#IMFs_starID_2157247_false_positive_quarter6 = emd.emd(yaxis_starID_2157247_false_positive_quarter6)
#IMFs_starID_2157247_false_positive_quarter7 = emd.emd(yaxis_starID_2157247_false_positive_quarter7)
#IMFs_starID_2157247_false_positive_quarter8 = emd.emd(yaxis_starID_2157247_false_positive_quarter8)
#IMFs_starID_2157247_false_positive_quarter9 = emd.emd(yaxis_starID_2157247_false_positive_quarter9)
#IMFs_starID_2157247_false_positive_quarter10 = emd.emd(yaxis_starID_2157247_false_positive_quarter10)
                                                        
#print('IMFs computed for star ID 2157247')

# Star ID: 2305866 (false positive), long cadence time series       
               
#IMFs_starID_2305866_false_positive_quarter1 = emd.emd(yaxis_starID_2305866_false_positive_quarter1)
#IMFs_starID_2305866_false_positive_quarter2 = emd.emd(yaxis_starID_2305866_false_positive_quarter2)
#IMFs_starID_2305866_false_positive_quarter3 = emd.emd(yaxis_starID_2305866_false_positive_quarter3)
#IMFs_starID_2305866_false_positive_quarter4 = emd.emd(yaxis_starID_2305866_false_positive_quarter4)
#IMFs_starID_2305866_false_positive_quarter5 = emd.emd(yaxis_starID_2305866_false_positive_quarter5)
#IMFs_starID_2305866_false_positive_quarter6 = emd.emd(yaxis_starID_2305866_false_positive_quarter6)
#IMFs_starID_2305866_false_positive_quarter7 = emd.emd(yaxis_starID_2305866_false_positive_quarter7)
#IMFs_starID_2305866_false_positive_quarter8 = emd.emd(yaxis_starID_2305866_false_positive_quarter8)
#IMFs_starID_2305866_false_positive_quarter9 = emd.emd(yaxis_starID_2305866_false_positive_quarter9)
#IMFs_starID_2305866_false_positive_quarter10 = emd.emd(yaxis_starID_2305866_false_positive_quarter10)
                
#print('IMFs computed for star ID 2305866')

###############################################################################

        
        
        
