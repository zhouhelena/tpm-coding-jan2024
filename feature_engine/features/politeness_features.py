"""
file: politeness_features.py
---
Defines a feature that calls the PolitenessStrategies from ConvoKit
and returns them as 21 columns (for each message).

Link to Politness Documentation: https://convokit.cornell.edu/documentation/politenessStrategies.html
Link to ConvoKit GitHub examples: https://github.com/CornellNLP/ConvoKit/tree/master/examples/politeness-strategies

You should follow the samples to create the appropriate imports, process the data, and call the function.
"""

import pandas as pd
from convokit import PolitenessStrategies
from convokit import Corpus, Speaker, Utterance
from convokit import TextParser, process_text
from pandas import DataFrame
import re
import spacy
from spacy.tokens import Doc

nlp = spacy.load("en_core_web_sm")

"""
function: get_politeness_strategies
(Chat-level function)

This gets the politeness annotations of each message, with some fields 
including HASHEDGE, Factuality, Deference, Gratitude, Apologizing, etc.
"""
def get_politeness_strategies(text):
    if not text:
        return pd.DataFrame({})
    
    ps = PolitenessStrategies()

    utterance = Utterance(id="0", speaker=Speaker(id="user"), text=text)
    parsed = process_text(text, spacy_nlp=nlp)
    utterance.add_meta("parsed", parsed)
    corpus = Corpus(utterances=[utterance])
    
    polite_strategies = ps.transform(corpus)

    features = polite_strategies.get_utterance(utterance.id).meta['politeness_strategies']
    df = pd.DataFrame([features])

    df.columns = [re.sub(r'feature_politeness_==', '', col) for col in df.columns]
    df.columns = [re.sub(r'==', '', col) for col in df.columns]

    return df
