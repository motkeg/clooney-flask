
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

labels = ["brad" , "clooney" , "dicaprio" ,"matt"]



def parse_score(score):
    indx  = list(score).index(max(score))
    return labels[indx]

def procces_img(path , url = False):
  
    img = Image.open(path).resize((224,224))
    x = img_to_array(img)
    x = np.expand_dims(x,0)
    return x

def get_result(path):

    MODEL = load_model("clooney_model/_cnn_clooney.best_v2.hdf5")
    x = procces_img(path)
    res = MODEL.predict(x)
    return parse_score(res[0])
    

