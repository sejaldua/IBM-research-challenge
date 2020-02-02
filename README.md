# IBM-research-challenge
TechTogether Boston 2020

## About
An NLP-powered, user-facing annotation tool to identify promising generic drugs for cancer treatment. 

## The Team
* Ashvini Varatharaj [Worcester Polytechnic Institute]
* Anastasia Spangler [Bellevue College]
* Sejal Dua [Tufts University]
* Smruthi Ramesh [Northeastern University]
* Sulbha Aggarwal [Queens College (CUNY)]

## Engineering Design Process
#### Design

#### Initial Approach



## Pipeline


## Languages, Packages, and Technologies
* Python
* Flask
* Jupyter notebook
* sci-kit learn
* regex
* nltk
* HTML
* CSS
* Javascript / jquery
* Heroku
* Allen NLP
* Scispacy / spacy

## Summary of Methods

## Bonus Challenge
* Goal: Use paper abstracts to classify them as directly relevant and non-relevant to cancer research
* Preprocessing: Cleaned up non-ascii characters resulting from footnotes and table links using regular expressions
* Features: Bag of words with stopwords removed (including domain relevant terms like measurements and acronyms)
  * Added part of speech tags onto the feature to provide more context
* Values: Word counts with a maximum per document limit to prevent common domain terms like "patient" that don't help with classification
  * Plan to move to tfIdf once there is more data
* Models: Logistic Regression and Support Vector Classifier trained with leave-one-out cross-validation due to small data size
* Accuracy: 73% for Logistic Regression and 74% for Support Vector Classifier
* Interesting Indicators:
  * Exclude: tolerated, safe
  * Include: demonstrated, potent, antitumor

## The Model in Action
![Demo 1](demos/working_demo1.gif)

![Demo 2](demos/working_demo2.gif)

## Future Directions
* offer a textbook for the user to paste a scientific abstract from PubMed
* color code the confidence values of network predictions 
* hover over biomedical jargon for simplified definition (e.g. apoptosis --> cell death)
* underline keywords to draw attention to themes that help inform the reader to answer the questions
* integrate saved responses with mongo DB database
* clean data better (e.g. filter out for artifacts and section titles like "BACKGROUND")
* be able to handle more complex therapeutic association classification than just binary (e.g. effective, no effect, inconclusive, detrimental)
* evaluate success of machine learning models with user input
* spend more time on bonus problem using neural net / `tdidf`

