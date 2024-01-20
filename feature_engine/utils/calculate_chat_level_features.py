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
# Importing features
from features.politeness_features import *
from features.word_count import *
from features.type_token_ratio import *

class ChatLevelFeaturesCalculator:
    def __init__(self, chat_data: pd.DataFrame) -> None:
        """
            This function is used to initialize variables and objects that can be used by all functions of this class.

        PARAMETERS:
            @param chat_data (pd.DataFrame): This is a pandas dataframe of the chat level features read in from the input dataset.
        """
        self.chat_data = chat_data

    def calculate_chat_level_features(self) -> pd.DataFrame:
        """
            This is the main driver function for this class.

        RETURNS:
            (pd.DataFrame): The chat level dataset given to this class during initialization along with 
                            new columns for each chat level feature.
        """
    
        self.apply_word_count()
        self.apply_word_ttr()
        self.apply_politeness()

        # Return the input dataset with the chat level features appended (as columns)
        return self.chat_data

    def apply_word_count(self) -> None:
        """
            This function calls the function that counts the number of words in a message.
        """
        # Count Words
        self.chat_data["num_words"] = self.chat_data["message"].apply(count_words)
    
    def apply_word_ttr(self) -> None:
        """
            This function calls the function that calculates the word type-to-token ratio.
        """
        self.chat_data["word_TTR"] = self.chat_data["message"].apply(get_word_TTR)
        
    def apply_politeness(self) -> None:
        """
        This function calls the Politeness module from Convokit and includes all outputted features.
        """
        politeness_features_list = []

        for text in self.chat_data["message"]:
            politeness_features = get_politeness_strategies(text)
            politeness_features_list.append(politeness_features)
        
        politeness_features_df = pd.concat(politeness_features_list, ignore_index=True)
        
        self.chat_data = pd.concat([self.chat_data, politeness_features_df], axis=1)