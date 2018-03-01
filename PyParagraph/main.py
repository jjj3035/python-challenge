import re
import os

path1 = os.path.join('paragraph_1.txt')
path2 = os.path.join('paragraph_2.txt')
files = [path1, path2]

total_sentences = 0
word_list = []
letter_list = []
letter_count_list = []

for file in files:
    with open (file, 'r') as paragraph:
        text = paragraph.read()
        sentence_list = re.split(r'[.!?]', text)
        total_sentences = total_sentences + len(sentence_list)
        for sentence in sentence_list:
            words = re.split(r'[\n\s\t]+', sentence)
            for word in words:
                word_list.append(word)
                letter_count_list.append(len(word))
                for letter in word:
                    letter_list.append(letter)
            
word_list = list(filter(None, word_list))
word_count = len(word_list)
letter_count = sum(letter_count_list)
avg_letter_count = letter_count/len(letter_count_list)
avg_sentence_length = word_count/total_sentences

with open("output.txt", 'w+') as text_file:
    print ('Paragraph Analysis', file=text_file)
    print ('-----------------', file=text_file)
    print ('Approximate Word Count:',word_count, file=text_file)
    print ('Approximate Sentence Count:',total_sentences, file=text_file)
    print ('Average Letter Count:',avg_letter_count, file=text_file)
    print ('Average Sentence Length:',avg_sentence_length, file=text_file)
    
with open('output.txt', 'r') as text_file:
    for line in text_file.readlines():
        print (line)           
