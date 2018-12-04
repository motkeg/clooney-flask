
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.backend import clear_session
from PIL import Image
import os 


labels = ["brad" , "clooney" , "dicaprio" ,"matt"]


def parse_score(score):
    if max(score) <=0.1:
        return "None"
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
    res = MODEL.predict(x ,steps=1)
    clear_session()
    return parse_score(res[0])

def get_batch():
    imgs =[]
    names = []
    
    MODEL = load_model("clooney_model/_cnn_clooney.best_v2.hdf5")

    for imgname in os.listdir(os.path.join("uploads/")):
        names.append(imgname)
        img = Image.open(f"uploads/{imgname}").resize((224,224))
        x = img_to_array(img) 
        imgs.append(x)
    imgs = np.asarray(imgs)
    score = MODEL.predict(imgs)
    score = [parse_score(i) for i in  score]
    #return score
    rows = [[n,l] for n,l in zip(names, score) ]
    # clear the model from the memorey
    clear_session()
    return   [['image name' , 'label']] + rows 



    

