from flask import Flask,request,jsonify
from flask_cors import CORS
from transformers import pipeline
# import numpy as np
# import cv2 as cv
# import os
# from inference_sdk import InferenceHTTPClient
# from dotenv import load_dotenv

# load_dotenv()

sentiment_pipeline = pipeline("sentiment-analysis")

# client = InferenceHTTPClient(
#     api_url="https://detect.roboflow.com",
#     api_key=os.getenv("ROBOFLOW_API_KEY")
# )

app = Flask(__name__)
from flask_cors import CORS

CORS(app, resources={
    r"/sentiment": {
        "origins": "*",
        "methods": ["POST"],
        "allow_headers": ["Content-Type"]
    }
})


@app.route("/") 
def home():
    return "Hello World"

@app.route("/sentiment",methods=["POST"])
def sentiment():

    # Get text and image from the request
    text = request.get_json().get('text')
    # image = request.files.get('image')

    text_output=None
    # image_output=None

    if text:
        result = sentiment_pipeline(text)
        text_output=result

    # if (image):
    #     image_bytes = np.frombuffer(image.read(), np.uint8)
    #     image_data = cv.imdecode(image_bytes, cv.IMREAD_COLOR)

    #     # Encode image as base64 for API request
    #     _, buffer = cv.imencode(".jpg", image_data)
    #     image_encoded = buffer.tobytes()

    #     # Send the request to the Roboflow API
    #     response = client.run_workflow(
    #         workspace_name="firsttime-6l8mq",
    #         workflow_id="objectdetection",
    #         images={"image": image_data},
    #         use_cache=True
    #     )
        
    #     # Extract predictions from response
    #     predictions = response[0]["model_predictions"]["predictions"]
    #     image_output=predictions

    result={
        "text":text_output
    }
    
    return jsonify(result),200


if __name__=="__main__":
    app.run(debug=True)