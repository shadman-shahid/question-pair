from flask import Flask, request
from get_answer import load_models, get_answer


pipe = load_models()
app = Flask(__name__)

@app.route("/get_answer",  methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        query = request.form.get("query")
        answer = get_answer(query, pipe)
        return answer
    return "Ok!"



if __name__ == "__main__":
    app.run(debug=True)