# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '106061102.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))


# Retrive ten data points from the beginning.

target_data = data[:10]
for i in range(0,9,1):
    print(target_data[i]['WDSD'])
print("I am divider")
def reserve(n):
    return  (n!=(-99|-999))==1
    
for i in range(0,9,1):
    templist=filter(reserve,target_data[i]['WDSD'])
    target_data[i]['WDSD']=list(templist)
    print(target_data[i]['WDSD'])

'''
for i in range(0,9,1):
    if (target_data[i]['WDSD']==0.9):
        print('true')
        del target_data[i][2]
    elif target_data[i]['WDSD']==0.000:
        del target_data[i]
    else:
        print(target_data[i]['WDSD'])
        # do nothing
'''


#=======================================


# Part. 4

#=======================================

# Print result

#print(target_data)

