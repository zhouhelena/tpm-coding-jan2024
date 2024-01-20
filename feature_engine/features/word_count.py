"""
file: word_count.py
---
Defines a feature that counts the number of words in a message.
"""
import numpy as np
import re

"""
function: count_words
@param text: The message for which we are counting words.
The output of this function should be a number (specifically, an integer).
Example: “Hello, how are you?” → 4
"""
def count_words(text):
    text = text.strip()
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    count = len(words)

    return count

# print(count_words("Hello, how are you? ?? ??? !!! . hi . hi.... hi")) 