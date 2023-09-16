import pygame
import win32api
import win32con
import win32gui

pygame.init()
mainClock = pygame.time.Clock()
window_screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Collision Detection')
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 600, 300, 0, 0, win32con.SWP_NOSIZE)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(
                       hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 0, 128), 0, win32con.LWA_COLORKEY)


done = 0
i = 50
while not done:
    for event in pygame.event.get():
        # Checking if quit button is pressed or not
        if event.type == pygame.QUIT:
            #  If quit then store true
            done = 1
        # Checking if the escape button is pressed or not
        if event.type == pygame.KEYDOWN:
            # If the escape button  is pressed then store true in the variable
            if event.key == pygame.K_ESCAPE:
                done = 1

    window_screen.fill((255, 0, 128))
    pygame.draw.line(window_screen, (255, 0, 0), (11, 22), (66, 66))

    pygame.draw.rect(window_screen, (0, 0, 255),
                     [100, 100, 400, 100], 0)


    pygame.display.update()
    mainClock.tick(120)

