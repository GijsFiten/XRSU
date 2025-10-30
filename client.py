import requests
from time import time
import json
import gzip
import os
import sys

listTime = []
returned_items = []

#check if --save_results has been provided as argument

    

for i in range(1,101):
    pathIm = "./sample_images/"+str(i)+"/img.jpg"
    pathText = "./sample_images/"+str(i)+"/cam_K.txt"
    if(os.path.isfile(pathIm) and os.path.isfile(pathText) ):
        files = {'photo': open(pathIm, 'rb'), 'cam' : open(pathText,"rb")}
        types_set = {type(value) for value in files.values()}
        start = time()
        response = requests.post(url = "http://localhost:5000/upload", files=files)

        if response.status_code == 200:
            if "error" not in str(response.content):
                try:
                    decompressed_data = json.loads(gzip.decompress(response.content).decode())
                    if '--save_results' in sys.argv:
                        listTime.append(time() - start)
                        returned_items.append(decompressed_data)
                    print("Image "+str(i)+" processed in "+str(time() - start)+" seconds")
                    print("Total data size: "+ str(sys.getsizeof(response.content) / 1000000) + " megabytes")
                    del decompressed_data
                except Exception as e:
                    print("Error processing image "+str(i)+":", e)
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
if '--save_results' in sys.argv:
    with open("listTime.txt", "w") as file:
        file.write(str(listTime))
        file.close()
        
    with open("returned_items.json", "w") as file:
        json.dump(returned_items, file)
        file.close()


