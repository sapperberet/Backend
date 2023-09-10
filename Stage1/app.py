from flask import Flask, jsonify, request
from datetime import *
from django.http import JsonResponse
import pytz
app = Flask(__name__)
date = datetime.now().strftime('%A')
time =  datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
@app.route('/api/endpoint', methods=['GET'])
def api_endpoint():
    response = {
    "slack_name": "example_name",
    "current_day": f"{date}",
    "utc_time": f"{time}",
    "track": "backend",
    "github_file_url": "https://github.com/sapperberet/Backend/blob/main/Stage1/app.py",
    "github_repo_url": "https://github.com/sapperberet/Backend",
    'status_code': 200
    }
    return jsonify(response)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
