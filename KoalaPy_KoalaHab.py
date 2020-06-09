# KoalaPy Data Series 2019
# for use with CSV files generated
# in ArcGIS or Excel
# prior to use, read KoalaPy Reference Guide

# import pandas module into python

import pandas as pd


# read data in the CSV file
# note headers and data ordering before proceeding, *all data must be 
# formatted to work correctly*
# let kp = koala data to be read

kp = pd.read_csv('KBuff5000mLGA.csv', header = None, names = ['NEW_Site_ID', 'X_Coord', 'Y_Coord', 'UQKoalaHab', 'Area'])

# print data set to check haders are correct and data import is successful

print(kp)

# structure data for analysis purposes
# use aggregation functions

site_suit = kp.groupby(['NEW_Site_ID', 'UQKoalaHab']).agg({'Area':['sum']})

print(site_suit)

# write output CSV for additional analysis or restructuring
# pay attention to naming convention and storage location
# initial output storage will be in the same folder as
# KoalaPy_UQKH_Suit and can be changed afterwards

site_suit.to_csv('KBuff5000mLGAResults.csv')

