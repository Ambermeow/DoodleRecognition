import pandas as pd
import numpy as np
import csv
import math
import os
import os.path
fr=open('train_list.txt')
filenames=[line.strip('\n').replace('_',' ') for line in fr.readlines()]
fr.close()
#filenames=filenames[0:2]
print(filenames)


for filename in filenames:
    ff=pd.read_csv("Data/train_data/"+filename)
    for i in range(len(ff)):
    #for i in range(1000):
        ran_int=math.floor(np.random.rand()*100)
        shuffled_filename="Data/Shuffled_train_data/train_"+str(ran_int)+".csv"
        #print(shuffled_filename)
        #print(ff.iloc[i])
        if os.path.exists(shuffled_filename):
            
            with open(shuffled_filename, 'a') as f:
                ff.iloc[i:i+1].to_csv(f,header=False)
            
        else:
            #print("not_exist")
            with open(shuffled_filename, 'w') as f:
                ff.iloc[i:i+1].to_csv(f,header=True)


