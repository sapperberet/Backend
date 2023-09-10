from flask import Flask, jsonify, request
from datetime import *
app = Flask(__name__)
date = datetime.now().strftime('%A')
time =  datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')   
@app.route('/api', methods=['GET'])
def api_endpoint():
    #?slack_name=AHMED+OMRAN&track=backend
    name = request.args.get('slack_name', 'Ahmed Omran')
    track = request.args.get('track', 'backend')
    response = {
    "slack_name": name,
    "current_day": f"{date}",
    "utc_time": f"{time}",
    "track": track,
    "github_file_url": "https://github.com/sapperberet/Backend/blob/main/Stage1/app.py",
    "github_repo_url": "https://github.com/sapperberet/Backend",
    'status_code': 200
    }
    # response.headers['Content-Type'] = 'application/json'
    app.config["JSON_SORT_KEYS"] = False    
    return jsonify(response)

if __name__ == '__main__':
    app.debug = True
    app.run()
