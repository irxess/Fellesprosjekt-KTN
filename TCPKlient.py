import pygame
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(('localhost', 9007))

while True:
    connection.send(str(raw_input("skriv noe: ")))

