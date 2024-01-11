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

# Importing modules from features
from features.politeness_features import *
from features.basic_features import *
from features.other_lexical_features import *


class ChatLevelFeaturesCalculator:
    def __init__(self, chat_data: pd.DataFrame, vect_data: pd.DataFrame, bert_sentiment_data: pd.DataFrame) -> None:
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
        self.chat_data["num_words"] = self.chat_data["message"].apply(count_words)

    
    def other_lexical_features(self) -> None:
        """
            This function extract the number of questions, classify whether the message contains clarification questions,
            calculate the word type-to-token ratio, and the proportion of first person pronouns from the chats
            (see features/other_LIWC_features.py to learn more about how these features are calculated)
        """
        
        # Calculate the word type-to-token ratio
        self.chat_data["word_TTR"] = self.chat_data["message"].apply(get_word_TTR)


    def calculate_politeness_sentiment(self) -> None:
        """
        This function calls the Politeness module from Convokit and includes all outputted features.
        """
        transformed_df = self.chat_data['message'].apply(get_politeness_strategies).apply(pd.Series)
        transformed_df = transformed_df.rename(columns=lambda x: re.sub('^feature_politeness_==()','',x)[:-2].lower())

        # Concatenate the transformed dataframe with the original dataframe
        self.chat_data = pd.concat([self.chat_data, transformed_df], axis=1)
