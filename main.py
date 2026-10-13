import onnxruntime as rt
from PIL import Image
import numpy as np


image = Image.open('image.png').convert('L').resize((28,28))

def predict(image):
    image =(np.array(image) / 255).astype('float32').reshape(1,28,28,1)

    ### model
    model_onnx_path = 'mnist.onnx'
    providers = ['CPUExecutionProvider']
    sess = rt.InferenceSession(model_onnx_path,providers=providers)

    ###run
    predict_onnx = sess.run(['dense'],{'args_0':image})
    print(predict_onnx[0].argmax())