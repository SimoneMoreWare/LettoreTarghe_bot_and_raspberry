# LettoreTarghe_bot_and_raspberry
Come creare un lettore di targhe con bot su Raspberry

Nell’articolo di oggi vedremo come realizzare con Raspberry Pi un sistema automatizzato in grado di leggere le targhe delle auto ogni tot secondi (se presenti) e in tal caso inviare una foto della targa con sotto un messaggio di testo contente le lettere e numeri che compongono la targa.

In questo articolo impareremo a riconoscere e leggere il numero di targa delle automobili utilizzando Raspberry Pi e OpenCV . Per riconoscere la targa utilizzeremo OpenCV Contour Detection con la combinazione di Tesseract OCR.

Componenti:

* Raspberry Pi
* Pi camera
* Librerie

Applicazioni:

* automatizzare i caselli
* scoprire trasgressori
* sistemi di sicurezza automatizzati
* apertura cancelli

Se non hai mai utilizzato prima d’ora la Raspberry Pi Camera dovrai configurala. Per avere maggiori info riguarda la prima configurazione ti invito a leggere il mio articolo: [Come installare e configurare la Raspberry Pi Camera](https://www.moreware.org/wp/blog/2021/08/29/come-configurare-e-installare-la-raspberry-pi-camera/)

Dobbiamo installare poi varie librerie tra cui:

* open cv
* telepot
* Tesseract 
* imutils
 
Ci sono tre passaggi logici fondamentali

* levamento targa
* gmentazione dei caratteri una volta rilevata la targa
* conoscimento dei caratteri con OCR

# tallazioni librerie

Aggiorniamo il Raspberry digitando il seguente comando nel terminale:

`sudo apt-get update`

Usa i seguenti comandi per installare le dipendenze necessarie per l’installazione di OpenCV sul tuo Raspberry Pi.

`sudo apt install libhdf5-dev -y 
sudo apt install libhdf5-serial-dev –y 
sudo apt install libatlas-base-dev –y 
sudo apt install libjasper-dev -y 
sudo apt install libqtgui4 –y 
sudo apt install libqt4-test –y`

Successivamente, usa il comando seguente per installare OpenCV sul tuo Raspberry Pi.

`pip3 install opencv-contrib-python==4.1.0.25`

Per installare Tesseract OCR (Optical Character Recognition) utilizzando l’opzione apt:

`sudo apt install tesseract-ocr`

installa pytesseract con il comando:

`pip3 install pytesseract`

imutils viene utilizzato per semplificare le funzioni di elaborazione delle immagini essenziali come traduzione, rotazione, ridimensionamento e visualizzazione di immagini Matplotlib con OpenCV. Utilizzare il comando seguente per installare imutils:

`pip3 install imutils`

# Configurazione bot telegram

Il primo passo consiste nell’aprire l’applicazione telegram. Una volta aperta cerchiamo “BotFather” tramite la funzione cerca cliccando sull’apposita lente di ingrandimento.

“BotFather” è un bot che permette di creare altri bot.

Avviamo il bot scrivendo “/start“, poi premiamo invio.

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2020/12/bothfather1.png?w=623&ssl=1)

Per creare un nuovo bot digitiamo “/newbot”.

BotFather ci chiederà di assegnare un nome al nostro nuovo Bot, basta digitare un qualsiasi nome e poi premere Invio.

Dobbiamo anche inserire un username che lo renderà riconoscibile pubblicamente. Username deve terminare in “Bot” o ” _bot”.

In seguito alla assegnazione del nome e dell’username BotFather ci comunicherà informazioni importanti in seguito per compilare il codice per il funzionamento della camera e dell’invio dati. ATTENZIONE: QUESTE INFOMAZIONI LE DOVREMMO TENERE SOLO PER NOI. La prima parte riguarda il percorso per trovare il nostro bot. La seconda è la API che sarà utilizzato nel nostro codice.

![alt text](https://i0.wp.com/www.moreware.org/wp/wp-content/uploads/2020/12/botfather2.png?w=618&ssl=1)

Per l’implementazione del bot occorre una specifica libreria. Per installare questa libreria basta eseguire il comando (prima usciamo dalle eventuali directory digitando cd).

`pip install telepot`

Nota bene: telepot oramai non è più supportato, ti consiglio di realizzare il bot con telebot o telethon

# [Codice](https://github.com/SimoneMoreWare/LettoreTarghe_bot_and_raspberry/blob/main/script.py)

Crea la cartella chiamata “timelapse” su desktop, cosi potrai copiare e incollare il codice

Esegui il codice, vai sul bot e scrivi /start, e mettiamo una bella targa davanti alla cam.

Ecco qui il video:

https://www.youtube.com/watch?v=ncQkinVYPnM
