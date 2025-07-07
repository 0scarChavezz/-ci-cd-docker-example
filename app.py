from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola desde Docker!"

@app.route('/api/suma')
def suma():
    return jsonify({"resultado": 4 + 4})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
