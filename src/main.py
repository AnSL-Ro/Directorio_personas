import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

ventana = None
entrada_nombre = None
entrada_numero = None
etiqueta_estado = None

def agregar_persona():
    nombre = entrada_nombre.get()
    numero = entrada_numero.get()
    
    etiqueta_estado.configure(text=f"Persona agregada: {nombre} con número {numero}")

def limpiar_campos():
    entrada_nombre.delete(0, ctk.END)
    entrada_numero.delete(0, ctk.END)


    

def contruir_interfaz():
    global ventana, entrada_nombre, entrada_numero, etiqueta_estado

    ventana = ctk.CTk()
    ventana.title("Interfaz de Usuario")
    ventana.geometry("400x400")

    etiqueta_nombre = ctk.CTkLabel(ventana, text="Nombre:")
    etiqueta_nombre.pack(pady=10)
    entrada_nombre = ctk.CTkEntry(ventana, placeholder_text="Ingrese su nombre")
    entrada_nombre.pack(pady=10)

    etiqueta_numero = ctk.CTkLabel(ventana, text="Número:")
    etiqueta_numero.pack(pady=10)
    entrada_numero = ctk.CTkEntry(ventana, placeholder_text="Ingrese un número")
    entrada_numero.pack(pady=10)

    etiqueta_estado = ctk.CTkLabel(ventana, text="")
    etiqueta_estado.pack(pady=10)

    btn = ctk.CTkButton(ventana, text="Agregar persona", command=agregar_persona)
    btn.pack(pady=10)

    btn_limpiar = ctk.CTkButton(ventana, text="Limpiar campos", command=limpiar_campos)
    btn_limpiar.pack(pady=10)


def main():
    global ventana

    contruir_interfaz()
    ventana.mainloop()
    

if __name__ == "__main__":
    main()
