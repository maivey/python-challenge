# python-challenge
# PyBank, PyPoll, PyBoss, PyParagraph

Each folder contains python scripts that take in datasets of various formats, and outputs clean and analyzed information that satisfy the requirements detailed below.

## Prerequisites
This script requires imports of the following:
```code
import os
import csv
```

## PyBank

![Revenue](Images/revenue-per-lead.png)

* Analyzes the financial records of a company. The script uses a financial dataset called [budget_data.csv](PyBank/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`.

* This ![python script](PyBank/main.py) analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* For example, the analysis looks similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, the script prints the analysis to the terminal and exports a text file with the results.

## PyPoll

![Vote-Counting](Images/Vote_counting.png)

* This script is for the following scenario: Helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

* This script uses a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

* This ![python script](PyPoll/main.py) analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* For example, the analysis looks similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

* In addition, the script prints the analysis to the terminal and exports a text file with the results.

## PyBoss

![Boss](Images/boss.jpg)

* This script is for the following scenario: You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. The company recently decided to purchase a new HR system, and unfortunately, the new system requires employee records be stored completely differently. This script helps bridge the gap by converting the employee records to the required format. 

* This ![python script](PyBoss/main.py) does the following:

* Imports the `employee_data.csv` file ![here](PyBoss/employee_data.csv), which currently holds employee records like the below:

```csv
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
```

* Then converts and exports the data to use the following format instead:

```csv
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
```

* In summary, the conversions are as follows:

  * The `Name` column is split into separate `First Name` and `Last Name` columns.

  * The `DOB` data is re-written into `MM/DD/YYYY` format.

  * The `SSN` data should is re-written such that the first five numbers are hidden from view.

  * The `State` data is re-written as simple two-letter abbreviations.

* This helpful link can provide the state abbreviations —[Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).


## PyParagraph

![Language](Images/language.png)

* This script is for the following scenario: As chief linguist at a local learning academy, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.

* This ![python script](PyBoss/main.py) automates the analysis of any such passage using these metrics. It does the following:

* Imports a text file filled with a paragraph of your choosing.

* Assesses the passage for each of the following:

  * Approximate word count

  * Approximate sentence count

  * Approximate letter count (per word)

  * Average sentence length (in words)

* As an example, this passage:

> “Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold.”

...would yield these results:

```output
Paragraph Analysis
-----------------
Approximate Word Count: 122
Approximate Sentence Count: 5
Average Letter Count: 4.6
Average Sentence Length: 24.0
```
