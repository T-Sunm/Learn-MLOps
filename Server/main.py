from fastapi import FastAPI
from router.ocr_router import ocr_router
app = FastAPI()


# Định nghĩa route tại đây
@app.get("/")
def read_root():
  return {"message": "Hello, World!"}


app.include_router(ocr_router, prefix="/ocr", tags=["ocr"])

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="127.0.0.1", port=8000)
