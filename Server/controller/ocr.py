import easyocr


def create_reader(languages: list):
  return easyocr.Reader(languages, gpu=False)

def extract_ocr(input_image, language):
  EASY_OCR = create_reader(language)
  ocr_result = EASY_OCR.readtext(input_image, slope_ths=0.5,
                                 height_ths=1.0, width_ths=1.5)

  texts = []
  confidents_level = []
  bboxs = []
  for results in ocr_result:
    bbox = [[float(coord[0]), float(coord[1])] for coord in results[0]]
    # Chuyển đổi mỗi tọa độ về kiểu int
    bboxs.append(bbox)
    texts.append(results[1])
    confidents_level.append(float(results[2]))

  return (bboxs, texts, confidents_level)
