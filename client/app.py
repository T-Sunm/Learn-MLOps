import gradio as gr
from apis.ocr import ocr_api

# Định nghĩa biến demo ở phạm vi toàn cục
choices = ["vi", "en", "ko", "ch_sim"]
demo = gr.Interface(
    fn=ocr_api,
    inputs=["image",
            gr.CheckboxGroup(choices=choices, label="Languages")],
    outputs=["image"],
)

if __name__ == "__main__":
  demo.launch(server_name="127.0.0.3",
              server_port=3000,
              share=False)
