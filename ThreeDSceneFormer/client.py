import requests
from time import time
import json
import gzip
import os

listTime = []
returned_items = []

for i in range(1,6):
    pathIm = "../sample_images/"+str(i)+"/img.jpg"
    pathText = "../sample_images/"+str(i)+"/cam_K.txt"
    if(os.path.isfile(pathIm) and os.path.isfile(pathText) ):
        files = {'photo': open(pathIm, 'rb'), 'cam' : open(pathText,"rb")}
        types_set = {type(value) for value in files.values()}
        start = time()
        response = requests.post(url = "http://localhost:5000/upload", files=files)

        if response.status_code == 200:
            if "error" not in str(response.content): 
                decompressed_data = json.loads(gzip.decompress(response.content).decode())
                listTime.append(time() - start)
                returned_items.append(decompressed_data)
                print("Image "+str(i)+" processed.")
                #uncomment this line to print the totaltime (needed to make plots of response time)
                #print("TotalTime = " + str(listTime))  
                #print(decompressed_data["bdb"][0]["centroid"])   
            #else:
                #print(response.content)

        else:
            print('Error:', response.status_code)
    else:
        print("File not found: "+ str(i))

#Let's save the listTime to a file
with open("listTime.txt", "w") as file:
    file.write(str(listTime))
    file.close()
    
with open("returned_items.json", "w") as file:
    json.dump(returned_items, file)
    file.close()


