import os
import random
import numpy as np
import nibabel as nib
tac_image = os.path.join("images", 'volume-55.nii.gz')
label = os.path.join("images", 'labels-55.nii.gz')
np.set_printoptions(precision=2, suppress=True)
img = nib.load(tac_image)
data = img.get_fdata()
img_label = nib.load(label)
label_array = img_label.get_fdata()
print(f" l'array di dati estratto è del tipo: {type(data)}")
print(f" le dimensioni sono: {data.shape} ")
print(f" le dimensioni sono: {label_array.shape} ")
print('insert x value (not a pair value)')
x = int(input())  #lato del quadrato
if x % 2 == 0:
    print('pair value not admitted')
    exit()
print('insert y value (not a pair value)')
y = int(input()) #lato del quadrato
if y % 2 == 0:
    print('pair value not admitted')
    exit()
#print('insert the index of the slice on z axis to extract')
#z = 0
x_i = (x - 2)
x_f = (x + 3)
y_i = (y - 2)
y_f = (y + 3)
l = ((x-1)/2)+1
i_sup=data.shape[0]-l #limiti sup e inf per i problemi di bordo
i_inf=(x-1)/2
j_inf=(y-1)/2
m = ((y-1)/2)+1
j_sup=data.shape[1]-m
k_sup = data.shape[2]-1
print(k_sup)
with open('training_set.txt', 'w') as outfile:
  for k in range(0,400):
    z = random.randint(0, k_sup)
    print(f'z= {z}')
    for i in range(0,500):
        x_c=random.randint(i_inf, i_sup)  #pixel centrale
        y_c=random.randint(j_inf, j_sup)  #pixel centrale
        x_i=int((x_c-((x-1)/2)))
        x_f=int((x_c+(((x-1)/2)+1)))
        print(f'x_i={x_i}')
        print(f'x_f={x_f}')
        y_i=int((y_c-((y-1)/2)))
        y_f=int((y_c+(((y-1)/2)+1)))
        print(f'y_i={y_i}')
        print(f'y_f={y_f}')
        square = data[x_i:x_f, y_i:y_f, z] #estrazione del quadratino fissato z
        print(f'il quadrato estratto è : {square}')
        print(f'le dimensioni di square: {square.shape}')
        #contatore_2=0
        label_px = label_array[x_c, y_c, z] #estrazione pixel centrale dall'immagine segmentata
        #contatore_2=0
        if label_px == 0:
            q = square
            q = np.append(square, label_px)
            q = q.reshape(1, ((x * y) + 1))
            # contatore_2 += 1
           # if contatore_2 % 2 != 0:
            continue
        else:
                t=square
                t = np.append(square, label_px)
                print(t)
        #print(f"la sequenza di pixel che saranno esportati in un file txt è: {t} ")
                t = t.reshape(1, ((x*y)+1))
        #np.savetxt('export.txt', t, delimiter=',', fmt='%i')
                np.savetxt(outfile, t, delimiter=',', fmt='%-7.2f') #esportazione su una riga di un file di testo con delimitatore virgola
                np.savetxt(outfile, q, delimiter=',', fmt='%-7.2f')