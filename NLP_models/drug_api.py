import pandas as pd
import numpy as np
from allennlp.predictors.predictor import Predictor


predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/bidaf-elmo-model-2018.11.30-charpad.tar.gz")


def find_drug_name(abstract):
	answers=predictor.predict(passage=abstract,question='What is the drug name?')
	drug_name=answers['best_span_str']
	print("Drug Name:",drug_name)



df = pd.read_csv('clean_docs_50_complete_share.csv')
for index,row in df.iterrows():
	abstract_val=row['abstract']
	find_drug_name(abstract_val)

