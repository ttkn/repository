@@ -0,0 +1,50 @@
#! python3
# preparing csv file for quickbooks import: rename department to quickbooks expense accounts

import pandas
import numpy as np
from collections import Counter

df = pandas.read_csv(r'C:\Users\Pearl\Downloads\720869792-5913.csv',
                     header=0, sep=',')

df['Department'].replace('WOODSHOP', '7006.W', inplace=True)
df['Department'].replace('CHAIRS', '7006.C', inplace=True)
df['Department'].replace('ASSEMBLY', '7006.A', inplace=True)
df['Department'].replace('SHIPPING', '7006.S', inplace=True)
df['Department'].replace('WOOD BEND', '7006.B', inplace=True)
df['Department'].replace('DRIVERS', '7006.D', inplace=True)
df['Department'].replace('MAINTENANC', '7006.M', inplace=True)
df['Department'].replace('UPHOLSTERY', '7006.U', inplace=True)
df['Department'].replace('ADM/HR', '7001', inplace=True)
df['Department'].replace('PROPS', '7000.P', inplace=True)
df['Department'].replace('LA SHWRM', '7000.B', inplace=True)
df['Department'].replace('MGT', '7002', inplace=True)

ct = Counter(df['employeeID'])
for i in ct:        # i variable: for each key
    if ct[i] == 1:
        ct[i] = ct[i] - 1 
ct2 = +ct
# counts each ID and removes the non-duplicates by setting them at 0
# +ct removes zeroes and negatives from the original ct

def findindex(x):
    return df['employeeID'][df['employeeID'] == x].index[0]
# some_series[some_series == a value].index[0]

def tempest():
    for j in df['employeeID']:
        caliban = findindex(j)
        # duplicates will have multiple index numbers. variable to store and manipulate
        while ct2[j] > 0:
            df.ix[caliban, 'Curr 125'] = 0
            df.ix[caliban, 'Curr EETax'] = 0
            # selects a cell in the dataframe and clears extra deductions from employees
            ct2[j] = ct2[j] - 1
            caliban += 1
            # subtracts 1 from the count after modifying the cells
            # and adds 1 to the index container variable
tempest()

#df.to_excel('2015.5.29 payroll qb import.xlsx', index=False)
