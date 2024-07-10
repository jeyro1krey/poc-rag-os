from flask import Flask, request
from flask import jsonify
from flask_cors import CORS, cross_origin

import base64

from typing import Annotated, Union

from inference_bot import repondre_question
from ingestion_doc import ingerer_document
from vecto_db import portion_doc, ecrire_db
from inference_bot import repondre_question

model_spacy = "fr_core_news_lg"
nom_db = 'db/test_premier'


app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'





@app.route('/', methods=['GET'])
def nouveau():
    response = jsonify({'message':'bienvenue'})
    response.headers.add('Access-Control-Allow-Origin',"*")
    return response

@app.route('/questions', methods=['GET','POST'])
def question_reponse():
    request_data = request.get_json()
    question = request_data['prompt']
    print('question : ',question)
    #response = jsonify({'message':'bienvenue'})
    response_temp = repondre_question(question)
    response = jsonify({'message':response_temp})
    response.headers.add('Access-Control-Allow-Origin',"*")
    return response

@app.route('/file/upload',methods=['GET','POST'])
def create_upload_file():
    if 'data' not in request.files:
        return {"message": "No upload file sent"}
    else:
        fichier = request.files['data'].save("db/temp.pdf")
        #print('data', image_string)
        pages = ingerer_document(fichier)
        chunks = portion_doc(pages, model_spacy)
        db = ecrire_db(chunks, nom_db)

        message = {"message": "prêt pour questions"}
        response = jsonify(message)
        response.headers.add('Access-Control-Allow-Origin',"*")

        return response
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)