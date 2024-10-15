from fastapi import APIRouter, UploadFile, File, Form, status, HTTPException
from controller.ocr import extract_ocr
import json
from schemas import ocr_output

ocr_router = APIRouter()

# FastAPI yêu cầu rằng các giá trị khác ngoài file (dữ liệu text) trong cùng request cũng phải được gửi dưới dạng form-data, và Form được sử dụng để nhận các giá trị đó.

@ocr_router.post("/predict", status_code=status.HTTP_200_OK)
async def predict_ocr(
    file_upload: UploadFile = File(...),
    languages: str = Form(...)
):
  # Đọc file upload
  file_name = file_upload.filename
  file_content = await file_upload.read()

  languages_list = json.loads(languages)
  bboxs, texts, confidents_level = extract_ocr(file_content, languages_list)
  print(languages)
#   if "lỗi":
#     raise HTTPException(status_code=404, detail='Band not Found')
  return ocr_output(
      bboxs=bboxs,
      texts=texts,
      score=confidents_level
  )
