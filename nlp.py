import json
import stanfordnlp
from config import config
import warnings
warnings.simplefilter('ignore', FutureWarning)
warnings.simplefilter('ignore', UserWarning)

def nlp_pipeline(text):
    required = {}

    nlp = stanfordnlp.Pipeline(**config.setting)
    doc = nlp(text)
    required['output'] = []
    for sent in doc.sentences:
        for word in sent.words:
            relationship = {}
            relationship['Text'] = text
            relationship['Orig'] = word.text
            relationship['Similarity'] = word.dependency_relation

            required['output'].append(relationship)
    result = json.dumps(required)

    return result

#print(nlp_pipeline("I saw the man with the binoculars on the hill."))