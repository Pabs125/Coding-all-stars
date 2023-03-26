from tkinter import *
from tkinter import messagebox
import urllib.request
from bs4 import BeautifulSoup
from langdetect import detect

def check_language():
    url = url_entry.get()
    try:
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.get_text()
        language = detect(body)
        if language == 'hi':
            messagebox.showinfo("Resultado", "La página está en hindi")
        else:
            messagebox.showinfo("Resultado", "La página no está en hindi")
    except Exception as e:
        messagebox.showerror("Error", f"Error al analizar la página: {e}")

# Crear ventana Tkinter
root = Tk()
root.title("Detener si una página está en hindi")

# Crear campos de entrada
url_label = Label(root, text="Ingrese una URL:")
url_label.pack()
url_entry = Entry(root, width=50) 
url_entry.pack()

# Crear botón de envío
submit_button = Button(root, text="Enviar", command=check_language)
submit_button.pack()

# Ejecutar la ventana Tkinter
root.mainloop()