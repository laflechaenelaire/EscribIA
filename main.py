import tkinter
import tkinter.messagebox
import customtkinter
import easygui
import openai
import threading
import traceback
from openai.api_resources.abstract.api_resource import APIResource
from tkinter import filedialog
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
model_id = 'whisper-1'


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EscribIA")
        self.geometry(f"{716}x{580}")
        self.iconbitmap('icon.ico')

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((1, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="EscribIA", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.load_audio_button = customtkinter.CTkButton(self.sidebar_frame, text="Cargar Audio", command=self.load_audio_file)
        self.load_audio_button.grid(row=1, column=0, padx=20, pady=10)
        self.transcribe_button = customtkinter.CTkButton(self.sidebar_frame, text="Transcribir", command=self.transcribe_audio, state="disabled")
        self.transcribe_button.grid(row=2, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Apariencia:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.guardar_button = customtkinter.CTkButton(self.sidebar_frame, text="Guardar", command=self.guardar_transcripcion, state="disabled")
        self.guardar_button.grid(row=3, column=0, padx=20, pady=10)


        # create label with custom text and background color
        self.footer_label = customtkinter.CTkLabel(self, text="SMG - 2023", anchor='ne', text_color=("grey", "gray75"))
        self.footer_label.grid(row=5, column=1, sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=500, height=500)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        texto = r"""
            (\ 
            \' \ 
             \' \    __________  
             / ' |   ()__________)
             \ '/    \ ~~~ ~~    \
               \       \ ~~~~        \
             (==)     \___________\
             (__)       ()___________) 

                    """
        self.textbox.insert("1.0", texto)
        self.textbox.insert("end", "EscribIA by SMG (2023)\n", "blue")
        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.textbox.tag_config("error", foreground="red")

        # Transcription file path
        self.file_path = ''

    def change_appearance_mode_event(self, new_appearance_mode: str):
      customtkinter.set_appearance_mode(new_appearance_mode)

    def load_audio_file(self):
        try:
            self.file_path = easygui.fileopenbox(filetypes=[["*.mp3", "*.wav","*.mp4", "*.ogg", "Archivos de audio"]])
            if self.file_path:
                self.transcribe_button.configure(state="normal")  # enable transcribe button
        except Exception as e:
            tb_str = traceback.format_exception(type(e), e, e.__traceback__)
            tb_str = "".join(tb_str)  # Convertir a cadena
            self.textbox.delete("1.0", "end")  # Limpiar la caja de texto
            self.textbox.insert("0.0", f"Ocurrió un error:\n\n{tb_str}", "error")

    def transcribe_audio(self):
        if self.file_path:
            threading.Thread(target=self.transcribe_file).start()

    def transcribe_file(self):
        try:
            self.textbox.delete("1.0", "end")  # Limpiar la caja de texto
            self.textbox.insert("0.0", "Transcribiendo...\n")
            media_file = open(self.file_path, 'rb')
            response = openai.Audio.transcribe(
                model=model_id,
                file=media_file
            )
            self.textbox.delete("1.0", "end")  # Limpiar la caja de texto
            self.textbox.insert("0.0", response['text'])
            self.guardar_button.configure(state="normal")  # Habilitar el botón de guardar
        except Exception as e:
            tb_str = traceback.format_exception(type(e), e, e.__traceback__)
            tb_str = "".join(tb_str)  # Convertir a cadena
            self.textbox.delete("1.0", "end")  # Limpiar la caja de texto
            self.textbox.insert("0.0", f"Ocurrió un error:\n\n{tb_str}", "error")

    def guardar_transcripcion(self):
        try:
            # Muestra el cuadro de diálogo de guardado de archivos
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])

            if file_path:
                # Obtiene el contenido actual del cuadro de texto
                texto = self.textbox.get("1.0", "end-1c")

                # Guarda el contenido en el archivo seleccionado
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(texto)
        except Exception as e:
            tb_str = traceback.format_exception(type(e), e, e.__traceback__)
            tb_str = "".join(tb_str)  # Convertir a cadena
            self.textbox.delete("1.0", "end")  # Limpiar la caja de texto
            self.textbox.insert("0.0", f"Ocurrió un error:\n\n{tb_str}", "error")

if __name__ == "__main__":
    app = App()
    app.mainloop()
