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

<img src="whole_team.jpg" alt="team" width="300" height="200/>

## Introduction
There are many studies published on the utilization of generic drugs for cancer treatment. Analyzing this data is a huge challenge for automation, with little profit incentive, which is why Cures for Cancer within Reach is taking this on.

We created a machine learning powered interface for annotating scientific abstracts. It uses suggestions as it guides the user through the annotation process - the user may not have a biomedical background. Often patient families are eager to help - and more than getting the work done, we make people feel empowered, not so helpless, in the most difficult period of their lives.

This terrific impact is powered by an architecture relying on `AllenNLP` and `SciSpacy` for the bulk of the work - a question answering model trained with ELMo provides excellent automatic annotations for cancer and drugs. `SciSpacy` as a prelayer that increased the quality of our results.


## Design
![design UI](images/design_ui.png)

## Summary of Methods
This project involves breaking down overwhelmingly technical text into information that can be used to identify promising cancer research directions. Therefore, when implementing the machine learning model to aid the user in labeling / annotating the data, our first priority was to create something that does not require for them to read the full abstract or even to have any clue as to what the abstract is communicating from a biomedical research perspective. For this reason, we wanted to make the user's sole job to evaluate and improve our machine learning model.

Since a user interface in a very simple development environment and a limited amount of time does not allow for machine learning models to be trained and re-trained in between user clicks of a button, we researched pre-trained models to see if we could query API(s) for our suggestive interface. 

The most promising tool at our disposal was Allen NLP, which is an open-source NLP research library, built on PyTorch. They have a functionality called "Reading Comprehension." This deep learning tool allows for the input data to be in the form of question and the output data to be in the form of an answer (or answer choice in the case that multiple options are specified). We used Allen NLP as an API towards which to query and used the output from their pre-trained ELMo-BiDaF models as suggested answers for the user.

For each annotation label category, we engineered the input and output specifications by testing which types of query strings return most accurate results when compared against the labeled data given for this project. Below, we have provided a summary of how each model works in the context of our working demonstration.

**DRUG**: 

```python
def find_drug_name(title):
```

**CANCER**:
```python
def identify_cancer(title, abstract):
```

**THERAPEUTIC ASSOCIATION**:
```python
def association_hint(passage):
```

**STUDY TYPE**:
```python
def classify_study_type(text):
```

## Pipeline
![pipeline diagram](images/pipeline_diagram.png)

## Languages, Packages, and Technologies
• **`Python`**: back end and Natural Language Processing
• **`Flask`**: integrate front end with back end
• **`Jupyter Notebook`**: testing, exploratory data analysis, and development
• **`sci-kit learn`**: training machine learning-based text classifiers
• **`Regex (regular expression)`**: clean data set, eliminating non-ASCII character set
• **`NLTK (Natural Language Toolkit)`**: text processing for classification models 
• **`HTML/CSS`**: UX/UI design
• **`Javascript / jquery`**: validations and dynamic elements in HTML/CSS 
• **`Heroku`**: hosting server
• **`AllenNLP`**: framework used for Natural Language processing
• **`Scispacy` / `spacy`**: used to extract biomedical terms and pre-process text for deep learning. 

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
![Demo 1](demos/working_demo1.gif)

![Demo 2](demos/working_demo2.gif)

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
