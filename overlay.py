import time
import pygame
import win32api
import win32con
import win32gui



class Overlay1:
    def __init__(self):
        #Overlay1.__init__(self)
        self.x = 0
        self.y = 0

    def refresh1(self, x, y):
        self.x = x
        self.y = y

    def start(self):
        self.coords = 1
        pygame.init()
        # initialize the pygame window
        window_screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Collision Detection')

        # for borderless window use pygame.Noframe
        # size of the pygame window will be of width 700 and height 450
        hwnd = pygame.display.get_wm_info()["window"]

        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 600, 300, 0, 0, win32con.SWP_NOSIZE)
        # Getting information of the current active window
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(
                               hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 0, 128), 0, win32con.LWA_COLORKEY)
        # This will set the opacity and transparency color key of a layered window
        font = pygame.font.SysFont("Times New Roman", 54)
        # declare the size and font of the text for the window
        text = []
        # Declaring the array for storing the text
        text.append((font.render("Transparent Window", 0, (255, 100, 0)), (20, 10)))
        text.append((font.render("Press Esc to close the window", 0, (255, 100, 100)), (20, 250)))
        # Appending the text in the array


        def show_text():
            for t in text:
              #  For loop for calling every element in the text
                window_screen.blit(t[0], t[1])
                 # Blit is for block transfer

        done = 0
        i = 50
        while not done:
            # Accessing the event if any occurred
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
             # Transparent background
            window_screen.fill((255,0,128))
            #  Calling the show_text function
            #show_text()
            player = pygame.Rect(200, i, 200, 200)
            pygame.draw.rect(window_screen, (0, 0, 0),player)
            pygame.draw.line(window_screen, (0, 0, 255), (0, 0), (639 + self.x, 479 + self.y))
            i += 1
            time.sleep(0.1)
            #  Checking for the update in the display
            pygame.display.update()
            print(self.x, self.y)