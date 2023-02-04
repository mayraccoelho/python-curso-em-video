print('=' * 40)
txt = 'Desafio 021 - Tocando um MP3'
print('\33[1:30:41m{:^40}\33[m'.format(txt))
print('=' * 40)

'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''


"""import pygame

pygame.mixer.init()
pygame.mixer.music.load('tudo posso.mp3')
pygame.mixer.music.play()
pygame.event.wait()"""
#nao funcionando

import webbrowser
webbrowser.open('tudo posso.mp3')