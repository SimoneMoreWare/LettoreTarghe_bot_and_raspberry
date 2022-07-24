import telepot
import time
import os
import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image 
from picamera import PiCamera

#inizializzo camera a una risoluzione HD
camera = PiCamera ()
camera.resolution = (1024,720)


# Handling message from Telegram
def handleMessage(msg):
    i=0
#con questo ciclo while avremo modo di avere un loop infinito quindi potremmo analizzare continuamente le varie immagini scattate in un intervallo di tempo X
    while True:
        id = msg['chat']['id']
        camera.capture("/home/pi/Desktop/timelapse/image{0:04d}.jpg".format(i)) #scatto foto che sono inserite nella cartella timelapse
        stringa="/home/pi/Desktop/timelapse/image{0:04d}.jpg".format(i) #mi servirà dopo per agevolare l'inivio della foto su telegram
        img = cv2.imread(str("/home/pi/Desktop/timelapse/image{0:04d}.jpg".format(i)),cv2.IMREAD_COLOR)
        
        i=i+1
     
     
        img = cv2.resize(img, (1024,720) )
     
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
        gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
        edged = cv2.Canny(gray, 30, 200) #Perform Edge detection #rilevamento dei bordi.
     
        # find contours in the edged image, keep only the largest
        # ones, and initialize our screen contour
        cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

# Una volta rilevati i contorni li ordiniamo dal grande al piccolo e consideriamo solo i primi 10 risultati ignorando gli altri.&nbsp;
#Nella nostre immagini potrebbero essercizi immagini contenti in un piano chiuso e tra questi piani c'è anche la nostra targa 
#Per filtrare l'immagine della targa tra i risultati ottenuti,
#esamineremo tutti i risultati e verificheremo quale ha un contorno a forma 
#di rettangolo con quattro lati e una figura chiusa. Dal momento che una 
#targa sarebbe sicuramente una figura rettangolare a quattro lati.

        cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10] 
        screenCnt = 0
     
        # loop over our contours,  cercare i contorni sulla nostra immagine
        for c in cnts:
         # approximate the contour
         peri = cv2.arcLength(c, True)

#Il valore 0,018 è un valore sperimentale; puoi giocarci intorno per 
#verificare quale funziona meglio per te. per chi ha dimestichezza potrebbe utilizzare modelli di appredimento automatico addestrati
#Una volta trovato il valore giusto lo salviamo in una variabile 
#chiamata screenCnt e poi disegniamo un rettangolo attorno ad esso per 
#assicurarci di aver rilevato correttamente la targa.

         approx = cv2.approxPolyDP(c, 0.018 * peri, True) 
         
         # if our approximated contour has four points, then
         # we can assume that we have found our screen
         if len(approx) == 4:
            screenCnt = approx
            break
        if screenCnt is 0:
            detected = 0
            print ("No contour detected")
        else:
         detected = 1
     
        if detected == 1:
            cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
            mask = np.zeros(gray.shape,np.uint8)
            new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
            new_image = cv2.bitwise_and(img,img,mask=mask)
        # Masking the part other than the number plate
        
     
            # Now crop 
            #maschero l'intera immagine tranne la regione della targa , ritagliamo l area della targa e la salviamo in una immagine
            (x, y) = np.where(mask == 255)
            (topx, topy) = (np.min(x), np.min(y))
            (bottomx, bottomy) = (np.max(x), np.max(y))
            Cropped = gray[topx:bottomx+1, topy:bottomy+1]
         
            #Read the number plate
            text = pytesseract.image_to_string(Cropped, lang='eng', config='--psm 13') #rilevamento targa come stringa
            result = "targa "+text 
            print("Detected Number is:",text.strip())
            bot.sendPhoto(id, open(stringa, 'rb')) #mando foto al bot
            bot.sendMessage(id, result) #manda la targa come stringa al bot

         
            #cv2.imshow('image',img)
            #cv2.imshow('Cropped',Cropped)
        time.sleep(20)
     
 
bot = telepot.Bot("YOURAPIKEY") #sostituisci la api key che hai trovato prima
bot.message_loop(handleMessage); #la funzione handleMessage viene chiamata
print ("Listening to bot messages….");
while 1:
    time.sleep(4000);     
