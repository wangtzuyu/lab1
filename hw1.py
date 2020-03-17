# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv

#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = 'sample_input.csv'

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

#target_data = data[:10]
target_data = list(filter(lambda item: item ['WDSD']!='-999.000' and  item['WDSD'] != '-99.000', data))
data0 = list(filter(lambda item: item ['station_id']=='C0A880', target_data))
data1 = list(filter(lambda item: item ['station_id']=='C0F9A0', target_data))
data2 = list(filter(lambda item: item ['station_id']=='C0G640', target_data))
data3 = list(filter(lambda item: item ['station_id']=='C0R190', target_data))
data4 = list(filter(lambda item: item ['station_id']=='C0X260', target_data))
list0=[]
list1=[]
list2=[]
list3=[]
list4=[]
for i in range (len(data0)):
    list0.append(data0[i]['WDSD'])
for i in range (len(data1)):
    list1.append(data1[i]['WDSD'])
for i in range (len(data2)):
    list2.append(data2[i]['WDSD'])
for i in range (len(data3)):
    list3.append(data3[i]['WDSD'])
for i in range (len(data4)):
    list4.append(data4[i]['WDSD'])    
if (len(list0)<2):
    print("[['C0A880','None'],",end="")
else :
    range0=float(max(list0))-float(min(list0))
    print("[['C0A880',",range0,",",end="")
if (len(list1)<2):
    print("['C0F9A0','None'],",end="")
else :
    range1=float(max(list1))-float(min(list1))
    range11=str(range1)
    print("['C0F9A0',",range11,"],",end="")

if (len(list2)<2):
    print("['C0G640','None'],",end="")
else :
    range2=float(max(list2))-float(min(list2))
    print("['C0G640'],",range2,"],",end="")

if (len(list3)<2):
    print("['C0R190','None'],",end="")
else :
    range3=float(max(list3))-float(min(list3))
    print("['C0R190'],",range3,"],",end="")
if (len(list4)<2):
    print("['C0X260','None']],",end="")
else :
    range4=float(max(list4))-float(min(list4))
    print("['C0X260'],",range4,"]],",end="")


#=======================================


# Part. 4

#=======================================

# Print result

#print(target_data)

