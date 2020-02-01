import pandas as pd
import numpy as np
from allennlp.predictors.predictor import Predictor


predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/bidaf-elmo-model-2018.11.30-charpad.tar.gz")


def find_study_type(abstract):
	answers=predictor.predict(passage=abstract, question='Is it vitro, vivo or both?')
	study_type=answers['best_span_str']
	return study_type



df = pd.read_csv('clean_docs_50_complete_share.csv')
answers = []
for index,row in df.iterrows():
	abstract_val=row['abstract']
	answers.append(find_study_type(abstract_val))
print(answers)