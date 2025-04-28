from flask import Flask, request
import yaml

app = Flask(__name__)

@app.route('/vuln', methods=['POST'])
def vuln():
    data = request.data
    yaml.load(data, Loader=yaml.FullLoader)  # vulnerable!
    return "Data loaded!", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
