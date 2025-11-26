import customtkinter as ctk
import directorio  
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

ventana = None
entrada_nombre = None
entrada_numero = None
etiqueta_estado = None

def agregar_persona():
    global entrada_nombre, entrada_numero, etiqueta_estado
    
    nombre = entrada_nombre.get()
    numero = entrada_numero.get()

    if nombre and numero: 
        try:
            
            directorio.guardar_contacto(nombre, numero)
            
            
            etiqueta_estado.configure(text=f"Guardado: {nombre}", text_color="green")
            limpiar_campos()
        except Exception as e:
            etiqueta_estado.configure(text=f"Error al guardar: {e}", text_color="red")
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")

def limpiar_campos():
    global entrada_nombre, entrada_numero
    entrada_nombre.delete(0, ctk.END)
    entrada_numero.delete(0, ctk.END)

def contruir_interfaz():
    global ventana, entrada_nombre, entrada_numero, etiqueta_estado

    ventana = ctk.CTk()
    ventana.title("Directorio de Personas")
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