import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
class_names = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]
st.header("Image Class Prediction using CNN")
model=load_model("cifar10mod1.h5")
st.markdown("""
Try uploading any of the following types to see whether the model predicts it correctly:

- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck
""")
upl_img=st.file_uploader("Upload Image",type=["png","jpeg","jpg"])

if upl_img is not None:
    img=Image.open(upl_img).convert('RGB')
    st.image(img,caption="Uploaded Image",width="stretch")

    img=img.resize((32,32))
    img_arr=np.array(img)/255.0
    img_arr=np.expand_dims(img_arr,axis=0)
    prob=model.predict(img_arr)
    idx=np.argmax(prob)
    st.subheader(f"Prediction : {class_names[idx].capitalize()}")
    st.subheader(f"Probability : {np.max(prob)*100:.2f}%")