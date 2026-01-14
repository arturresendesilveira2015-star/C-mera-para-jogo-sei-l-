import pyautogui
import time
import cv2
import numpy as np

def proximo_de_preto(cor):
    if sao_proximas(cor) and cor[0] + cor[1] + cor[2] < 180:
        return True
    else:
        return False

def sao_proximas(cor):
    maximo = [0, 0, 0]
    minimo = [0, 0, 0]
    for i in range(3):
        maximo[i] = cor[i] + 5
        minimo[i] = cor[i] - 5
    o_que_retornar = True
    for x in range(3):
        for i in range(3):
            if cor[i] < minimo[x] or cor[i] > maximo[x]:
                o_que_retornar = False
    return o_que_retornar

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Erro: não foi possível acessar a webcam.")
    exit()

while True:
    ret, frame = camera.read()
    if not ret:
        print("Erro ao capturar o frame.")
        break

    h, w = frame.shape[:2]       
    cx, cy = w // 2, h // 2
    for x in range(50, 100):
        for i in range(100, 150):
            b, g, r = frame[x, i].tolist()
            cores = [r, g, b]
            if proximo_de_preto(cores):
                pyautogui.press('w')
                break
        for i in range(200, 250):
            b, g, r = frame[x, i].tolist()
            cores = [r, g, b]
            if proximo_de_preto(cores):
                pyautogui.press('a')
                break
        for i in range(300, 350):
            b, g, r = frame[x, i].tolist()
            cores = [r, g, b]
            if proximo_de_preto(cores):
                pyautogui.press('s')
                break
        for i in range(400, 450):
            b, g, r = frame[x, i].tolist()
            cores = [r, g, b]
            if proximo_de_preto(cores):
                pyautogui.press('d')
                break
        for i in range(500, 550):
            b, g, r = frame[x, i].tolist()
            cores = [r, g, b]
            if proximo_de_preto(cores):
                pyautogui.click()
                break
    for i in range(150, h - 150):
        b, g, r = frame[i, 50].tolist()
        cores = [r, g, b]
        if proximo_de_preto(cores):
            pyautogui.press(' ')
            break 
    cv2.rectangle(frame, (100, 50), (150, 100), (0, 0, 0), 3)
    cv2.rectangle(frame, (200, 50), (250, 100), (0, 0, 0), 3)
    cv2.rectangle(frame, (300, 50), (350, 100), (0, 0, 0), 3)
    cv2.rectangle(frame, (400, 50), (450, 100), (0, 0, 0), 3)
    cv2.rectangle(frame, (500, 50), (550, 100), (0, 0, 0), 3)
    cv2.line(frame, (50, 150), (50, h - 150), (0, 0, 0), 3)
    cv2.putText(frame, "w", (108, 85), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "a", (208, 85), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "s", (308, 85), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "d", (408, 85), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "cl", (505, 85), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "Space", (75, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow("Controles", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()