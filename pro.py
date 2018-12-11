import subprocess
from flask import Flask
from flask import request, jsonify, render_template

app = Flask(__name__)

result = subprocess.run(["top", "-n", "1", "-b"], stderr=subprocess.PIPE, stdout=subprocess.PIPE)

summ = result.stdout.split(b'\n')

summ = summ[6:]

x_data=[]
y_data=[]

for row in summ[1:]:
	x_data.append(row[37:44])
	y_data.append(row[68:])

print(x_data[:15])
print(y_data[:15])

@app.route('/data', methods=['GET'])
def data():
	result = subprocess.run(["top", "-n", "1", "-b"], stderr=subprocess.PIPE, stdout=subprocess.PIPE)

	summ = result.stdout.split(b'\n')

	summ = summ[6:]

	x_data=[]
	y_data=[]

	for row in summ[1:]:
		x_data.append(row[37:44])
		y_data.append(row[68:])

	result = {'output': x_data, 'input': y_data}

	return jsonify(result)

@app.route('/')
def trial():
    return render_template('five_funds.html')

if __name__ == "__main__":
	app.run()