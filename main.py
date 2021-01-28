from flask import Flask
from flask import request
import controls

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
	json_data = request.json
	X_Value = json_data["X"]
	Y_Value = json_data["Y"]
	On_Value = json_data["ON"]
	controls.moveTo(X_Value, Y_Value, On_Value)
	return "success!"

if __name__ == '__main__':
	controls.init_setup()
	app.run(debug=True, port=8888, host='0.0.0.0')
	controls.cleanup()
