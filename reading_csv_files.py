import numpy as np
import matplotlib.pyplot as plt
import ptsa
from ptsa import emd 
from numpy import genfromtxt

# Reading time vectors

os.chdir('csv_files_confirmed_fp_stars') # changing to the subfolder where the *.csv files are located

        
## TIME SERIES FOR QUARTER 1 TO 10 FROM COMFIRMED CASES #######################        
        
# Star ID 2571238 (confirmed), long cadence time series
        
xaxis_starID_2571238_confirmed_quarter1 = genfromtxt('star_id_2571238_confirmed_quarter1_xaxis.csv', delimiter = ',')
xaxis_starID_2571238_confirmed_quarter2 = genfromtxt('star_id_2571238_confirmed_quarter2_xaxis.csv', delimiter = ',')
xaxis_starID_2571238_confirmed_quarter3 = genfromtxt('star_id_2571238_confirmed_quarter3_xaxis.csv', delimiter = ',')
xaxis_starID_2571238_confirmed_quarter4 = genfromtxt('star_id_2571238_confirmed_quarter4_xaxis.csv', delimiter = ',')
xaxis_starID_2571238_confirmed_quarter5 = genfromtxt('star_id_2571238_confirmed_quarter5_xaxis.csv', delimiter = ',')
xaxis_starID_2571238_confirmed_quarter6 = genfromtxt('star_id_2571238_confirmed_quarter6_xaxis.csv', delimiter = ',')
xaxis_starID_2571238_confirmed_quarter7 = genfromtxt('star_id_2571238_confirmed_quarter7_xaxis.csv', delimiter = ',')
xaxis_starID_2571238_confirmed_quarter8 = genfromtxt('star_id_2571238_confirmed_quarter8_xaxis.csv', delimiter = ',')
xaxis_starID_2571238_confirmed_quarter9 = genfromtxt('star_id_2571238_confirmed_quarter9_xaxis.csv', delimiter = ',')
xaxis_starID_2571238_confirmed_quarter10 = genfromtxt('star_id_2571238_confirmed_quarter10_xaxis.csv', delimiter = ',')

yaxis_starID_2571238_confirmed_quarter1 = genfromtxt('star_id_2571238_confirmed_quarter1_yaxis.csv', delimiter = ',')
yaxis_starID_2571238_confirmed_quarter2 = genfromtxt('star_id_2571238_confirmed_quarter2_yaxis.csv', delimiter = ',')
yaxis_starID_2571238_confirmed_quarter3 = genfromtxt('star_id_2571238_confirmed_quarter3_yaxis.csv', delimiter = ',')
yaxis_starID_2571238_confirmed_quarter4 = genfromtxt('star_id_2571238_confirmed_quarter4_yaxis.csv', delimiter = ',')
yaxis_starID_2571238_confirmed_quarter5 = genfromtxt('star_id_2571238_confirmed_quarter5_yaxis.csv', delimiter = ',')
yaxis_starID_2571238_confirmed_quarter6 = genfromtxt('star_id_2571238_confirmed_quarter6_yaxis.csv', delimiter = ',')
yaxis_starID_2571238_confirmed_quarter7 = genfromtxt('star_id_2571238_confirmed_quarter7_yaxis.csv', delimiter = ',')
yaxis_starID_2571238_confirmed_quarter8 = genfromtxt('star_id_2571238_confirmed_quarter8_yaxis.csv', delimiter = ',')
yaxis_starID_2571238_confirmed_quarter9 = genfromtxt('star_id_2571238_confirmed_quarter9_yaxis.csv', delimiter = ',')
yaxis_starID_2571238_confirmed_quarter10 = genfromtxt('star_id_2571238_confirmed_quarter10_yaxis.csv', delimiter = ',')


# Star ID 3231341 (confirmed), long cadence time series

xaxis_starID_3231341_confirmed_quarter1 = genfromtxt('star_id_3231341_confirmed_quarter1_xaxis.csv', delimiter = ',')
xaxis_starID_3231341_confirmed_quarter2 = genfromtxt('star_id_3231341_confirmed_quarter2_xaxis.csv', delimiter = ',')
xaxis_starID_3231341_confirmed_quarter3 = genfromtxt('star_id_3231341_confirmed_quarter3_xaxis.csv', delimiter = ',')
xaxis_starID_3231341_confirmed_quarter4 = genfromtxt('star_id_3231341_confirmed_quarter4_xaxis.csv', delimiter = ',')
xaxis_starID_3231341_confirmed_quarter5 = genfromtxt('star_id_3231341_confirmed_quarter5_xaxis.csv', delimiter = ',')
xaxis_starID_3231341_confirmed_quarter6 = genfromtxt('star_id_3231341_confirmed_quarter6_xaxis.csv', delimiter = ',')
xaxis_starID_3231341_confirmed_quarter7 = genfromtxt('star_id_3231341_confirmed_quarter7_xaxis.csv', delimiter = ',')
xaxis_starID_3231341_confirmed_quarter8 = genfromtxt('star_id_3231341_confirmed_quarter8_xaxis.csv', delimiter = ',')
xaxis_starID_3231341_confirmed_quarter9 = genfromtxt('star_id_3231341_confirmed_quarter9_xaxis.csv', delimiter = ',')
xaxis_starID_3231341_confirmed_quarter10 = genfromtxt('star_id_3231341_confirmed_quarter10_xaxis.csv', delimiter = ',')

yaxis_starID_3231341_confirmed_quarter1 = genfromtxt('star_id_3231341_confirmed_quarter1_yaxis.csv', delimiter = ',')
yaxis_starID_3231341_confirmed_quarter2 = genfromtxt('star_id_3231341_confirmed_quarter2_yaxis.csv', delimiter = ',')
yaxis_starID_3231341_confirmed_quarter3 = genfromtxt('star_id_3231341_confirmed_quarter3_yaxis.csv', delimiter = ',')
yaxis_starID_3231341_confirmed_quarter4 = genfromtxt('star_id_3231341_confirmed_quarter4_yaxis.csv', delimiter = ',')
yaxis_starID_3231341_confirmed_quarter5 = genfromtxt('star_id_3231341_confirmed_quarter5_yaxis.csv', delimiter = ',')
yaxis_starID_3231341_confirmed_quarter6 = genfromtxt('star_id_3231341_confirmed_quarter6_yaxis.csv', delimiter = ',')
yaxis_starID_3231341_confirmed_quarter7 = genfromtxt('star_id_3231341_confirmed_quarter7_yaxis.csv', delimiter = ',')
yaxis_starID_3231341_confirmed_quarter8 = genfromtxt('star_id_3231341_confirmed_quarter8_yaxis.csv', delimiter = ',')
yaxis_starID_3231341_confirmed_quarter9 = genfromtxt('star_id_3231341_confirmed_quarter9_yaxis.csv', delimiter = ',')
yaxis_starID_3231341_confirmed_quarter10 = genfromtxt('star_id_3231341_confirmed_quarter10_yaxis.csv', delimiter = ',')


# Star ID: 3323887 (confirmed), long cadence time series

                   
xaxis_starID_323887_confirmed_quarter1 = genfromtxt('star_id_323887_confirmed_quarter1_xaxis.csv', delimiter = ',')
xaxis_starID_323887_confirmed_quarter2 = genfromtxt('star_id_323887_confirmed_quarter2_xaxis.csv', delimiter = ',')
xaxis_starID_323887_confirmed_quarter3 = genfromtxt('star_id_323887_confirmed_quarter3_xaxis.csv', delimiter = ',')
xaxis_starID_323887_confirmed_quarter4 = genfromtxt('star_id_323887_confirmed_quarter4_xaxis.csv', delimiter = ',')
xaxis_starID_323887_confirmed_quarter5 = genfromtxt('star_id_323887_confirmed_quarter5_xaxis.csv', delimiter = ',')
xaxis_starID_323887_confirmed_quarter6 = genfromtxt('star_id_323887_confirmed_quarter6_xaxis.csv', delimiter = ',')
xaxis_starID_323887_confirmed_quarter7 = genfromtxt('star_id_323887_confirmed_quarter7_xaxis.csv', delimiter = ',')
xaxis_starID_323887_confirmed_quarter8 = genfromtxt('star_id_323887_confirmed_quarter8_xaxis.csv', delimiter = ',')
xaxis_starID_323887_confirmed_quarter9 = genfromtxt('star_id_323887_confirmed_quarter9_xaxis.csv', delimiter = ',')
xaxis_starID_323887_confirmed_quarter10 = genfromtxt('star_id_323887_confirmed_quarter10_xaxis.csv', delimiter = ',')

yaxis_starID_323887_confirmed_quarter1 = genfromtxt('star_id_323887_confirmed_quarter1_yaxis.csv', delimiter = ',')
yaxis_starID_323887_confirmed_quarter2 = genfromtxt('star_id_323887_confirmed_quarter2_yaxis.csv', delimiter = ',')
yaxis_starID_323887_confirmed_quarter3 = genfromtxt('star_id_323887_confirmed_quarter3_yaxis.csv', delimiter = ',')
yaxis_starID_323887_confirmed_quarter4 = genfromtxt('star_id_323887_confirmed_quarter4_yaxis.csv', delimiter = ',')
yaxis_starID_323887_confirmed_quarter5 = genfromtxt('star_id_323887_confirmed_quarter5_yaxis.csv', delimiter = ',')
yaxis_starID_323887_confirmed_quarter6 = genfromtxt('star_id_323887_confirmed_quarter6_yaxis.csv', delimiter = ',')
yaxis_starID_323887_confirmed_quarter7 = genfromtxt('star_id_323887_confirmed_quarter7_yaxis.csv', delimiter = ',')
yaxis_starID_323887_confirmed_quarter8 = genfromtxt('star_id_323887_confirmed_quarter8_yaxis.csv', delimiter = ',')
yaxis_starID_323887_confirmed_quarter9 = genfromtxt('star_id_323887_confirmed_quarter9_yaxis.csv', delimiter = ',')
yaxis_starID_323887_confirmed_quarter10 = genfromtxt('star_id_323887_confirmed_quarter10_yaxis.csv', delimiter = ',')


                   
# Star ID: 3632418 (confirmed), long cadence time series

                  
xaxis_starID_3632418_confirmed_quarter1 = genfromtxt('star_id_3632418_confirmed_quarter1_xaxis.csv', delimiter = ',')
xaxis_starID_3632418_confirmed_quarter2 = genfromtxt('star_id_3632418_confirmed_quarter2_xaxis.csv', delimiter = ',')
xaxis_starID_3632418_confirmed_quarter3 = genfromtxt('star_id_3632418_confirmed_quarter3_xaxis.csv', delimiter = ',')
xaxis_starID_3632418_confirmed_quarter4 = genfromtxt('star_id_3632418_confirmed_quarter4_xaxis.csv', delimiter = ',')
xaxis_starID_3632418_confirmed_quarter5 = genfromtxt('star_id_3632418_confirmed_quarter5_xaxis.csv', delimiter = ',')
xaxis_starID_3632418_confirmed_quarter6 = genfromtxt('star_id_3632418_confirmed_quarter6_xaxis.csv', delimiter = ',')
xaxis_starID_3632418_confirmed_quarter7 = genfromtxt('star_id_3632418_confirmed_quarter7_xaxis.csv', delimiter = ',')
xaxis_starID_3632418_confirmed_quarter8 = genfromtxt('star_id_3632418_confirmed_quarter8_xaxis.csv', delimiter = ',')
xaxis_starID_3632418_confirmed_quarter9 = genfromtxt('star_id_3632418_confirmed_quarter9_xaxis.csv', delimiter = ',')
xaxis_starID_3632418_confirmed_quarter10 = genfromtxt('star_id_3632418_confirmed_quarter10_xaxis.csv', delimiter = ',')

yaxis_starID_3632418_confirmed_quarter1 = genfromtxt('star_id_3632418_confirmed_quarter1_yaxis.csv', delimiter = ',')
yaxis_starID_3632418_confirmed_quarter2 = genfromtxt('star_id_3632418_confirmed_quarter2_yaxis.csv', delimiter = ',')
yaxis_starID_3632418_confirmed_quarter3 = genfromtxt('star_id_3632418_confirmed_quarter3_yaxis.csv', delimiter = ',')
yaxis_starID_3632418_confirmed_quarter4 = genfromtxt('star_id_3632418_confirmed_quarter4_yaxis.csv', delimiter = ',')
yaxis_starID_3632418_confirmed_quarter5 = genfromtxt('star_id_3632418_confirmed_quarter5_yaxis.csv', delimiter = ',')
yaxis_starID_3632418_confirmed_quarter6 = genfromtxt('star_id_3632418_confirmed_quarter6_yaxis.csv', delimiter = ',')
yaxis_starID_3632418_confirmed_quarter7 = genfromtxt('star_id_3632418_confirmed_quarter7_yaxis.csv', delimiter = ',')
yaxis_starID_3632418_confirmed_quarter8 = genfromtxt('star_id_3632418_confirmed_quarter8_yaxis.csv', delimiter = ',')
yaxis_starID_3632418_confirmed_quarter9 = genfromtxt('star_id_3632418_confirmed_quarter9_yaxis.csv', delimiter = ',')
yaxis_starID_3632418_confirmed_quarter10 = genfromtxt('star_id_3632418_confirmed_quarter10_yaxis.csv', delimiter = ',')

                                      

## TIME SERIES FOR QUARTER 1 TO 10 FROM FALSE POSITIVE CASES ##################  


# Star ID: 2166206 (false positive), long cadence time series

xaxis_starID_2166206_false_positive_quarter1 = genfromtxt('star_id_2166206_false_positive_quarter1_xaxis.csv', delimiter = ',')
xaxis_starID_2166206_false_positive_quarter2 = genfromtxt('star_id_2166206_false_positive_quarter2_xaxis.csv', delimiter = ',')
xaxis_starID_2166206_false_positive_quarter3 = genfromtxt('star_id_2166206_false_positive_quarter3_xaxis.csv', delimiter = ',')
xaxis_starID_2166206_false_positive_quarter4 = genfromtxt('star_id_2166206_false_positive_quarter4_xaxis.csv', delimiter = ',')
xaxis_starID_2166206_false_positive_quarter5 = genfromtxt('star_id_2166206_false_positive_quarter5_xaxis.csv', delimiter = ',')
xaxis_starID_2166206_false_positive_quarter6 = genfromtxt('star_id_2166206_false_positive_quarter6_xaxis.csv', delimiter = ',')
xaxis_starID_2166206_false_positive_quarter7 = genfromtxt('star_id_2166206_false_positive_quarter7_xaxis.csv', delimiter = ',')
xaxis_starID_2166206_false_positive_quarter8 = genfromtxt('star_id_2166206_false_positive_quarter8_xaxis.csv', delimiter = ',')
xaxis_starID_2166206_false_positive_quarter9 = genfromtxt('star_id_2166206_false_positive_quarter9_xaxis.csv', delimiter = ',')
xaxis_starID_2166206_false_positive_quarter10 = genfromtxt('star_id_2166206_false_positive_quarter10_xaxis.csv', delimiter = ',')

yaxis_starID_2166206_false_positive_quarter1 = genfromtxt('star_id_2166206_false_positive_quarter1_yaxis.csv', delimiter = ',')
yaxis_starID_2166206_false_positive_quarter2 = genfromtxt('star_id_2166206_false_positive_quarter2_yaxis.csv', delimiter = ',')
yaxis_starID_2166206_false_positive_quarter3 = genfromtxt('star_id_2166206_false_positive_quarter3_yaxis.csv', delimiter = ',')
yaxis_starID_2166206_false_positive_quarter4 = genfromtxt('star_id_2166206_false_positive_quarter4_yaxis.csv', delimiter = ',')
yaxis_starID_2166206_false_positive_quarter5 = genfromtxt('star_id_2166206_false_positive_quarter5_yaxis.csv', delimiter = ',')
yaxis_starID_2166206_false_positive_quarter6 = genfromtxt('star_id_2166206_false_positive_quarter6_yaxis.csv', delimiter = ',')
yaxis_starID_2166206_false_positive_quarter7 = genfromtxt('star_id_2166206_false_positive_quarter7_yaxis.csv', delimiter = ',')
yaxis_starID_2166206_false_positive_quarter8 = genfromtxt('star_id_2166206_false_positive_quarter8_yaxis.csv', delimiter = ',')
yaxis_starID_2166206_false_positive_quarter9 = genfromtxt('star_id_2166206_false_positive_quarter9_yaxis.csv', delimiter = ',')
yaxis_starID_2166206_false_positive_quarter10 = genfromtxt('star_id_2166206_false_positive_quarter10_yaxis.csv', delimiter = ',')



# Star ID: 1722276 (false positive), long cadence time series
                   
xaxis_starID_1722276_false_positive_quarter1 = genfromtxt('star_id_1722276_false_positive_quarter1_xaxis.csv', delimiter = ',')
xaxis_starID_1722276_false_positive_quarter2 = genfromtxt('star_id_1722276_false_positive_quarter2_xaxis.csv', delimiter = ',')
xaxis_starID_1722276_false_positive_quarter3 = genfromtxt('star_id_1722276_false_positive_quarter3_xaxis.csv', delimiter = ',')
xaxis_starID_1722276_false_positive_quarter4 = genfromtxt('star_id_1722276_false_positive_quarter4_xaxis.csv', delimiter = ',')
xaxis_starID_1722276_false_positive_quarter5 = genfromtxt('star_id_1722276_false_positive_quarter5_xaxis.csv', delimiter = ',')
xaxis_starID_1722276_false_positive_quarter6 = genfromtxt('star_id_1722276_false_positive_quarter6_xaxis.csv', delimiter = ',')
xaxis_starID_1722276_false_positive_quarter7 = genfromtxt('star_id_1722276_false_positive_quarter7_xaxis.csv', delimiter = ',')
xaxis_starID_1722276_false_positive_quarter8 = genfromtxt('star_id_1722276_false_positive_quarter8_xaxis.csv', delimiter = ',')
xaxis_starID_1722276_false_positive_quarter9 = genfromtxt('star_id_1722276_false_positive_quarter9_xaxis.csv', delimiter = ',')
xaxis_starID_1722276_false_positive_quarter10 = genfromtxt('star_id_1722276_false_positive_quarter10_xaxis.csv', delimiter = ',')

yaxis_starID_1722276_false_positive_quarter1 = genfromtxt('star_id_1722276_false_positive_quarter1_yaxis.csv', delimiter = ',')
yaxis_starID_1722276_false_positive_quarter2 = genfromtxt('star_id_1722276_false_positive_quarter2_yaxis.csv', delimiter = ',')
yaxis_starID_1722276_false_positive_quarter3 = genfromtxt('star_id_1722276_false_positive_quarter3_yaxis.csv', delimiter = ',')
yaxis_starID_1722276_false_positive_quarter4 = genfromtxt('star_id_1722276_false_positive_quarter4_yaxis.csv', delimiter = ',')
yaxis_starID_1722276_false_positive_quarter5 = genfromtxt('star_id_1722276_false_positive_quarter5_yaxis.csv', delimiter = ',')
yaxis_starID_1722276_false_positive_quarter6 = genfromtxt('star_id_1722276_false_positive_quarter6_yaxis.csv', delimiter = ',')
yaxis_starID_1722276_false_positive_quarter7 = genfromtxt('star_id_1722276_false_positive_quarter7_yaxis.csv', delimiter = ',')
yaxis_starID_1722276_false_positive_quarter8 = genfromtxt('star_id_1722276_false_positive_quarter8_yaxis.csv', delimiter = ',')
yaxis_starID_1722276_false_positive_quarter9 = genfromtxt('star_id_1722276_false_positive_quarter9_yaxis.csv', delimiter = ',')
yaxis_starID_1722276_false_positive_quarter10 = genfromtxt('star_id_1722276_false_positive_quarter10_yaxis.csv', delimiter = ',')

                   

# Star ID: 2157247 (false positive), long cadence time series     

                   
xaxis_starID_2157247_false_positive_quarter1 = genfromtxt('star_id_2157247_false_positive_quarter1_xaxis.csv', delimiter = ',')
xaxis_starID_2157247_false_positive_quarter2 = genfromtxt('star_id_2157247_false_positive_quarter2_xaxis.csv', delimiter = ',')
xaxis_starID_2157247_false_positive_quarter3 = genfromtxt('star_id_2157247_false_positive_quarter3_xaxis.csv', delimiter = ',')
xaxis_starID_2157247_false_positive_quarter4 = genfromtxt('star_id_2157247_false_positive_quarter4_xaxis.csv', delimiter = ',')
xaxis_starID_2157247_false_positive_quarter5 = genfromtxt('star_id_2157247_false_positive_quarter5_xaxis.csv', delimiter = ',')
xaxis_starID_2157247_false_positive_quarter6 = genfromtxt('star_id_2157247_false_positive_quarter6_xaxis.csv', delimiter = ',')
xaxis_starID_2157247_false_positive_quarter7 = genfromtxt('star_id_2157247_false_positive_quarter7_xaxis.csv', delimiter = ',')
xaxis_starID_2157247_false_positive_quarter8 = genfromtxt('star_id_2157247_false_positive_quarter8_xaxis.csv', delimiter = ',')
xaxis_starID_2157247_false_positive_quarter9 = genfromtxt('star_id_2157247_false_positive_quarter9_xaxis.csv', delimiter = ',')
xaxis_starID_2157247_false_positive_quarter10 = genfromtxt('star_id_2157247_false_positive_quarter10_xaxis.csv', delimiter = ',')

yaxis_starID_2157247_false_positive_quarter1 = genfromtxt('star_id_2157247_false_positive_quarter1_yaxis.csv', delimiter = ',')
yaxis_starID_2157247_false_positive_quarter2 = genfromtxt('star_id_2157247_false_positive_quarter2_yaxis.csv', delimiter = ',')
yaxis_starID_2157247_false_positive_quarter3 = genfromtxt('star_id_2157247_false_positive_quarter3_yaxis.csv', delimiter = ',')
yaxis_starID_2157247_false_positive_quarter4 = genfromtxt('star_id_2157247_false_positive_quarter4_yaxis.csv', delimiter = ',')
yaxis_starID_2157247_false_positive_quarter5 = genfromtxt('star_id_2157247_false_positive_quarter5_yaxis.csv', delimiter = ',')
yaxis_starID_2157247_false_positive_quarter6 = genfromtxt('star_id_2157247_false_positive_quarter6_yaxis.csv', delimiter = ',')
yaxis_starID_2157247_false_positive_quarter7 = genfromtxt('star_id_2157247_false_positive_quarter7_yaxis.csv', delimiter = ',')
yaxis_starID_2157247_false_positive_quarter8 = genfromtxt('star_id_2157247_false_positive_quarter8_yaxis.csv', delimiter = ',')
yaxis_starID_2157247_false_positive_quarter9 = genfromtxt('star_id_2157247_false_positive_quarter9_yaxis.csv', delimiter = ',')
yaxis_starID_2157247_false_positive_quarter10 = genfromtxt('star_id_2157247_false_positive_quarter10_yaxis.csv', delimiter = ',')


# Star ID: 2305866 (false positive), long cadence time series       

                   
xaxis_starID_2305866_false_positive_quarter1 = genfromtxt('star_id_2305866_false_positive_quarter1_xaxis.csv', delimiter = ',')
xaxis_starID_2305866_false_positive_quarter2 = genfromtxt('star_id_2305866_false_positive_quarter2_xaxis.csv', delimiter = ',')
xaxis_starID_2305866_false_positive_quarter3 = genfromtxt('star_id_2305866_false_positive_quarter3_xaxis.csv', delimiter = ',')
xaxis_starID_2305866_false_positive_quarter4 = genfromtxt('star_id_2305866_false_positive_quarter4_xaxis.csv', delimiter = ',')
xaxis_starID_2305866_false_positive_quarter5 = genfromtxt('star_id_2305866_false_positive_quarter5_xaxis.csv', delimiter = ',')
xaxis_starID_2305866_false_positive_quarter6 = genfromtxt('star_id_2305866_false_positive_quarter6_xaxis.csv', delimiter = ',')
xaxis_starID_2305866_false_positive_quarter7 = genfromtxt('star_id_2305866_false_positive_quarter7_xaxis.csv', delimiter = ',')
xaxis_starID_2305866_false_positive_quarter8 = genfromtxt('star_id_2305866_false_positive_quarter8_xaxis.csv', delimiter = ',')
xaxis_starID_2305866_false_positive_quarter9 = genfromtxt('star_id_2305866_false_positive_quarter9_xaxis.csv', delimiter = ',')
xaxis_starID_2305866_false_positive_quarter10 = genfromtxt('star_id_2305866_false_positive_quarter10_xaxis.csv', delimiter = ',')

yaxis_starID_2305866_false_positive_quarter1 = genfromtxt('star_id_2305866_false_positive_quarter1_yaxis.csv', delimiter = ',')
yaxis_starID_2305866_false_positive_quarter2 = genfromtxt('star_id_2305866_false_positive_quarter2_yaxis.csv', delimiter = ',')
yaxis_starID_2305866_false_positive_quarter3 = genfromtxt('star_id_2305866_false_positive_quarter3_yaxis.csv', delimiter = ',')
yaxis_starID_2305866_false_positive_quarter4 = genfromtxt('star_id_2305866_false_positive_quarter4_yaxis.csv', delimiter = ',')
yaxis_starID_2305866_false_positive_quarter5 = genfromtxt('star_id_2305866_false_positive_quarter5_yaxis.csv', delimiter = ',')
yaxis_starID_2305866_false_positive_quarter6 = genfromtxt('star_id_2305866_false_positive_quarter6_yaxis.csv', delimiter = ',')
yaxis_starID_2305866_false_positive_quarter7 = genfromtxt('star_id_2305866_false_positive_quarter7_yaxis.csv', delimiter = ',')
yaxis_starID_2305866_false_positive_quarter8 = genfromtxt('star_id_2305866_false_positive_quarter8_yaxis.csv', delimiter = ',')
yaxis_starID_2305866_false_positive_quarter9 = genfromtxt('star_id_2305866_false_positive_quarter9_yaxis.csv', delimiter = ',')
yaxis_starID_2305866_false_positive_quarter10 = genfromtxt('star_id_2305866_false_positive_quarter10_yaxis.csv', delimiter = ',')

                   
                  

os.chdir('../') # returnig to the main folder
