import pyautogui
import time
import datetime
from pyautogui import ImageNotFoundException

pyautogui.PAUSE = 0.5

def log(msg):
    agora = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{agora}] {msg}")

def tentar_achar(nome, confidence=0.7):
    """Tenta achar a imagem mas sem levantar erro."""
    try:
        return pyautogui.locateCenterOnScreen(nome, confidence=confidence)
    except ImageNotFoundException:
        return None

# ORDEM LÓGICA DO FLUXO
etapas = [
    "imagem_2.png",  # Lutar (home)
    "imagem_4.png",  # Lutar (segunda tela)
    "imagem_5.png",  # Lutar (terceira tela)
    "imagem_6.png",  # Skip
    "imagem_7.png"   # Continuar
]

log("BOT INICIADO! Abra o jogo e deixe o bot rodando.")
log("Pressione CTRL + C para parar.\n")

etapa_atual = 0  # começa na primeira etapa

while True:
    log(f"--- Procurando qualquer etapa válida (etapa atual: {etapas[etapa_atual]}) ---")

    encontrado = False

    # Tenta achar QUALQUER imagem do fluxo
    for i in range(len(etapas)):
        idx = (etapa_atual + i) % len(etapas)   # busca circular
        imagem = etapas[idx]

        pos = tentar_achar(imagem)

        if pos:
            log(f"Encontrado: {imagem} → Clicando")
            pyautogui.click(pos)

            # Próxima etapa
            etapa_atual = (idx + 1) % len(etapas)
            log(f"Avançando para a próxima etapa: {etapas[etapa_atual]}\n")
            encontrado = True
            break

    if not encontrado:
        log("Nenhuma imagem encontrada. Aguardando...")
        time.sleep(1)
