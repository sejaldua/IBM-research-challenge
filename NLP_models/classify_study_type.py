import allennlp
import pandas as pd
import numpy as np
from allennlp.predictors.predictor import Predictor
import re

predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/bidaf-elmo-model-2018.11.30-charpad.tar.gz")

def allen_study_type(abstract):
    '''calls AllenNLP on the given abstract to return predicted study type'''

    answers=predictor.predict(passage=abstract, question='Is it vitro, vivo or both?')
    study_type=answers['best_span_str']
    return study_type

def allen_cleanup(abstract):
    '''cleans up AllenNLP results to extract relevant category for study type'''

    cleaned_answer = None
    answer = allen_study_type(abstract)
    if ("vivo" in answer and "vitro" in answer) or ("both" in answer):
        cleaned_answer = "both"
    elif "vivo" in answer:
        cleaned_answer = "vivo"
    return cleaned_answer

def classify_study_type(text):
    '''decision function for using classification rules and AllenNLP together'''

    # words that indicate one study type or another
    # NOTE: due to lack of domain expertise, we do not know which biomedical
    # terms are used to denote in vitro studies, but some words we considered were
    # "assay" and "cell lines"
    vivo_checks = ["mouse", "mice", "rat", "rats", "animal","vivo"]
    vitro_checks = ["vitro"]

    words = text.split()
    ans = None

    vivo_count = 0
    vitro_count = 0

    for word in vivo_checks:
        if word in words:
            vivo_count+=1
        for word in vitro_checks:
            if word in words:
                vitro_count+=1

    # cases which clearly indicate the abstract involves one study type or another
    if vivo_count == 0 and vitro_count > 0:
        ans = "vitro"
    elif vivo_count > 0 and vitro_count == 0:
        ans = "vivo"
    elif vivo_count - vitro_count >= 3:
        ans = "vivo"
    elif vitro_count - vivo_count >= 3:
        ans = "vitro"

    # do further discriminating via API query with pretrained NLP model
    else:
        ans = allen_cleanup(text) 

    return ans

  