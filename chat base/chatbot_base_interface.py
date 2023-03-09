'''import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

def send_message():
    message = 'olá'
    response = 'tudo bem?'
    output_box.insert(tk.END, "Usuário: " + message + "\n")
    output_box.insert(tk.END, "ChatBot: " + str(response) + "\n\n")
    input_box.delete(0, tk.END)

root = tk.Tk()
root.title("ChatBot")

input_box = ttk.Entry(root, width=70)
input_box.pack(padx=10, pady=10)

send_button = ttk.Button(root, text="Enviar", command=send_message)
send_button.pack(padx=10, pady=10)

output_box = scrolledtext.ScrolledText(root, width=80, height=20)
output_box.pack(padx=10, pady=10)

root.mainloop()'''

#################################################################

import tkinter as tk

# Crie uma janela principal
root = tk.Tk()
root.title("Meu ChatBot")

# Crie uma área de texto para exibir as mensagens
messages = tk.Text(root)
messages.pack()

# Crie uma caixa de entrada para que o usuário possa digitar mensagens
entry = tk.Entry(root)
entry.pack()

# Crie uma variável para armazenar a resposta do chatbot
bot_response = tk.StringVar()

# Defina uma função para enviar a mensagem do usuário e receber a resposta do chatbot
def send_message():
    message = entry.get()
    messages.insert(tk.END, "Você: " + message + "\n")
    entry.delete(0, tk.END)
    response = 'resposta bot...'
    bot_response.set(response)
    messages.insert(tk.END, "ChatBot: " + response + "\n")

# Crie um botão "Enviar" para que o usuário possa enviar a mensagem
send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack()

# Crie uma área de texto para exibir a resposta do chatbot
bot_response_label = tk.Label(root, textvariable=bot_response)
bot_response_label.pack()

# Execute a interface gráfica do usuário
root.mainloop()