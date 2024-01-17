import os
from roboflow import Roboflow


rf = Roboflow(api_key="rDuXL5zl6C3fhC8peb16")
project = rf.workspace("shubham-karn-jb3zo").project("apples-tppur")
model = project.version(4).model



directory_path = "Apples"
labels = "labels"


for j,filename in enumerate(os.listdir(directory_path)):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        image_name, image_extension = os.path.splitext(os.path.basename(file_path))

        text_filename = image_name + ".txt"

        label_path = os.path.join(labels, text_filename)

        text_content = model.predict(file_path, confidence=40, overlap=30).json()

        pred = text_content['predictions']
        img = text_content['image']
        wid = int(img['width'])
        het = int(img['height'])
        for i in range(len(pred)):
          x = int(pred[i]['x'])
          y = int(pred[i]['y'])
          width = int(pred[i]['width'])
          height = int(pred[i]['height'])
          class_id = int(pred[i]['class_id'])
          a = x/wid
          b = y/het
          c = width/wid
          d = height/het

          text_content = '{} {} {} {} {}\n'.format(class_id,a,b,c,d)

          with open(label_path, "a") as text_file:
            text_file.write(text_content)

        print("{} Text file created with the name: {}".format(j,text_filename))
