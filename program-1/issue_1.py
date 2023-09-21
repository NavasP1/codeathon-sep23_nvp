from collections import Counter

def sort_string_by_frequency(s):
    # Step 1: Create a dictionary to store the frequency of each character
    freq_dict = Counter(s)

    # Step 2: Sort the dictionary by the frequency of characters in descending order
    sorted_dict = dict(sorted(freq_dict.items(), key=lambda item: item[1], reverse=True))

    # Step 3: Create a new string by concatenating each character in the sorted dictionary with its frequency
    sorted_string = ""
    for char, freq in sorted_dict.items():
        sorted_string += char * freq

    return sorted_string