from flask import Flask, json, request, jsonify
import logging
import argparse
from functools import wraps
import jwt
import os
import sys
import nlp
from config import config

handle = "my-api"
app = Flask(__name__)
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.NOTSET, datefmt='%d-%b-%y %H:%M:%S')
_logger = logging.getLogger(handle)

@app.route("/v1/process", methods = ['POST'])
def process():
    try:
        data = request.get_json()
        _logger.info(data)
        try:
            if not data:
                _logger.warning("API PROCESS > please connect your camera")
                return jsonify({
                    "BaseResponse":{
                            "Status":False,
                            "Message": "Please only pass text",
                            "Data": None,
                        },
                    "Error": "Bad request"
                }), config.HTTP_400_BAD_REQUEST
            try:
                result = nlp.nlp_pipeline(data)
                return jsonify({
                        "BaseResponse":{
                                "Status":True,
                                "Messsage":"Operation successfully"
                            },
                        "detections":json.loads(result),
                    }), config.HTTP_200_OK
            except Exception as ex:
                _logger.warning(f"API PROCESS > No text found")
                return jsonify({
                    "BaseResponse":{
                            "Status":False,
                            "Message":str(ex)
                        },
                    "Error":"Error processing text"
                }), config.HTTP_404_NOT_FOUND

        except Exception as ex:
            _logger.warning(f"API PROCESS > APPLICATION ERROR while processing text")
            return jsonify({
                "BaseResponse":{
                            "Status":False,
                            "Message":str(ex)
                        },
                "Error":"Something went wrong",
            }), config.HTTP_500_INTERNAL_SERVER_ERROR

    except Exception as ex:
            _logger.warning(f"API PROCESS > The data is not in json format")
            return jsonify({
                "BaseResponse":{
                            "Status":False,
                            "Message":str(ex)
                        },
                "Error":"The data is not in json format",
            }), config.HTTP_404_NOT_FOUND


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Text Similarity exposing stanfordnlp")
    parser.add_argument("-p", "--port", default=8080, type=int, help="port number")
    args = parser.parse_args()
    app.run(host='0.0.0.0', debug=True, port=args.port)