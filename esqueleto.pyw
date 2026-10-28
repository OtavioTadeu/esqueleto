import tkinter as tk
import random
import threading
import time
import sys
import os

# Função para encontrar o caminho correto do GIF, seja rodando o .py ou o .exe compilado
def resource_path(relative_path):
    """Retorna o caminho absoluto para o recurso, suportando execução direta e PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))

    path = os.path.join(base_path, relative_path)
    if not os.path.exists(path):
        # Fallback para o diretório onde o executável ou script foi iniciado
        exe_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        fallback = os.path.join(exe_dir, relative_path)
        if os.path.exists(fallback):
            return fallback
    return path

# ================= CONFIGURAÇÕES =================
GIF_FILE = resource_path("esqueleto.gif")  # O GIF DEVE ESTAR VIRADO PARA A ESQUERDA
MIN_MINUTES = 1
MAX_MINUTES = 1
TEMPO_TRAVESSIA_MS = 500    # Tempo desejado em milissegundos (1000ms = 1 segundo)
FRAME_DELAY_MS = 30          # Tempo entre cada quadro do GIF
# =================================================

class SkeletonPrank:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw() 
        
        threading.Thread(target=self.timer_loop, daemon=True).start()
        self.root.mainloop()

    def timer_loop(self):
        while True:
            wait_time = random.randint(MIN_MINUTES * 60, MAX_MINUTES * 60)
            time.sleep(wait_time)
            self.root.after(0, self.trigger_skeleton)

    def trigger_skeleton(self):
        anim_win = tk.Toplevel(self.root)
        anim_win.overrideredirect(True) 
        anim_win.attributes('-topmost', True) 
        
        trans_color = '#000001'
        anim_win.config(bg=trans_color)
        anim_win.attributes('-transparentcolor', trans_color)

        label = tk.Label(anim_win, bg=trans_color)
        label.pack()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # === CÁLCULO DINÂMICO DE VELOCIDADE ===
        # Distância total a percorrer: Largura da tela + margem de segurança (400px)
        distancia_total = screen_width + 400
        # Quantas vezes o script vai atualizar a tela
        atualizacoes_por_segundo = max(1, TEMPO_TRAVESSIA_MS // FRAME_DELAY_MS)
        # Quantos pixels pular a cada atualização
        velocidade_pixels = max(1, distancia_total // atualizacoes_por_segundo)

        # 1. POSIÇÃO INICIAL: Canto direito
        current_x = screen_width
        y_pos = (screen_height // 2) - 150 
        
        def move_and_animate(frame_idx=0):
            nonlocal current_x
            
            try:
                frame_image = tk.PhotoImage(file=GIF_FILE, format=f'gif -index {frame_idx}')
                label.config(image=frame_image)
                label.image = frame_image 
                next_frame = frame_idx + 1
            except tk.TclError:
                next_frame = 0 
                frame_image = tk.PhotoImage(file=GIF_FILE, format=f'gif -index {next_frame}')
                label.config(image=frame_image)
                label.image = frame_image

            # 2. MOVIMENTO: Usa a velocidade calculada dinamicamente
            current_x -= velocidade_pixels 
            anim_win.geometry(f"+{current_x}+{y_pos}")
            
            if current_x > -400:
                anim_win.after(FRAME_DELAY_MS, lambda: move_and_animate(next_frame))
            else:
                anim_win.destroy() 

        move_and_animate()

if __name__ == "__main__":
    SkeletonPrank()
