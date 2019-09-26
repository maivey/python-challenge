'''
**************************************************
********************  PYBOSS   *******************
**************************************************
'''

#import os and csv
import os
import csv

#Create csv path for employee_data.csv
csvpath = os.path.join('employee_data.csv')

#Add dictionary of all states and their respective abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    
    #Create header row
    header = next(csvreader)

    #Insert First Name and Last Name to header, at cols 1 and 2
    header.insert(1,"First Name")
    header.insert(2,"Last Name")

    #Remove Name header
    header.remove("Name")

    #Create empty lists for each column: 
    #employee ID, first name, last name, date, social security number, and state
    empID_list = []
    firstName_list = []
    lastName_list = []
    date_list = []
    ssn_list = []
    state_list = []


    #Loop through each line in the csv:
    for line in csvreader:
        # 1:  Append the employee ID to empID_list
        empID_list.append(line[0])

        # 2. Split the whole name into first and last name and append to firstName_list, lastName_list
        first_name, last_name = line[1].split(" ")
        firstName_list.append(first_name)
        lastName_list.append(last_name)

        # 3.  Split the year, month, and day from original file (original format: YYYY-MM-DD)
        year_list, month_list, day_list = line[2].split("-")
        #   Re-format the date to MM/DD/YYYY format
        date_single = month_list + "/" + day_list + "/" + year_list
        #   Append the re-formatted date the the date_list
        date_list.append(date_single)

        # 4.  Split the first 3, next 2, last 4 digits of the social security number (original format: XXX-XX-XXXX)
        first_three, middle_two, last_four = line[3].split("-")
        #   Hide the first 5 numbers, show the last 4 numbers
        ssn_hidden = "***-**-" + last_four
        #   Append the hidden SSN to ssn_list
        ssn_list.append(ssn_hidden)
        
        # 5. Append the state abbreviation matching with the state in col 4 of csv file
        state_list.append(us_state_abbrev[line[4]])
        

#Zip each list of data into a list:
zipped_list = zip(empID_list,firstName_list,lastName_list,date_list,ssn_list,state_list)


#******USING ZIPPED LIST***************
#Create path to write new csv output_PyBoss.csv :
output_path = os.path.join('output_PyBoss.csv')
with open(output_path, 'w', newline='') as csvfile_out:
    writer = csv.writer(csvfile_out)
    #Write the header to the csv file
    writer.writerows([header])
    #Write the zipped list to the csv file
    writer.writerows(zipped_list)