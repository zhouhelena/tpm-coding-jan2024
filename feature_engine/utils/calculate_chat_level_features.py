"""
file: calculate_chat_level_features.py
---
This file defines the ChatLevelFeaturesCalculator class using the modules defined in "features".
The intention behind this class is to use these modules and define any and all chat level features here. 

The steps needed to add a feature would be to:
- First define any building blocks that the feature would need in the appropriate "features" module (like word counter).
- Define a function within the class that uses these building blocks to build the feature and appends it 
  to the chat level dataframe as columns.
- Call the feature defining function in the driver function.
"""
import pandas as pd
# Importing modules from features
from features.politeness_features import *
from features.basic_features import *
from features.other_lexical_features import *


class ChatLevelFeaturesCalculator:
    def __init__(self, chat_data: pd.DataFrame) -> None:
        """
            This function is used to initialize variables and objects that can be used by all functions of this class.

        PARAMETERS:
            @param chat_data (pd.DataFrame): This is a pandas dataframe of the chat level features read in from the input dataset.
        """
        # print(f'this is the length{len(chat_data)}')
        # print(chat_data.tail(1))
        self.chat_data = chat_data

    def calculate_chat_level_features(self) -> pd.DataFrame:
        """
            This is the main driver function for this class.

        RETURNS:
            (pd.DataFrame): The chat level dataset given to this class during initialization along with 
                            new columns for each chat level feature.
        """
        
        # Text-Based Basic Features
        self.text_based_features()

        # Other lexical features
        self.other_lexical_features()

        # Politeness (ConvoKit)
        self.calculate_politeness_sentiment()

        # Return the input dataset with the chat level features appended (as columns)
        return self.chat_data

    def text_based_features(self) -> None:
        """
            This function is used to implement the common text based featuers.
        """
        # Count Words
        '''
        @TODO: Call your count_words() function here!
        '''

    
    def other_lexical_features(self) -> None:
        """
            This function extract the number of questions, classify whether the message contains clarification questions,
            calculate the word type-to-token ratio, and the proportion of first person pronouns from the chats
            (see features/other_LIWC_features.py to learn more about how these features are calculated)
        """
        
        '''
        @TODO: Call your get_word_TTR() function here!
        '''


    def calculate_politeness_sentiment(self) -> None:
        """
        This function calls the Politeness module from Convokit and includes all outputted features.
        """
        
        '''
        @TODO: Call your get_politeness_strategies() function here! 
        PS: Don't forget to appropriately process your output!
        '''