#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):

    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

def get_sentence():
    while True:
        sentence = input("Please enter sentence")
    if is_sentence(sentence):
                return sentence
    else:
                print("Error: Sentence must start with a capital letter and end with punctuation (., !, ?).")

def calculate_frequencies(sentence):
    word = sentence[:-1].split()
    wordlist = []
    freqlist = []

    for word in words:
        if word in wordList:
         index = wordList.index(word)
         freqList[index] += 1
        else:
         wordList.append(word)
         freqList.append(1)
        return wordList, freqList

#print the results
def printFrequencies(words, freqs):
    print("\nWord frequencies:")
    for i in range(len(words)):
        print(words[i], "-", freqs[i])


def main():
    sentence = getSentence()
    words, freqs = calculateFrequencies(sentence)
    printFrequencies(words, freqs)

main()










    
