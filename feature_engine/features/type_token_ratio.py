"""
file: type_token_ratio.py
---
Defines a feature that outputs the word type-token ratio.
"""

from features.word_count import *
  
"""
function: get_word_TTR
@param text: The message for which we are calculating the word type-token ratio.
Recall that the type-token ratio is equal to (# of unique words) / (# of total words).
The output of this function should be a number (specifically, a float).
Example: “Please, oh please can I go to the ball?” → 8 / 9 → 0.889
"""
def get_word_TTR(text):
    text = text.strip()
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    text = re.sub(r'[^\w\s]', '', text)
    words = [word.lower() for word in text.split()]

    unique_words = len(set(words))
    total_words = len(words)

    if total_words > 0:
        ttr = unique_words / total_words
    else:
        ttr = 0  

    return ttr

# print(get_word_TTR("hi hi hi hi hi")) 