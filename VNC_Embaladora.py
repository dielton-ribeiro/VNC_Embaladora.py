import os
import tkinter as tk

def abrir_conexao_vnc(event=None):
    loja = loja_entry.get()

    cabo = [18, 43, 49, 51, 53, 67]
    ip = 200
    lan = 26
    if int(loja) in cabo:
        ip = 100
        lan = 20

    loja = loja.lstrip('0')

    config = f"""[Connection]
ConnMethod=tcp
ConnTime=2021-10-17T18:00:35.134Z
Host=172.{lan}.{loja}.{ip}
Password=60ec78bc10c90d64
RelativePtr=0
Uuid=c4fb904e-bfb6-437d-9e99-ceb59c4535ea"""

    with open("config.vnc", "w") as file:
        file.write(config)

    os.system("start config.vnc")

    # Apaga as informações dos campos de entrada
    loja_entry.delete(0, tk.END)

    loja_entry.focus_set()

root = tk.Tk()
window_width = 250
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{window_width}x{window_height}")

root.title("VNC Embaladora")

frame_loja = tk.Frame(root)
frame_loja.pack(pady=10)
tk.Label(frame_loja, text="Digite o número da loja:").pack(side=tk.LEFT)
loja_entry = tk.Entry(frame_loja, width=10)
loja_entry.pack(side=tk.RIGHT)

tk.Button(root, text="Abrir Conexão VNC", command=abrir_conexao_vnc).pack(pady=1)

loja_entry.bind("<Return>",  abrir_conexao_vnc)

root.mainloop()
