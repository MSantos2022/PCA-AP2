import pygame
pygame.init()

tela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Jogo Escreva a Palavra")

janela_aberta = True
while janela_aberta:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            janela_aberta = False

pygame.quit()






            
            
    






    
