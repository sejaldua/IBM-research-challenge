# import scispacy
import spacy
import re
from allennlp.predictors.predictor import Predictor

print('loading')
predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/bidaf-elmo-model-2018.11.30-charpad.tar.gz")
predictor2 = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/naqanet-2019.04.29-fixed-weight-names-allennlpv1.0.tar.gz")
print('done loading')

def find_drug_name(title):
    answers=predictor.predict(passage=title,question='What is the drug name?')
    drug_name=answers['best_span_str']
    return drug_name

def association_hint(passage):
    question = "What was the impact of the drug on the cancer: effective, detrimental, no effect, or were the results inconclusive? "
    answers = predictor.predict(passage=passage, question=question)
    hint = answers['best_span_str']
    return hint

# def find_cancer_name(title):
#     print('cancer function starting')
#     def a_cancer(phrase):
#         cancers = []
#         with open('cancer.txt', 'r') as f:
#             for line in f:
#                 cancers.append(line.strip())

#         words = phrase.split()

#         for cancer in cancers:
#             if any([word in cancer for word in words]):
#                 return phrase

#     answers = predictor2.predict(passage=title, question='What is the cancer name?')
#     print('predictor is done')
#     cancer_name = answers['answer']['value']
#     return a_cancer(cancer_name)

def identify_cancer(title, abstract):
    print('cancer function starting')
    nlp = spacy.load("en_core_sci_sm")
    print("loaded spacy")
    predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/naqanet-2019.04.29-fixed-weight-names-allennlpv1.0.tar.gz")

    def find_cancer_type(abstract, query_str):
        study_type = predictor.predict(passage=abstract, question=query_str)
        return study_type['answer']['value']

    doc = nlp(title)
    query_list = list(doc.ents)
    query_list = [str(w) for w in query_list]
    query_str = "Of " + " ".join(query_list) + " , which is a cancer?"
    print('predictor is done')
    return find_cancer_type(abstract, query_str)

# predictor = Predictor.from_path( "https://storage.googleapis.com/allennlp-public-models/bidaf-elmo-model-2018.11.30-charpad.tar.gz")

def allen_study_type(abstract):
    '''calls AllenNLP on the given abstract to return predicted study type'''

    answers = predictor.predict(passage=abstract, question='Is it vitro, vivo or both?')
    study_type = answers['best_span_str']
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

    print("classifying study type")
    vivo_checks = ["mouse", "mice", "rat", "rats", "animal", "vivo"]
    vitro_checks = ["vitro"]

    words = text.split()
    ans = None

    vivo_count = 0
    vitro_count = 0

    for word in vivo_checks:
        if word in words:
            vivo_count += 1
        for word in vitro_checks:
            if word in words:
                vitro_count += 1

    if vivo_count == 0 and vitro_count > 0:
        ans = "vitro"
    elif vivo_count > 0 and vitro_count == 0:
        ans = "vivo"
    elif vivo_count - vitro_count >= 3:
        ans = "vivo"
    elif vitro_count - vivo_count >= 3:
        ans = "vitro"
    else:
        ans = allen_cleanup(text)

    print(ans)
    return ans

