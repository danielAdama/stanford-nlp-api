import os

LANG_MODEL = os.path.join(os.path.abspath("../stanfordnlp_resources"),"en_ewt_models")
setting = {
        'processors': 'tokenize,pos,depparse',
        'lang': 'en',
        'tokenize_model_path': os.path.join(LANG_MODEL, "en_ewt_tokenizer.pt"),
        'pos_model_path': os.path.join(LANG_MODEL, "en_ewt_tagger.pt"),
        'pos_pretrain_path': os.path.join(LANG_MODEL, "en_ewt.pretrain.pt"),
        'depparse_model_path': os.path.join(LANG_MODEL, "en_ewt_parser.pt"),
        'depparse_pretrain_path': os.path.join(LANG_MODEL, "en_ewt.pretrain.pt")
    }

HTTP_400_BAD_REQUEST = 400
HTTP_200_OK = 200
HTTP_500_INTERNAL_SERVER_ERROR = 500
HTTP_404_NOT_FOUND = 404
