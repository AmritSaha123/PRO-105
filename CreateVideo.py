import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        images.sort()
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
print(frame.shape)
height,width,channels = frame.shape
size = (width,height)
print(size)
out = cv2.VideoWriter("video1.mp4",cv2.VideoWriter_fourcc(*'DIVX'),1,size)
for i in range(0,count-1,1):
    frame = cv2.imread(images[i])
    print(images[i])
    out.write(frame)
out.release()
print("done")