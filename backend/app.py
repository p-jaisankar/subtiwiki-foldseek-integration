#Flask app

from flask import Flask, request, jsonify
import foldseek_utils

app = Flask(__name__)

# Example endpoint for running Foldseek queries
@app.route('/api/foldseek/search', methods=['POST'])
def run_foldseek():
    data = request.json
    query_file = data['query_file']
    target_db = data['target_db']
    
    # Run Foldseek search
    results = foldseek_utils.run_foldseek(query_file, target_db)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
