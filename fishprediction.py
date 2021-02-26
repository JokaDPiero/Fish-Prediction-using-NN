from keras.models import load_model
import pandas as pd
import numpy as np

def predictions(x):
    labels={'Bream':0, 'Roach':1, 'Whitefish':2, 'Parkki':3, 'Perch':4, 'Pike':5, 'Smelt':6}
    mdl = load_model("fishmodel.h5")
    pred=np.argmax(mdl.predict(x),axis=-1)
    for k,v in labels.items():
        if v==pred:
            return k
def ip():
    i1=float(input("Enter Weight :"))
    i2=float(input("Enter Length1 :"))
    i3=float(input("Enter Length2 :"))
    i4=float(input("Enter Length3 :"))
    i5=float(input("Enter Height :"))
    i6=float(input("Enter Width :"))
    inp=pd.DataFrame([i1,i2,i3,i4,i5,i6],index=['Weight', 'Length1', 'Length2', 'Length3', 'Height',
       'Width']).transpose()
    print("Your input is-")
    print(inp)
    pr=predictions(inp)
    print("The predicted species is: ")
    print(pr)
print("Welcome to fish prediction program!!")
print("_"*40)
while(True):
    ip()
    c=input("Do you want to continue (y/n):")
    if(c=='n' or c=='N'):
        print("Thanks for using our program!")
        break
