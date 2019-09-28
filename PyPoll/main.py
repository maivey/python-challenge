'''
**************************************************
********************  PYPOLL   *******************
**************************************************
'''
#import os and csv
import os
import csv

#Create csv path for election_data.csv
csvpath = os.path.join('election_data.csv')

#Read in csvfile:
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    
    #Create header row, exclude header row from calculations by calling next()
    header = next(csvreader)
    
    #Find the first line of data
    first_line = next(csvreader)

    #Create empty list to hold the unique canditates names (complete list of candidates who recieved votes)
    cand_names = []

    #Find the first candidate-- col 2 of first_line
    first_cand = first_line[2]

    #Add the first candidate's name to cand_names list
    cand_names.append(first_cand)
   
   #Create empty list to hold candidates names, to count number of times the candidate was voted for
    cand_list = []
    #*****ACCOUNT FOR FIRST CANDIDATE in list
    cand_list.append(first_cand)

    
    #Initialize variable line_num to calculate the total number of votes cast
    #Since first line has been read in, start from 1
    line_num = 1

    #Loop through lines in the csv file
    for line in csvreader:
        #Add one to line_num each line to count total number of votes cast
        line_num +=1

        #Append the candidates name (col=2) to cand_list
        cand_list.append(line[2])

        #Find canditates names: if the name is not already in cand_names list, append new name to list
        if line[2] not in cand_names:
            cand_names.append(line[2])
            

#Create path for output text file-- "output_ElectionResults.txt"
output_path = os.path.join('output_ElectionResults.txt')

#Open the text file and write the following:
with open(output_path, 'w', newline='') as text:
    #---------------------------------------------------------------
    #Print to the terminal window: Title, Total number of votes cast
    print("Election Results")
    print("---------------------------------------------")
    print(f"Total Votes: {line_num}")
    print("----------------------------------------------")
    #---------------------------------------------------------------

    #Initialize the winner variable to compare each candidate and find the winner
    win_cand = 0

    #Create list of strings to be written to text file: Title, Total number of votes cast
    lines_text = ["Election Results\n",
             "---------------------------------------------\n",
             f"Total Votes: {line_num}\n",
             "---------------------------------------------\n",
             ]
    #Write lines_text to the text file
    text.writelines(lines_text)

    #Loop through each unique candidate names
    for x in cand_names:
        #Count the total number of votes each candidate won
        count_cand = cand_list.count(x)
        #Calculate the percentage of votes each candidate won and round to 3 decimals
        perc_cand = (count_cand/line_num)*100
        perc_cand_3dec = format(perc_cand,'.3f')

        '''-------------------------------------------------
        Print to the terminal window for each candidate: 
        1. The candidate
        2. The percentage of votes won
        3. The total number of votes won'''
        print(f"{x}: {perc_cand_3dec}% ({count_cand})")
        #---------------------------------------------------


        ''' Write to the text file for each candidate: 
        1. The candidate
        2. The percentage of votes won
        3. The total number of votes won'''
        text.write(f"{x}: {perc_cand_3dec}% ({count_cand})\n")

        #Find the winner of the election based on popular vote:
        if perc_cand > win_cand:
            win_cand = perc_cand
            win_name = x
    '''--------------------------------------------------------
    Print the winner to the terminal window: '''
    print("---------------------------------------------")
    print(f"Winner: {win_name}")
    print("---------------------------------------------")
    #----------------------------------------------------------

    #Write the winner to the text file:
    text.write("---------------------------------------------\n")
    text.write(f"Winner: {win_name}\n")
    text.write("---------------------------------------------\n")

