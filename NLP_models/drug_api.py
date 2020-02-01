import pandas as pd
import numpy as np
from allennlp.predictors.predictor import Predictor


predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/bidaf-elmo-model-2018.11.30-charpad.tar.gz")


def find_drug_name(abstract):
	''' Query Allen NLP API reading comprehension to discern drug name via pre-trained model. '''
	
	answers=predictor.predict(passage=abstract,question='What is the drug name?')
	drug_name=answers['best_span_str']
	return drug_name

