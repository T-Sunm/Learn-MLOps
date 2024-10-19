from pydantic import BaseModel
from typing import List, Union

class ocr_output(BaseModel):
  bboxs: List[List[List[float]]]
  texts: List[str]
  score: List[float]

class ocr_response(BaseModel):
    data: ocr_output
    status_code: int
