#!/bin/python
#!/bin/python
import requests
import random

def get_word_list(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.split('\n')
    else:
        print(f"Failed to retrieve the word list. Status code: {response.status_code}")
        return []

def is_valid_word(word):
    target_letters = set('ertyuiopsdfghjkl')
    return all(c in target_letters for c in word.lower())

def display_word_groups(words, default_group_size, num_groups):
    group_size = max(default_group_size, 1)
    valid_words = [word.lower() for word in words if is_valid_word(word)]

    for i in range(num_groups):
        group = random.choices(valid_words, k=group_size)
        print(" ".join(group))

if __name__ == "__main__":
    url_word_list = "https://raw.githubusercontent.com/dolph/dictionary/master/popular.txt"
    words = get_word_list(url_word_list)

    try:
        default_group_size = int(input("Enter the number of words per group (default is 4): ") or 4)
        num_groups = 20
    except ValueError:
        print("Invalid input. Using the default group size, which is 4.")
        default_group_size = 4
        num_groups = 20

    print(f"\nDisplaying {num_groups} groups of words, each group containing {default_group_size} words containing the letters 'ertyuiopsdfghjkl':")
    display_word_groups(words, default_group_size, num_groups)

