import tkinter as tk
import time

def atualizar_relogio():
    hora_atual = time.strftime('%H:%M:%S')
    label.config(text=hora_atual)
    root.after(1000, atualizar_relogio) #Atualiza a cada 1 segundo
    
    # Janela principal
    
root = tk.Tk()
root.title("Relógio Digital")
root.geometry("250x100")
root.configure(bg='black')

# Estilo do texto
label = tk.Label(root, font=(' Arial', 40), fg='lime', bg='black')
label.pack(anchor='center')

#Inicia o relógio
atualizar_relogio()

root.mainloop()
