import pandas as pd
import re
import numpy as np
import multiprocessing



# Reading File
knowledge_base_data = pd.read_csv("input_data.csv")
data = knowledge_base_data[:]

complete_corpus = []
for i in range(len(data)):
    complete_corpus.append(data.loc[i,"data"])
    
nphi = len(complete_corpus)

str_complete_corpus = []
for i in range(len(complete_corpus)):
    str_complete_corpus.append(str(complete_corpus[i]))
    
complete_data = "".join(str(complete_corpus))

text_file = open("Output.txt", "w")
text_file.write(complete_data)
text_file.close()

len(complete_data)


stre = complete_data
my_new_string = re.sub('[^ a-zA-Z0-9]', '', stre)



dataf = []


dataf.append(data["Commands"].tolist())
dataf.append(data["data"].tolist())
dataf[1][276] = "nnn"
dataffin = []

for i12 in range(nphi):
    dataf[1][i12] = dataf[1][i12].split()    
    a = len(dataf[1][i12])
    a11 = []
    i=0
    while i<a:
        if len(dataf[1][i12][i]) > 3:
            a11.append(dataf[1][i12][i])
        i+=1
    dataffin.append(a11)

dataf = []


dataf.append(data["Commands"].tolist())
dataf.append(dataffin)
nphi = len(dataffin)
num_arr_123 = []
for i in range(nphi):
    num_arr_123.append(len(dataf[1][i]))
    
   
np.mean(num_arr_123)
    
q12 = 0
a12 = nphi
while q12<a12:
    if len(dataf[1][q12]) > 4000:
        del(dataf[1][q12])
        del(dataf[0][q12])
        a12-=1
    q12+=1



nphi = len(dataffin)
    
  
a1 = []
for i in range(nphi):
    a1.append(0)

fast = [] 
for i in range(nphi):
    fast.append(i)

mn = [0]
mn[0] = -1
a2 = []

guestFile = open("guestList.csv","w")
guestFile.close()

# Main function supporting Parallel Computing, Append used instead
def calc(i):
    a2 = []
    for i1 in range(nphi-1):
        a2.append(0)
    a2[0] = i
    mn[0] += 1
    ophi = -1
    for j in range(nphi):
        if i!=j:
            ophi += 1            
            for k in range(len(dataf[1][i])):
                for l in range(len(dataf[1][j])):
                    if dataf[1][i][k] == dataf[1][j][l]:
                        a2[ophi] += 1
            print(str(i)+"---------------"+str(j)+"/"+str(nphi)+"---")           
    max_arr = [0,0,0,0,0]
    max_arr[0] = np.argmax(a2)
    a2[np.argmax(a2)] = 0
    max_arr[1] = np.argmax(a2)
    a2[np.argmax(a2)] = 0    
    max_arr[2] = np.argmax(a2)
    a2[np.argmax(a2)] = 0
    max_arr[3] = np.argmax(a2)
    a2[np.argmax(a2)] = 0
    max_arr[4] = np.argmax(a2)
    for j1 in range(5):
        if max_arr[j1] >= i:
            max_arr[j1] += 1  
    print(max_arr)
    for entries in max_arr :
        guestFile = open("guestList.csv","a")
        guestFile.write(knowledge_base_data.loc[i,"Commands"]+","+knowledge_base_data.loc[entries,"Commands"]+","+str(i))
        guestFile.write("\n")
    guestFile.close()
    print(str(i)+"/"+str(nphi))    





# Run on a GPU
pool = multiprocessing.Pool(processes=100)
r = pool.map(calc, fast)
pool.close()
