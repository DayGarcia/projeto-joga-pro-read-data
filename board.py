import socket
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import csv
import json
from time import sleep
import RPi.GPIO as GPIO
from serial import Serial
from random import randrange
from threading import Thread
from datetime import datetime as dt
from numpy import array, concatenate
from decimal import Decimal

import functions.check as check


    
def leitura() -> bool:
    UDP_IP = "192.168.15.149" # IP do meu servidor
    UDP_PORT = 8080 # Aqui devo usar a mesma porta que coloquei no Arduino
    SIZE_PACKET=10 # Tamanho da string que o Arduino ira enviar
    #10,0,0,200
    
    #sock = socket.socket(socket.AF_INET, # Internet
    #socket.SOCK_DGRAM) # DGRAM é para UDP e para TCP seria SOCK_STREAM
    #sock.bind((UDP_IP, UDP_PORT)) # Chamo o bind para associar a porta ao IP no meu sock
    
    print ("Realizando Leitura ") 
    #data, addr = sock.recvfrom(SIZE_PACKET)
    data = "924416"
    print ("")
    # print ("IP :", addr[0])
    print ("Mensagem recebida:", data)
    recebido = str(data)
    recebido = recebido[2:10]
    #print (recebido)
    
    """ ip = str(addr[0])
    date = dt.now().strftime("%d/%m/%Y")
    hour = dt.now().strftime("%H:%M:%S.%f")
    horario = date + ","+hour
    gravacao = horario + "," + ip + "," + recebido
    

    with open("recebimento_de_dados.csv", "a", newline = "") as csvfile:
                    date = dt.now().strftime("%d/%m/%Y")
                    hour = dt.now().strftime("%H:%M:%S")
                    csvfile = csv.writer(csvfile, delimiter = ",")
                    split = gravacao.split(",")
                    row = split[0:16]
                    split = split[16:]
                    csvfile.writerow(row) """
    status = check.is_valid(data)
    return status

    
def escrita(status):
    #MESSAGE = b"{123456F}"
    UDP_IP1 = "192.168.15.100" # IP do meu servidor
    UDP_PORT1 = 8080
    
    
    MESSAGE = str(status).encode("ascii")
    print (status)
    
    print ("Realizando Escrita ") 
       
    #sock = socket.socket(socket.AF_INET, # Internet
                   #     socket.SOCK_DGRAM) # UDP
   # sock.sendto(MESSAGE, (UDP_IP1, UDP_PORT1))
    print ("Enviando Dados")



while True:
    status = leitura()
    escrita(status)
    sleep (5)
