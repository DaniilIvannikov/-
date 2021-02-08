import pygame
import sys


def if_end(mas, sign):
    null = 0
    for i in mas:
        null += i.count(0)
        if i.count(sign) == 3:
            return sign
    for j in range(3):
        if mas[0][j] == sign and mas[1][j] == sign and mas[2][j] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if null == 0:
        return 'Ничья'
    return False


pygame.init()
blsize = 100
margin = 15
width = height = blsize * 3 + margin * 4

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Игра: крестики - нолики')
# цвета в игре:
wiol = (182, 10, 255)  # Фиолетовый
svser = (240, 240, 240)  # Светло-серый
white = (255, 255, 255)  # Белый
blue = (0, 191, 255)  # Голубой
igrok = 0
screen.fill(svser)

mas = [[0] * 3 for i in range(3)]
rez = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not rez:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            j = x_mouse // (blsize + margin)
            i = y_mouse // (blsize + margin)
            if mas[i][j] == 0:
                if igrok % 2 == 0:
                    mas[i][j] = 'X'
                else:
                    mas[i][j] = 'O'
                igrok += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            rez = False
            mas = [[0] * 3 for i in range(3)]
            igrok = 0
            screen.fill(svser)
    if not rez:
        for j in range(3):
            for i in range(3):
                if mas[i][j] == 'X':
                    jor = wiol
                elif mas[i][j] == 'O':
                    jor = blue
                else:
                    jor = white
                x = j * blsize + (j + 1) * margin
                y = i * blsize + (i + 1) * margin
                pygame.draw.rect(screen, jor, (x, y, blsize, blsize))
                if jor == wiol:
                    pygame.draw.line(screen, white, (x + 5, y + 5), (x + blsize - 5, y + blsize - 5), 5)
                    pygame.draw.line(screen, white, (x + blsize - 5, y + 5), (x + 5, y + blsize - 5), 5)
                elif jor == blue:
                    pygame.draw.circle(screen, white, (x + blsize // 2, y + blsize // 2), blsize // 2 - 3, 5)

    if (igrok - 1) % 2 == 0:
        rez = if_end(mas, 'X')
    else:
        rez = if_end(mas, 'O')

    if rez:
        screen.fill(svser)
        font = pygame.font.SysFont('stxingkai', 80)
        text1 = font.render(rez, True, blue)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])

    pygame.display.update()