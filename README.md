# Team Processing Mapping Coding Task

Welcome to the coding task for the Team Process Mapping project! Before you begin, please make sure to read through the full instructions [here](https://docs.google.com/document/d/1_FZ-N-7Qr9_CXK-fX9vdcMhkaDzmRXyUh1aHEHjL1hs/edit).

## Packages and Requirements

The packages required for you to complete the task are listed in `requirements.txt`. You can use a virtual environment for managing the dependencies associated with this project.

## Your Goal

To complete this assignment, you will need to modify 4 different files:

- features/word_count.py: `count_words(text)`
- features/type_token_ratio.py: `get_word_ttr(text)`
- features/politeness_features.py: `get_politeness_strategies(text)`
- utils/calculate_chat_level_features.py (For calling the functions; you only need to modify `apply_politeness()`).

## Your Deliverables

At the end of Part 2, we will need the following:

- A link to your GitHub cloned repository. This should contain:
  1. Your Python code;
  2. Your Part 2 Reflection (directly edit this README!).
- A copy of your chat-level CSV that contains columns for the features you generated. **Note: this should be reproducible!** We should be able to get the same results by running your code from the GitHub link you submit.

# Part 2 Reflection

Please answer the following four questions:

## 1. Sanity Check

Open up your output CSV and look at the columns you generated for each of the three features. Do the values “make sense” intuitively? Why or why not?

> The values make sense intuitively. After reviewing a few random rows, the number of words and TTR calculated are correct for corresponding messages. I also agree with the values for the different politeness strategies, though I could not find the definitions for some of these politeness strategies (ex: 1st_person_start).

## 2. Testing

How would you implement tests for these features?

> I would implement straightforward unit tests for count_words() and get_word_TTR(). The code would be implemented like the following:

    class TestWordCount(unittest.TestCase):
      def test_basic(self):
        self.assertEqual(count_words("Hello, how are you?"), 4)

> I would test edge cases such as empty strings, special characters, varying uppercase and lowercase letters, etc. Testing get_politeness_strategies() is a bit more complex due to its dependencies and output structure. In the Convokit Github, I saw [unit tests for the politeness strategies API](https://github.com/CornellNLP/ConvoKit/blob/c5b2bd790614c3365352d68f5a299e8e3172ef47/convokit/tests/politeness_strategies/test_politeness_strategies.py#L133). Similarly, I would use texts with predefined values for the strategies and check for expected politeness strategies in the result.

## 3. Overall Experience

Please provide an overall reflection of your experience. How did you approach this task? What challenge(s) did you encounter? Is there anything you would be curious to explore in the future, if you had more time?

> The first two features were much easier for me than the last feature, as I implemented them relatively quickly. There were some edge cases I needed to catch and work through, such as initially, the letter case distinguishing words for the TTR and various punctuation adding to the word count. I approached this by thinking of edge cases with the code I had written and testing it against the expected output in the console. For the last task, I started by familiarizing myself with the documentation (mostly the introductory tutorial and data format pages) and installing ConvoKit and SpaCy. Next, I looked at the Github examples, especially the [politeness demo](https://github.com/CornellNLP/ConvoKit/blob/master/examples/politeness-strategies/politeness_demo.ipynb) since it resembled the task most. To write get_politeness_strategies() here, I used code from the Github example and documentation and tweaked it to return a cleaned-up dataframe as specified in the instructions. If I had more time, I would be curious to explore more advanced politeness analysis. For example, I would like to see how it differs across cultures, regions, and settings (social media versus in person) and adapt the model to recognize these variations, or how politeness levels correlate with conversation outcomes / resolution of conflicts.

## 4. Time Required

How much time did it take you to complete Parts 1 and 2? (Please be honest; we are looking for feedback to make sure the tasks are scoped appropriately.)

> About 4 hours.
