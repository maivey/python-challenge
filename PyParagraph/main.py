'''
**************************************************
*****************  PYPARAGRAPH  ******************
**************************************************
'''
#import os and re
import os
import re

#--------------------------------------------------------
#Uncomment what passage you want to read in:
output_path = os.path.join('raw_data','passage_text.txt') 
#output_path = os.path.join('raw_data','paragraph_1.txt') 
#output_path = os.path.join('raw_data','paragraph_2.txt') 
#--------------------------------------------------------

with open(output_path, 'r', newline='') as text:
    paragraph = text.read()

#Split the sentences
split_sentence = re.split("(?<=[.!?]) +", paragraph)

#Initialize sent_len = 0 to calculate the sentence length
sent_len = 0

#Create empty list sent_hard to fill in loop
sent_hard = []

for test in split_sentence:
    #Split sentences where new line
    test_sent = test.split('\n\n')

    #Append new list sent_hard with no new lines '\n\n'
    sent_hard.append(test_sent)

    #Count number of sentences in each list in split_sentence
    sent_len += len(test_sent)

#Count number of sentences directly from split_sentence
#**Will not work on paragraph_2.txt***
#sentence_count = len(split_sentence)



#Create empty list for counting number of words per sentence
sent_count = []
#Count words per sentence:
# Loop through list of sentences
for sent in sent_hard:
    #Loop through each sentence in list of sentences
    for sent_indiv in sent:
        #Split sentence into individual words
        word_per_sent = str(sent_indiv).split()
        #Count number of words per sentence
        sent_count.append(len(word_per_sent))

#Calculate average words per sentence
avg_words_perSent = round(sum(sent_count)/len(sent_count),2)


#Count number of words:
split_word = paragraph.split()

word_count = len(split_word)


#Count number of characters per word:
tot_char_count = 0
char_counts = []
for word in split_word:
    # ***This counts hyphenates words and words with apostrophies as one single word***
    #Remove all non-alphabetical characters, store in new_word variable
    new_word = re.sub('[^A-Za-z0-9]+', '', word)
    #Append the length of the word (with only alphabetical characters)
    char_counts.append(len(new_word))
    #Increase the total character count by the length of the word
    tot_char_count += len(new_word)


#Calulate average character count per word
avg_char_count = round(tot_char_count/len(char_counts),1)

#Print results to terminal window
print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {word_count}")

#***********For paragraph 1 and  passage_text*************
#print(f"Approximate Sentence Count: {sentence_count}")
#*********************************************************

#*****************For all paragraphs*****************
print(f"Approximate Sentence Count: {sent_len}")
#****************************************************

print(f"Average Letter Count: {avg_char_count}")
print(f"Average Sentence Length: {avg_words_perSent}")




