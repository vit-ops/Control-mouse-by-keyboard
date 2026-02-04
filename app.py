import subprocess
import sys
import os
import threading
import time

# --- INSTALAÇÃO AUTOMÁTICA DE DEPENDÊNCIAS ---
def setup():
    if not getattr(sys, 'frozen', False): # Só instala se não for um .exe
        libs = ['customtkinter', 'pyautogui', 'keyboard', 'pyinstaller']
        for lib in libs:
            try:
                __import__(lib)
            except ImportError:
                subprocess.check_call([sys.executable, "-m", "pip", "install", lib, "--quiet"])

setup()

import customtkinter as ctk
import pyautogui as auto
import keyboard

ctk.set_appearance_mode("dark")

class MouseArrow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MouseArrow Pro")
        self.geometry("300x250")
        self.attributes("-topmost", True)
        self.resizable(False, False)
        
        self.active = False
        self.speed = 0.0
        self.max_s = 20.0
        auto.FAILSAFE = True
        auto.PAUSE = 0 

        # --- BOTÃO PRINCIPAL ---
        self.btn_main = ctk.CTkButton(self, text="LIGAR (F9)", fg_color="#1f538d",
                                      command=self.toggle, font=("Roboto", 16, "bold"), height=60)
        self.btn_main.pack(pady=20, padx=30, fill="x")

        self.status = ctk.CTkLabel(self, text="OFF", text_color="red", font=("Roboto", 12, "bold"))
        self.status.pack()

        # --- BOTÃO DE INSTALAR (SÓ APARECE NO SCRIPT .PY) ---
        if not getattr(sys, 'frozen', False):
            self.btn_install = ctk.CTkButton(self, text="INSTALL (.EXE)", fg_color="#2b2b2b",
                                            command=self.generate_exe)
            self.btn_install.pack(pady=20, padx=60, fill="x")

        # Atalhos e Threads
        keyboard.add_hotkey('f9', self.toggle)
        threading.Thread(target=self.move_loop, daemon=True).start()
        threading.Thread(target=self.action_loop, daemon=True).start()

    def toggle(self):
        self.active = not self.active
        self.speed = 0.0
        if self.active:
            self.btn_main.configure(text="DESLIGAR (F9)", fg_color="#961a1a")
            self.status.configure(text="ATIVO", text_color="#2db34a")
        else:
            self.btn_main.configure(text="LIGAR (F9)", fg_color="#1f538d")
            self.status.configure(text="OFF", text_color="red")

    def action_loop(self):
        while True:
            if self.active:
                try:
                    # Clique Esquerdo (/) e Direito (*)
                    if keyboard.is_pressed(181) or keyboard.is_pressed(53) or keyboard.is_pressed('/'):
                        auto.click(button='left'); time.sleep(0.2)
                    if keyboard.is_pressed(106) or keyboard.is_pressed(55) or keyboard.is_pressed('*'):
                        auto.click(button='right'); time.sleep(0.2)
                    # Scroll (+ e -)
                    if keyboard.is_pressed('+'): auto.scroll(150); time.sleep(0.05)
                    if keyboard.is_pressed('-'): auto.scroll(-150); time.sleep(0.05)
                except: pass
            time.sleep(0.01)

    def move_loop(self):
        while True:
            if self.active:
                keys = ['up', 'down', 'left', 'right']
                if any(keyboard.is_pressed(k) for k in keys):
                    v = 1 if keyboard.is_pressed('shift') else int(self.speed if self.speed >= 1 else 1)
                    if not keyboard.is_pressed('shift'):
                        self.speed = min(self.speed + 0.5, self.max_s)
                    if keyboard.is_pressed('up'): auto.moveRel(0, -v)
                    if keyboard.is_pressed('down'): auto.moveRel(0, v)
                    if keyboard.is_pressed('left'): auto.moveRel(-v, 0)
                    if keyboard.is_pressed('right'): auto.moveRel(v, 0)
                else: self.speed = 0.0
            time.sleep(0.01)

    def generate_exe(self):
        self.btn_install.configure(text="INSTALLING...", state="disabled")
        def run():
            try:
                script = os.path.abspath(sys.argv[0])
                # Comando usando o módulo python para evitar erro de PATH
                subprocess.run([sys.executable, "-m", "PyInstaller", "--noconsole", "--onefile", script], check=True)
                if os.path.exists('dist'): os.startfile('dist')
                self.btn_install.configure(text="DONE!", fg_color="green", state="normal")
            except:
                self.btn_install.configure(text="ERROR", fg_color="red", state="normal")
        threading.Thread(target=run, daemon=True).start()

if __name__ == "__main__":
    app = MouseArrow()
    app.mainloop()
