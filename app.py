from predicted import classifier
from Tools import savefile
from hashlib import md5
from flask import Flask, request, jsonify, Response
app = Flask(__name__)

@app.route('/classifier', methods=['POST'])
def predicted_classifier():
    corpus_path = "./upload_corpus/"
    content = request.args.get('content', '')
    hl = md5()
    hl.update(content.encode(encoding='utf-8'))
    filename =  hl.hexdigest()
    savefile(corpus_path + filename + ".txt" , content.encode('utf-8')) 
    data = dict(class_type=classifier(filename))
    resp = jsonify(data)
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)