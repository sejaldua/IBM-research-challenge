import re

def underline(text):
    '''simple function to underline relevant terms for annotation using regex'''

    #indicator words for vivo/vitro and other study types - to be extracted using nlp in future
    vivo_checks = ["mouse", "mice", "rat", "rats", "animal","vivo"]
    vitro_checks = ["vitro"]
    other_study = ["clinical trial", "clinical study", "case study", "clinic", "clinical", "inconclusive", "side effects", "report"]
    
    underlined_text = []

    for checks in [vitro_checks, vivo_checks, other_study]:
        for keyword in checks:
            results = re.findall(r"(?:\S+\s+){0,3}\b"+re.escape(keyword)+r"\b\s*(?:\S+\b\s*){0,3}",text)
            if len(results) > 0:
                underlined_text.append(results[0].rstrip().lstrip())
    
    return underlined_text