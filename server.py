from flask import Flask
from flask import jsonify
from flask import request
from rec import get_recommendation
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/recommendation", methods=['GET'])
def recommendation():
    course_name = request.args.get('name')
    print(f"\n\n\n\n{course_name}\n\n\n\n")
    recomendation = get_recommendation(course_name)
    response = jsonify({'recomendation': recomendation})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run()