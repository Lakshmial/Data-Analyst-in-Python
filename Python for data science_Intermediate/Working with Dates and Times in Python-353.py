## 1. Introduction ##

from csv import reader
opened_file = open("potus_visitors_2015.csv")
read_file = reader(opened_file)
potus = list(read_file)

# storing column names into potus_header
potus_header = potus[0]
# removing the header and storing the rest to  variable potus
potus = potus[1:]
print(potus_header)
potus[0:3]

## 3. The Datetime Module ##

import datetime as dt

## 4. The Datetime Class ##

import datetime as dt
ibm_founded = dt.datetime(1911,6,16)
man_on_moon = dt.datetime(1969,7,20,20,17)
print(ibm_founded)
print(man_on_moon)

## 5. Using Strptime to Parse Strings as Dates ##

# The `potus` list of lists is available from
# the earlier screen where we created it
date_format = "%m/%d/%y %H:%M"

for row in potus:
    start_date = row[2]
    start_date= dt.datetime.strptime(start_date,date_format)
    row[2]= start_date
    
    

## 6. Using Strftime to format dates ##

visitors_per_month={}
for row in potus:
    start_date = row[2]
    dt_str = dt.datetime.strftime(start_date,"%B, %Y")
    if dt_str not in visitors_per_month:
        visitors_per_month[dt_str]=1
    else:
        visitors_per_month[dt_str]+=1
     
print(visitors_per_month)
      
        

## 7. The Time Class ##

appt_times=[]#Instantiate an empty appt_times list.
for row in potus:#Iterate over each row in the potus list of lists.
    start_time_dt=row[2]#Assign the datetime object stored at index value 2 to a variable.
    start_time_t=start_time_dt.time()#Create a time object from the datetime object.
    appt_times.append(start_time_t)#Append the time object to the appt_times list.
print(appt_times[0:4])

## 8. Comparing time objects ##

min_time = min(appt_times)
max_time = max(appt_times)
print(min_time ,max_time)

## 9. Calculations with Dates and Times ##

dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)
answer_1=dt_2 - dt_1
answer_2 = dt_3 + dt.timedelta(56)
answer_3 = dt_4 - dt.timedelta(seconds=3600)
print(answer_1)
print(answer_2)
print(answer_3)


## 10. Summarizing Appointment Lengths ##

for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date
    
appt_lengths ={}
for row in potus:
    app_start_date = row[2]
    app_end_date  = row[3]
    length = app_end_date - app_start_date
    if length not in appt_lengths:
        appt_lengths[length]=1
    else:
        appt_lengths[length]+=1
min_length = min(appt_lengths)
max_length = max(appt_lengths)
print(min_length)
print(max_length)
print(appt_lengths)



