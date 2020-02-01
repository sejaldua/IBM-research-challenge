import pandas as pd
import numpy as np
import allennlp
import io
import scispacy
import spacy
from allennlp.predictors.predictor import Predictor
import io
import pandas as pd

def identify_cancer(title, abstract):
  nlp = spacy.load("en_core_sci_sm")
  predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/naqanet-2019.04.29-fixed-weight-names-allennlpv1.0.tar.gz")

  def find_cancer_type(abstract, query_str):
    study_type = predictor.predict(passage=abstract, question=query_str)
    return study_type['answer']['value']

  doc = nlp(title)
  query_list = list(doc.ents)
  query_list = [str(w) for w in query_list]
  query_str = "Of " + " ".join(query_list) + " , which cancer?"
  return find_cancer_type(df['abstract'][i], query_str))
