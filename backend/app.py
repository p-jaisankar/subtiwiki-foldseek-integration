from flask import Flask, request, jsonify
from mock_foldseek import run_mock_foldseek

app = Flask(__name__)

@app.route('/api/foldseek', methods=['POST'])
def foldseek_api():
    data = request.json
    query = data.get('query_file')
    target = data.get('target_db')
    results = run_mock_foldseek(query, target)
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True)
