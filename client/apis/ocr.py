import requests
import numpy as np
from utils.pre_img import encode_image, plot_bbox
import json
import os
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL", "http://0.0.0.0:8000")


def ocr_api(image_path: np.ndarray, languages: list[str]):

  img_byte_arr = encode_image(image_path)

  url = f"{BACKEND_URL}/ocr/predict"
  files = {"file_upload": ("image.jpg", img_byte_arr, "image/jpeg")}
  option = {
      "languages": json.dumps(languages)
  }

  response = requests.post(url, files=files, data=option)

  image_bbox = plot_bbox(response.json(), image_path)
  return image_bbox
