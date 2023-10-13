from flask import Flask, send_file

app = Flask(__name__)

# Define a route to serve the trained model
@app.route('/', methods=['GET'])
def download_model():
    model_path = 'knn.pkl'
    filename = 'knn.pkl'

    return send_file(model_path, as_attachment=True, download_name="Model")

if __name__ == '__main__':
    app.run(debug=True)
