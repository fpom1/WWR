from PIL import Image as im
import numpy as np
import random
import csv

def randomazzio(entries):
    rand = []
    for i in range(entries):
        rand.append(random.randint(0,255))
    return rand

def arrlist(arr):
    values = []
    for i in range(len(arr)):
        arr_row = arr[i]
        for i in range(len(arr_row)):
            arr_entry = arr_row[i]
            for i in range(len(arr_entry)):
                values.append(int(arr_entry[i]))
    return values

def modarrlist(entries,arr):
    rando = randomazzio(entries)
    array = arrlist(arr)
    for i in range(len(array)):
        if array[i]+rando[i%entries] > 255:
            array[i] = array[i]+rando[i%entries]-256
        else:
            array[i] = array[i]+rando[i%entries]
    return (rando,array)

def demodarrlist(key,arr):
    array = arrlist(arr)
    for i in range(len(array)):
        if array[i]-int(key[i%len(key)]) < 0:
            array[i] = array[i]-int(key[i%len(key)])+256
        else:
            array[i] = array[i]-int(key[i%len(key)])
    return (array)

def show_img(arr):
    array= arr.astype(np.uint8)
    image = im.fromarray(array)
    image.show()
    return image

def rearray(lis,arr):
    for row_index in range(len(arr)):
        rows = len(arr)
        for column_index in range(len(arr[row_index])):
            columns = len(arr[row_index])
            for entry_index in range(len(arr[row_index][column_index])):
                entries = len(arr[row_index][column_index])
                row_index_value = row_index*columns*entries
                column_index_value = column_index*entries
                entry_index_value = entry_index
                index = row_index_value+column_index_value+entry_index_value
                arr[row_index][column_index][entry_index] = lis[index]
    return arr

def imgscrambler(key_len,img,image_name):
    img_array = np.array(im.open(img))
    modlist = modarrlist(key_len,img_array)
    keyholder = []
    keycode = modlist[0]
    codelist = modlist[1]
    keyholder.append(keycode)
    scrambled_array = rearray(codelist,img_array)
    image = show_img(scrambled_array)
    image.save(image_name+".png")
    with open(image_name+"_key.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(keyholder)

def imgdescrambler(key_file,img):
    with open(key_file) as f:
        reader = csv.reader(f)
        examples = list(reader)
    key = examples[0]
    img_array = np.array(im.open(img))
    normlist = demodarrlist(key,img_array)
    normarray = rearray(normlist,img_array)
    image = show_img(normarray)


#set these variables in order to encrypt your normal image
#name of the image you want to encrypt
image = 'Images/twitter.png'
#size of the key used to encrypy you image
key_len = 25
#the name of the new image and key files that will be created
#the image will be saved as new_name+".png", and the key will be saved as new_name+"_key.csv"
new_name = 'new_image'

#set these variables in order to decrypt your encrypted image
#the name of the image you wish to decrypt.
encrypted = 'new_image.png'
#the name of the key you will use to decrypt the image
key_file = 'new_image_key.csv'


#this function will encrypt your image
imgscrambler(key_len,image,new_name)

#this function will decrypt your image
imgdescrambler(key_file,encrypted)








