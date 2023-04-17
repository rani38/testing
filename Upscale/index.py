from flask import Flask
import gradio as gr
import os

app = Flask("__name__")

@app.route('/')
def fun():

    load_spaces = gr.load(name="doevent/Face-Real-ESRGAN", src="spaces")
    filepath = "image1.jpg"
    response = load_spaces(filepath, "2x",  fn_index=0)
    print(response)
    return response

if __name__ == "__main__":
    app.run()