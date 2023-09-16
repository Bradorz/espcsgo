import pymem.process
import time
import pygame
import win32api
import win32con
import win32gui

dwGlowObjectManager = (0x535A9C8)
dwEntityList = (0x4DFFEF4)
dwLocalPlayer = (0xDEA964)
dwViewMatrix = (0x4DF0D24)
m_iGlowIndex = (0x10488)
m_iTeamNum = (0xF4)
m_bIsDefusing = (0x997C)
m_iHealth = (0x100)
m_bDormant = (0xED)
m_vecOrigin = (0x138)

Width = 1920
Height = 1080


pygame.init()
mainClock = pygame.time.Clock()
window_screen = pygame.display.set_mode((Width, Height), display = 0, flags = pygame.NOFRAME | pygame.FULLSCREEN)
#window_screen = pygame.display.set_mode((Width, Height), display = 0, flags = pygame.NOFRAME)
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(
                       hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(255, 0, 128), 0, win32con.LWA_COLORKEY)


def GetEntityVars(pm, entity):
    while True:
        try:
            entity_glow = pm.read_uint(entity + m_iGlowIndex)
            entity_team_id = pm.read_uint(entity + m_iTeamNum)
            entity_isdefusing = pm.read_uint(entity + m_bIsDefusing)
            entity_hp = pm.read_uint(entity + m_iHealth)
            entity_dormant = pm.read_uint(entity + m_bDormant)
            x = pm.read_float(entity + m_vecOrigin)
            y = pm.read_float(entity + m_vecOrigin + 0x4)
            z = pm.read_float(entity + m_vecOrigin + 0x8)
        except Exception as e:
            print("GG")
            time.sleep(0.2)
            continue
        return entity_glow, entity_team_id, entity_isdefusing, entity_hp, entity_dormant, x, y, z


def WorldToScreen(x,y,z):
    m11 = pm.read_float(client + dwViewMatrix + 0 * 0x4)
    m12 = pm.read_float(client + dwViewMatrix + 1 * 0x4)
    m13 = pm.read_float(client + dwViewMatrix + 2 * 0x4)
    m14 = pm.read_float(client + dwViewMatrix + 3 * 0x4)

    m21 = pm.read_float(client + dwViewMatrix + 4 * 0x4)
    m22 = pm.read_float(client + dwViewMatrix + 5 * 0x4)
    m23 = pm.read_float(client + dwViewMatrix + 6 * 0x4)
    m24 = pm.read_float(client + dwViewMatrix + 7 * 0x4)

    m31 = pm.read_float(client + dwViewMatrix + 8 * 0x4)
    m32 = pm.read_float(client + dwViewMatrix + 9 * 0x4)
    m33 = pm.read_float(client + dwViewMatrix + 10 * 0x4)
    m34 = pm.read_float(client + dwViewMatrix + 11 * 0x4)

    m41 = pm.read_float(client + dwViewMatrix + 12 * 0x4)
    m42 = pm.read_float(client + dwViewMatrix + 13 * 0x4)
    m43 = pm.read_float(client + dwViewMatrix + 14 * 0x4)
    m44 = pm.read_float(client + dwViewMatrix + 15 * 0x4)

    screenW = (m41 * x) + (m42 * y) + (m43 * z) + m44
    if screenW > 1:
        screenX = (m11 * x) + (m12 * y) + (m13 * z) + m14
        screenY = (m21 * x) + (m22 * y) + (m23 * z) + m24

        camX = Width / 2
        camY = Height / 2

        X = camX + (camX * screenX / screenW)
        Y = camY - (camY * screenY / screenW)
        return (int(X),int(Y))
    else:
        return(-99,-99)


pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
X = Y = X2 = Y2 = 0

done = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = 1

    LocalPlayer = pm.read_int(client + dwLocalPlayer)
    localTeam = pm.read_int(pm.read_uint(client + dwLocalPlayer) + m_iTeamNum)

    window_screen.fill((255, 0, 128))
    for i in range(0, 32):
        entity = pm.read_uint(client + dwEntityList + i * 0x10)
        if entity:
            entity_glow, entity_team_id, entity_isdefusing, entity_hp, entity_dormant, x, y, z = GetEntityVars(pm, entity)
            if entity != LocalPlayer and entity_team_id != localTeam and entity_dormant == 0 and entity_hp > 0:
                X, Y = WorldToScreen(x,y,z)
                X2, Y2 = WorldToScreen(x, y, z+60)
                long = (Y - Y2) / 4
                if X > 0 and X < Width and Y > 0 and Y < Height:
                    pygame.draw.rect(window_screen, (255, 0, 0), pygame.Rect(X2 - long, Y2, long * 2, Y-Y2), 1)
                    #pygame.draw.circle(window_screen, (255,100,0), (X2, Y2-long/3), long/2, 4) #(r, g, b) is color, (x, y) is center, R is radius and w is the thickness of the circle border.
                    hp = int(entity_hp)
                    hp = hp / 100
                    test = (Y - Y2) * hp
                    pygame.draw.rect(window_screen, (255, 102, 0), pygame.Rect(X2 + long/2 , Y2 , long/2, test), 0)

                    # GREEN = (0, 0, 0)
                    # BLUE = (255, 0, 0)
                    # font_obj = pygame.font.Font(pygame.font.get_default_font(), int(long))
                    # text_surface_obj = font_obj.render(hp, True, BLUE)
                    # text_rect_obj = pygame.Rect(X2 - long, Y2, long * 2, Y-Y2)
                    # window_screen.blit(text_surface_obj, text_rect_obj)

    pygame.display.update()
    mainClock.tick(120)