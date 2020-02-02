# IBM-research-challenge
TechTogether Boston 2020

## About
An NLP-powered, user-facing annotation tool to identify promising generic drugs for cancer treatment. 
![logo](images/logo.png)

## The Team
* Ashvini Varatharaj [Worcester Polytechnic Institute]
* Anastasia Spangler [Bellevue College]
* Sejal Dua [Tufts University]
* Smruthi Ramesh [Northeastern University]
* Sulbha Aggarwal [Queens College (CUNY)]

![fun with the team](images/team.jpg)

## Introduction
There are many studies published on the utilization of generic drugs for cancer treatment. Analyzing this data is a huge challenge for automation, with little profit incentive, which is why Cures for Cancer within Reach is taking this on.

We created a machine learning powered interface for annotating scientific abstracts. It uses suggestions as it guides the user through the annotation process - the user may not have a biomedical background. Often patient families are eager to help - and more than getting the work done, we make people feel empowered, not so helpless, in the most difficult period of their lives.

This terrific impact is powered by an architecture relying on `AllenNLP` and `SciSpacy` for the bulk of the work - a question answering model trained with ELMO provides excellent automatic annotations for cancer and drugs. `SciSpacy` as a prelayer that increased the quality of our results.


## Engineering Design Process
#### Design
![design UI](images/design_ui.png)

#### Pipeline
![pipeline diagram](images/pipeline_diagram.png)

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
* **Goal**: Use paper abstracts to classify them as directly relevant and non-relevant to cancer research
* **Preprocessing**: Cleaned up non-ascii characters resulting from footnotes and table links using regular expressions
* **Features**: Bag of words with stopwords removed (including domain relevant terms like measurements and acronyms)
  * Added part of speech tags onto the feature to provide more context
* **Values**: Word counts with a maximum per document limit to prevent common domain terms like "patient" that don't help with classification
  * Plan to move to tfIdf once there is more data
* **Models**: Logistic Regression and Support Vector Classifier trained with leave-one-out cross-validation due to small data size
* **Accuracy**: 73% for Logistic Regression and 74% for Support Vector Classifier
* **Interesting Indicators**:
  * Exclude: tolerated, safe
  * Include: demonstrated, potent, antitumor

## The Model in Action
![Demo 1](demos/working_demo.gif)

![Demo 2](demos/working_demo1.gif)

## Future Directions
* offer a text box for the user to paste a scientific abstract from PubMed
* include 3-5 suggestions for the user to select from instead of just 1
* if the hint is not relevant for therapeutic association, give the user the option to highlight relevant text and give their confidence
* color code the confidence values of network predictions 
* hover over biomedical jargon for simplified definition (e.g. apoptosis --> cell death)
* underline keywords to draw attention to themes that help inform the reader to answer the questions
* integrate saved responses with mongo DB database
* clean data better (e.g. filter out for artifacts and section titles like "BACKGROUND")
* be able to handle more complex therapeutic association classification than just binary (e.g. effective, no effect, inconclusive, detrimental)
* evaluate success of machine learning models with user input
* spend more time on bonus problem using neural net / `tdidf`
* use mongoDB for storing user input at large scalability