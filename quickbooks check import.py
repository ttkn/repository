# python3
# preparing csv file for quickbooks import: rename department to quickbooks expense accounts

import pandas
import numpy as np
from collections import Counter

df = pandas.read_csv(r'C:\Users\Pearl\Downloads\625850771-1530.csv',
                     header=0, sep=',')
df = df.fillna(0)

df['Deductions'] = (df['Curr AflacAcc'] + df['Curr AflacDen'] + df['Curr AflacHos'] + df['Curr AflacLife'] + df['Curr AflacSh'] + df['Curr 401kL'] + df['Curr 401k'] + df['Curr Bus'] + df['Curr Child'] + df['Curr D125'] + df['Curr Garn'] + df['Curr Garn1'] + df['Curr Garn2'] + df['Curr M125'] + df['Curr Misc'] + df['Curr S-Corp'] + df['Curr V125']) * -1

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

# counts each ID and removes the non-duplicates by setting them at 0
ct = Counter(df['employeeID'])
for i in ct:        # i variable: for each key
    if ct[i] == 1:
        ct[i] = ct[i] - 1 
duplicate_count = +ct
# +ct removes zeroes and negatives from the original ct

def findindex(x):
    return df.employeeID[df['employeeID'] == x].index[0]
# some_series[some_series == a value].index[0]
# returns the index row that the value was in

def tempest():
    for j in df['employeeID']:
        caliban = findindex(j)
        # duplicates will have multiple index numbers. variable to store and manipulate
        while duplicate_count[j] > 0:
            df.ix[caliban, 'Deductions'] = 0
            df.ix[caliban, 'Taxes'] = 0
            # selects a cell in the dataframe and clears extra deductions from employees
            duplicate_count[j] = duplicate_count[j] - 1
            caliban += 1
            # subtracts 1 from the count after modifying the cells
            # and adds 1 to the index container variable
tempest()

#date = time.strptime(df.loc[1][1], '%m/%d/%Y')
#newdate = time.strftime('%Y.%d.%m', date)

df.to_excel('2015.6.12 payroll qb import.xlsx', index=False)
