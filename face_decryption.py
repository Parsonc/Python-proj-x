import cv2
import numpy as np
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".",",","?"," ",]
def camera_access():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    while True:
        ret,img = cap.read()
        gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        front_faces = face_cascade.detectMultiScale(gray_scale,1.3,5)
        for (x,y,w,h) in front_faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray_scale[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        cv2.imshow('processing',img)
        q = cv2.waitKey(30) & 0xff
        if q==27:
            break
    cap.release()
    cv2.destroyAllWindows()
def encryption(plaintext):
    cipher = ""
    for i in plaintext:
        ciphertext_index1=(alpha.index(i))
        ciphertext_index2=((((ciphertext_index1*7)%30)-7)%30)
        ciphertext_display=alpha[ciphertext_index2]
        cipher += ciphertext_display
    return(cipher)
def decryption(ciphertext):
    plaintext = ""
    for i in ciphertext:
        plaintext_index1=(alpha.index(i))
        plaintext_index2=((((plaintext_index1+7)%30)*13)%30)
        plaintext_display=alpha[plaintext_index2]
        plaintext+=plaintext_display
    return (plaintext)
def main():
    choice_accepted=["0","1","2","3"]
    choice=""
    while choice!="0":
        choice = input("Press 1 then Enter to Encrypt\nPress 2 then Enter to Decrypt\nPress 3 then Enter to Register your Face\nPress 0 then Enter to Exit Program\n")
        if choice not in choice_accepted:
            print("Invalid Option!.Please read the following instructions and try again") 
        if choice == "1":
            msg1=input("Enter message to Encrypt\n")
            encrypted_msg = encryption(msg1)
            print ("Your Encrypted Message is:\n",encrypted_msg)
        if choice == "2":
            msg2 = input("Enter messge to Decrypt\n")
            decrypted_message=decryption(msg2)
            print ("Your Decrypted Message is:\n",decrypted_message)
        if choice == "0":
            print("Thank you for using my Program!")
            break
        if choice == "3":
            camera_access()
   
main ()





