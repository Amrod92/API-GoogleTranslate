from flask import Flask, request, jsonify, make_response
from translate import TanslateAPI

app = Flask(__name__)

textTranslate = TanslateAPI


@app.route('/')
def home():
    return "<h1>Welcome to API-GoogleTranslate</h1>"

@app.route('/text', methods=["GET"])
def Translator(ogText):
    trnText = textTranslate(ogText)
    return trnText, 200

@app.route('/textTranslate', methods=["POST"])
def json():
    if request.is_json:
        req = request.get_json()    
        response = {
            "message": "JSON received!",
            "name": req.get("name")
        }

        pairs = response.items()
        for key, value in pairs:
            if key == "name":
                textTrans = Translator(value)
        
        res = make_response(jsonify(textTrans), 200)
        return res
    else:
        res = make_response(jsonify({"message": "Status: 400 - No JSON! Try again"}), 400)
        return res

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)