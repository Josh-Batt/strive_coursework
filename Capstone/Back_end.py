'''
Imports
'''
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
#%matplotlib.inline
from deepface import DeepFace

import os
import collections

'''
Verify
'''
def verify(img1_path, img2_path):
    match = None

    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # plt.imshow(img1[:, :, ::-1 ]) # SHOWS IMAGES
    # plt.show()
    # plt.imshow(img2[:, :, ::-1 ])
    # plt.show()

    result = DeepFace.verify(img1_path, img2_path, model_name='Facenet512', distance_metric='euclidean_l2', enforce_detection=False)
    list_result = list(result.items())
    #print('Result:\t', list_result) #RESULTS

    if list_result[1][1] > 1.15: # CHANGE HOW SIMILAR THE PHOTOS NEED TO BE
        print('You DONT look alike!')
    else:
        match = True
        print('Match = ' + str(match) + '! You DO look alike')
  
    return match

'''
Full Match
'''
def full_match(requests, profile):
    directory = 'DEMO_Profiles/'
    match = None

    holder = requests
    requests = profile
    request_paths = []
    for dirpath, subdirs, files in os.walk(directory):
        for x in files:
            if x.endswith('request_' + str(requests) + '.jpg'): # CHANGE FILE END NAME
                request_paths.append(os.path.join(dirpath, x))
    print(request_paths)

    profile = holder
    pic_paths = []
    for dirpath, subdirs, files in os.walk(directory):
        for x in files:
            if x.endswith('pp_' + str(profile) + '.jpg'): # CHANGE FILE END NAME
                pic_paths.append(os.path.join(dirpath, x))
    print(pic_paths)

    for i in request_paths:
        for j in pic_paths:
            result = verify(i, j)
            if result == True:
                match = True
        
    if match == True:
        return print('Its a MATCH!')
    if match != True :
        return print('No Match!')

'''
Matching Algorithm
'''
def matching_algo():
    directory = 'DEMO_Profiles/'
    
    requests = 1
    request_paths = []
    for dirpath, subdirs, files in os.walk(directory):
        for x in files:
            if x.endswith('request_' + str(requests) + '.jpg'): # CHANGE FILE END NAME
                request_paths.append(os.path.join(dirpath, x))
    print(request_paths)

    profile = 2
    pic_paths = []
    for dirpath, subdirs, files in os.walk(directory):
        for x in files:
            if x.endswith('pp_' + str(profile) + '.jpg'): # CHANGE FILE END NAME
                pic_paths.append(os.path.join(dirpath, x))
    print(pic_paths)
    return request_paths, pic_paths
    # with open("request_paths.txt", "r+") as output:
    #     for row in request_paths:
    #         output.write(str(row)+"\n")  

    # with open('profile_paths.txt', 'r+') as output:
    #     for row in pic_paths:
    #         output.write(str(row)+'\n')          

# if __name__ == '__main__':
#     request_paths, pic_paths = matching_algo()
    # half = None

    # for j in request_paths:
    #     for k in pic_paths:
    #         result = verify(j, k)
            
    #         if result == True:
    #             half = True

    # if half == True:
    #     print('Half Match!')
    #     full_match(1, 2)
    # else:
    #     print('No Half-Match')