"""
file: feature_builder.py
---
This file defines the FeatureBuilder class using the modules defined in "utils" and "features".
The intention behind this class is to use these modules and:
- Preprocess the incoming dataset defined in an input file path.
- Create chat level features -> Use the moduled in "utils" and "features" to create features 
                                on each chat message in the dataset (like word count, character count etc.).
- Create conversation level features -> These can come from 2 sources:
                                        - By aggregating the chat level features
                                        - By defining new features specifically applicable for conversations
- Save the chat and conversation level features in the output path specified.
"""

# 3rd Party Imports
import pandas as pd
import re
import numpy as np
from pathlib import Path

# Imports from feature files and classes
# from utils.summarize_chat_level_features import *
from utils.calculate_chat_level_features import ChatLevelFeaturesCalculator
from utils.preprocess import *

class FeatureBuilder:
    def __init__(
            self, 
            input_file_path: str, 
            output_file_path_chat_level: str, 
        ) -> None:
        """
            This function is used to define variables used throughout the class.

        PARAMETERS:
            @param input_file_path (str): File path of the input csv dataset (assumes that the '.csv' suffix is added)
            @param output_file_path_chat_level (str): Path where the output csv file is to be generated 
                                                      (assumes that the '.csv' suffix is added)
        """
        #  Defining input and output paths.
        self.input_file_path = input_file_path
        print("Initializing Featurization for " + self.input_file_path + " ...")

        # Reading chat level data (this is available in the input file path directly).
        self.chat_data = pd.read_csv(self.input_file_path, encoding='mac_roman')

        # Preprocess chat data
        self.preprocess_chat_data(col="message", turns=False)

        # Set all paths for vector retrieval (contingent on turns)
        self.output_file_path_chat_level = output_file_path_chat_level

    def featurize(self, col: str="message") -> None:
        """
            This is the main driver function of this class.
        
        PARAMETERS:
            @param col (str): (Default value: "message")
                              This is a parameter passed onto the preprocessing modules 
                              so as to identify the columns to preprocess.
        """
        print("Generating chat-level Features ...")
        self.chat_level_features()
        # Make it possible to create folders if they don't exist
        Path(self.output_file_path_chat_level).parent.mkdir(parents=True, exist_ok=True) 
        # Write the feartures into the files defined in the output paths.
        self.chat_data.to_csv(self.output_file_path_chat_level, index=False)
        print("All Done!")
            
    def preprocess_chat_data(self, col: str="message", turns=False) -> None:
        """
            This function is used to call all the preprocessing modules needed to clean the text.
        
        PARAMETERS:
            @param col (str): (Default value: "message")
                              This is used to identify the columns to preprocess.
        """
        # create the appropriate grouping variables and assert the columns are present
        self.chat_data = preprocess_conversation_columns(self.chat_data)
        assert_key_columns_present(self.chat_data)
        # Preprocessing the text in `col` and then overwriting the column `col`.
        self.chat_data[col] = self.chat_data[col].astype(str).apply(preprocess_text)

    def chat_level_features(self) -> None:
        """
            This function instantiates and uses the ChatLevelFeaturesCalculator to create the chat level features 
            and add them into the `self.chat_data` dataframe.
        """
        # Instantiating.
        chat_feature_builder = ChatLevelFeaturesCalculator(
            chat_data = self.chat_data
        )
        # Calling the driver inside this class to create the features.
        self.chat_data = chat_feature_builder.calculate_chat_level_features()
        # Remove special characters in column names
        self.chat_data.columns = ["".join(c for c in col if c.isalnum() or c == '_') for col in self.chat_data.columns]