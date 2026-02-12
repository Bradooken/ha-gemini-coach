import sys
import json
import urllib.request
import base64
import os

# Arguments passed from Home Assistant
if len(sys.argv) < 3:
    # Fallback for testing without args
    prompt = "A calm morning landscape"
    api_key = "MISSING_KEY" 
else:
    prompt = sys.argv[1]
    api_key = sys.argv[2]

IMAGE_OUTPUT_PATH = "/config/www/daily_briefing_img.jpg"
ERROR_LOG = "/config/www/gemini_error.log"

def generate_image():
    # Using the standard Vertex AI/Imagen 3 endpoint
    url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-001:predict?key={api_key}"
    
    data = {
        "instances": [{"prompt": prompt}],
        "parameters": {"sampleCount": 1, "aspectRatio": "16:9"}
    }

    try:
        req = urllib.request.Request(
            url, 
            data=json.dumps(data).encode('utf-8'), 
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            if 'predictions' in result:
                with open(IMAGE_OUTPUT_PATH, 'wb') as f:
                    f.write(base64.b64decode(result['predictions'][0]['bytesBase64Encoded']))
            else:
                with open(ERROR_LOG, "w") as f:
                    f.write(f"No image data: {json.dumps(result)}")
                    
    except Exception as e:
        with open(ERROR_LOG, "w") as f:
            f.write(str(e))

if __name__ == "__main__":
    generate_image()
