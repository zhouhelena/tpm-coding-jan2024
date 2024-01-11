"""
file: featurize.py
---
This file is the main driver of the feature generating pipeline. 
It instantiates and calls the FeatureBuilder class which defines the logic used for feature creation.
"""

# Importing the Feature Generating Class
from feature_builder import FeatureBuilder

# Main Function
if __name__ == "__main__":
	
	
	# Instantiating the Feature Generating Class
	# Calling the "engine"/"driver" function of the FeatureBuilder class 
	# that creates the features, and writes them in output.
	# Defines one class for each dataset.

	# TINY Test sets --- just two conversations each
	# Tiny Juries
	feature_builder = FeatureBuilder(
		input_file_path = "../feature_engine/data/raw_data/juries_tiny_for_testing.csv",
		output_file_path_chat_level = "../feature_engine/output/chat/jury_TINY_output_chat_level.csv",
		output_file_path_user_level = "../feature_engine/output/user/jury_TINY_output_user_level.csv",
		output_file_path_conv_level = "../feature_engine/output/conv/jury_TINY_output_conversation_level.csv",
		turns = False,
		analyze_first_pct = [0.25, 0.5, 0.75, 1]
	)
	feature_builder.featurize(col="message")

	# Tiny CSOP
	tiny_csop_feature_builder = FeatureBuilder(
		input_file_path = "../feature_engine/data/raw_data/csop_conversations_TINY.csv",
		output_file_path_chat_level = "../feature_engine/output/chat/csop_TINY_output_chat_level.csv",
		output_file_path_user_level = "../feature_engine/output/user/csop_TINY_output_user_level.csv",
		output_file_path_conv_level = "../feature_engine/output/conv/csop_TINY_output_conversation_level.csv",
		turns = True,
		analyze_first_pct = [0.25, 0.5, 0.75, 1]
	)
	tiny_csop_feature_builder.featurize(col="message")

	