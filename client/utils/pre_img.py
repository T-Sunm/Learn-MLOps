from PIL import Image, ImageDraw, ImageFont
import io
import base64
import numpy as np

def encode_image(image_path):
  image = Image.fromarray(image_path)

 # chuyển đổi thành byte
  buffered = io.BytesIO()
  image.save(buffered, format="PNG")
  img_byte_arr = buffered.getvalue()

  return img_byte_arr


def plot_bbox(ocr_result, image):
  bboxs = ocr_result['bboxs']
  texts = ocr_result['texts']
  confidents_level = ['score']

  # Chuyển đổi hình ảnh thành đối tượng PIL Image
  image = Image.fromarray(image)

  # Tạo đối tượng vẽ trên ảnh
  draw = ImageDraw.Draw(image)

  # Vẽ bounding box và label
  for i, box in enumerate(bboxs):
    # Chuyển đổi mỗi tọa độ về kiểu int và làm phẳng các tọa độ
    coordinates = np.array(box, dtype=int)

    # x1,y1,x2,y2,x3,y,x4,y4
    box_flattened = coordinates.flatten()

    draw.polygon(box_flattened.tolist(), outline="red", width=3)

    # Lấy văn bản từ kết quả OCR
    label = texts[i]
    padding = 10

    # Tạo đối tượng phông chữ
    font_size = 20
    font = ImageFont.truetype(
        "./fonts/JetBrainsMono-Medium.ttf", size=font_size)

    # Lấy tọa độ góc trái trên của bounding box
    top_left = (box_flattened[0], box_flattened[1] - 30)

    # Sử dụng textbbox() để tính toán kích thước của văn bản
    text_bbox = draw.textbbox(top_left, label, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Xác định tọa độ của hình chữ nhật nền cho label
    background_box = [
        (top_left[0], top_left[1]),  # Góc trên trái
        (top_left[0] + text_width + padding, top_left[1] + \
         text_height + padding)  # Góc dưới phải
    ]

    draw.rectangle(background_box, fill="yellow")

    draw.text(top_left, label, font=font, fill="black")

  return image
