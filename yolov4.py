import subprocess
import os
import pathlib
import joblib
from pathlib import Path

base_path= Path.("root"/"darknet")

def imShow(path):
  import cv2
  import matplotlib.pyplot as plt
  #%matplotlib inline

  image = cv2.imread(path)
  height, width = image.shape[:2]
  resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)

  fig = plt.gcf()
  fig.set_size_inches(18, 10)
  plt.axis("off")
  plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
  plt.savfig('predicted img.jpg')
  #plt.show()

#/home/contact_antrikshlabs_gmail_com/darknet

make = 'make'

proc = subprocess.Popen(['bash -c "'+make+'"'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = proc.communicate()
print(out,err)

dataset = base_path/"Dataset"

names = os.listdir(dataset/"train")

noof_classes = len(names)
with open(base_path/"output"/"obj.names", 'w') as out:
      for name in names:
            #name.replace(" ", "_")
            out.write(name + '\n')


with open(base_path/"output"/"train.txt", 'w') as out:
    for name in names:
        for img in [f for f in os.listdir(dataset/"train"/+str(name)) if f.endswith('jpg')]:
            out.write(str(base_path)+'/Dataset/train/'+ name+'/' +img +'\n')

with open(base_path/"output"/"valid.txt", 'w') as out:
    for name in names:
        for img in [f for f in os.listdir(dataset/"validation"/+str(name)) if f.endswith('jpg')]:
            out.write(str(base_path)+'/Dataset/validation/'+name+ '/'+ img +'\n')


with open(base_path/"output"/"obj.data", 'w') as out:
  out.write('classes ='+ str(noof_classes)+'\n')
  out.write('train ='+str(base_path) +'/output/train.txt\n')
  out.write('valid ='+str(base_path) +'/output/valid.txt\n')
  out.write('names ='+str(base_path)+'/output/obj.names\n')
  out.write('backup ='+str(basepath)+'/output')

obj_path = str(base_path)+'/output/obj.data'
cfgfile = str(base_path)+'/cfg/yolov4-custom.cfg'
weight_path = str(base_path)+'/yolov4.conv.137'
train_command = './darknet detector train'+" "+ str(obj_path)+" "+ str(cfgfile)+" "+ str(weight_path)+ " "+'-dont_show -map'

proc = subprocess.Popen(['bash -c "'+train_command+'"'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
out, err = proc.communicate()

print(out,err)








