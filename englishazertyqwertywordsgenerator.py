#!/bin/python
import re
import sys
import random
# pip3 install requests
import requests

def get_words():
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    response = requests.get(url)
    words = response.text.split("\n")
    return words

def filter_words(words):
    pattern = re.compile(r'^[ertyuiopsdfghjkl]+$')
    filtered_words = [word for word in words if pattern.match(word)]
    return filtered_words

def display_words_in_batches(words, batch_size=20):
    random.shuffle(words)  # Mélanger les mots
    for i in range(0, len(words), batch_size):
        batch = words[i:i+batch_size]
        print("\n".join(batch))
        input("\nAppuyez sur Entrée pour afficher les 20 mots suivants...")

if __name__ == "__main__":
    words = get_words()
    filtered_words = filter_words(words)

    print("Mots contenant uniquement les lettres 'ertyuiopsdfghjkl' (mélangés):")
    display_words_in_batches(filtered_words)
