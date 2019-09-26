
'''
**************************************************
********************  PYBANK   *******************
**************************************************
'''

#import os, csv
import os
import csv

#Create csv path for budget_data.csv
csvpath = os.path.join('budget_data.csv')


#Create empty list to hold values of diff_amt: the change in profit/losses each month
diff_amt = []

'''Initialize greatest increase and greatest decrease;
set both = 0 to calculate the greatest inc in profits 
and greatest dec in losses over entire period'''
greatest_inc = 0
greatest_dec = 0

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',') 
    
    #Create header row, exclude header row from calculations by calling next()
    header = next(csvreader)
    
    
    #Find the first line, set first amount to the first profit/loss to calculate each change in profit/loss
    first_line = next(csvreader)
    first_amt = int(first_line[1])
    
    '''Initialize variable line_num to calculate number of months(lines):
    1. Set line_num =1 to account for first_amt
    2. **Loop will thus start at line 2** '''
    line_num = 1

    '''Initialize variable tot_amt to calculate the net total amount of "Profit/Losses" over the entire period total
    1. Set tot_amt = first_amt to account for first month's profit/loss value
    2. In for loop, use tot_amt to sum each line (profit/loss value each month)'''
    tot_amt = first_amt

    #Loop through lines in csv file
    for line in csvreader:
        
        #Add each month's profit/loss to total amount
        tot_amt += int(line[1])

        #Increase line_num to count total number of months
        line_num +=1

        #Calculate the change in profit/loss:
            #set next_amt to next profit/loss
        next_amt = int(line[1])

            #append the difference of current line - previous line to diff_amt array
        diff_amt.append(next_amt-first_amt)
        
            #convert the difference to an integer
        diff_amt_int = int(next_amt-first_amt)

            #set the new first_amt to be current line for next line in loop
        first_amt = int(line[1])
        
        '''Find the greatest increase in profits and the greatest decrease in losses:
        1. If the difference is greater than the greatest inc in profits, set the greatest inc to that difference
        2. Extract the month when the greatest increase happens
        3. If the difference is less than the greatest dec in losses, set the greatest dec to that difference
        4. Extract the month when the greatest decrease happens'''
        if diff_amt_int > greatest_inc:
            greatest_inc = diff_amt_int
            greatest_inc_month = line[0]
        elif diff_amt_int < greatest_dec:
            greatest_dec = diff_amt_int
            greatest_dec_month = line[0]
            

#Calculate average change
avg_change = sum(diff_amt)/len(diff_amt)

#Print Financial Analysis results to terminal:
print("Financial Analysis")
print("----------------------------------------------------")
print(f"Total Months: {line_num}")
print(f"Total: ${tot_amt}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})")


#Print Financial Analysis to text file:
output_path = os.path.join('output_FinancialAnalysis.txt')
with open(output_path, 'w', newline='') as text:
    lines_text = ["Financial Analysis",
             "\n",
             "----------------------------------------------------",
             "\n",
             "Total Months: " + str(line_num),
             "\n",
             "Average Change: $" + str(round(avg_change,2)),
             "\n",
             "Greatest Increase in Profits: " + str(greatest_inc_month) + " ($" + str(greatest_inc)+ ")",
             "\n",
             "Greatest Decrease in Profits: " + str(greatest_dec_month) + " ($" + str(greatest_dec)+ ")"
            ]
    text.writelines(lines_text)


