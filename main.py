from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
	json_data = request.json
	X_Value = json_data["X"]
	Y_Value = json_data["Y"]
	On_Value = json_data["ON"]
	return "X_Value: {} Y_Value: {} On_Value: {}".format(X_Value, Y_Value, On_Value)

if __name__ == '__main__':
	app.run(debug=True, port=8888, host='0.0.0.0')
