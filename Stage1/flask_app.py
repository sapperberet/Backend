# # from flask import Flask, jsonify, request
# # from fastapi import FastAPI, Query
# # from datetime import *
# # # app = Flask(__name__)
# # # new=datetime.now()
# # # new=new+timedelta(hours=-3)
# # # new=new.strftime("%Y-%m-%dT%H:%M:%SZ")
# # # @app.route('/api', methods=['GET'])
# # app = FastAPI()
# # @app.get("/api")
# # async def root(slack_name: str = Query(""), track: str = Query("")):
# #     date =  datetime.utcnow().strftime("%A")
# #     time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
# #     # name = request.args.get('slack_name', 'Ahmed Omran')
# #     # track = request.args.get('track', 'backend')
# #     data = {
# #     "slack_name": slack_name,
# #     "current_day": date,
# #     "utc_time": time,
# #     "track": track,
# #     "github_file_url": "https://github.com/sapperberet/Backend/blob/main/Stage1/app.py",
# #     "github_repo_url": "https://github.com/sapperberet/Backend",
# #     'status_code': 200
# #     }
# #     return data
# #     # response = jsonify(data)
# #     # response.headers['Content-Type'] = 'application/json'
# #     # app.config["JSON_SORT_KEYS"] = False
# #     # return response

# # if __name__ == '__main__':
# #     import uvicorn
# #     # app.debug = True
# #     # app.run()
# from fastapi import FastAPI, Query
# from datetime import datetime, timedelta
# import pytz

# app = FastAPI()


# @app.get("/api")
# async def root(slack_name: str = Query(""), track: str = Query("")):

#     current_day = datetime.utcnow().strftime("%A")
#     utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

#     response_data = {
#     "slack_name": slack_name,
#     "current_day": current_day,
#     "utc_time": utc_time,
#     "track": track,
#     "github_file_url": "https://github.com/MichaelHopeDavid/HNGT1_Endpoint/blob/master/main.py",
#     "github_repo_url": "https://github.com/MichaelHopeDavid/HNGT1_Endpoint/tree/master",
#     "status_code": 200
#     }

#     return response_data


# if __name__ == "__main__":
#     import uvicorn
#     # app.json.sort_keys = False
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    current_day = datetime.datetime.utcnow().strftime('%A')
    current_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time,
        "track": track,
        "github_file_url": "https://github.com/sapperberet/Backend/blob/main/Stage1/app.py",
        "github_repo_url": "https://github.com/sapperberet/Backend",
        "status_code": 200
    }
    return jsonify(response)
# https://sapperberet.pythonanywhere.com/api?slack_name=Ahmed+Omran&track=backend