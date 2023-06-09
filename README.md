# EscribIA

EscribIA es una simple aplicación de transcripción de audio impulsada por el modelo de OpenAI, Whisper. Utiliza la interfaz gráfica de usuario (GUI) de Tkinter y es compatible con los formatos de audio más comunes, como .mp3, .wav, .mp4 y .ogg.

![Ejemplo de imagen](GUI.png)
## Características
- Transcripción de audio usando OpenAI Whisper.
- Interfaz gráfica de usuario fácil de usar, impulsada por Tkinter.
- Soporte para cambiar la apariencia entre Light, Dark y System.
- Posibilidad de guardar transcripciones en archivos de texto.

## Instalación
Para utilizar esta aplicación, primero debes clonar el repositorio:

```
git clone https://github.com/laflechaenelaire/EscribIA
```

Luego, instale las dependencias necesarias utilizando pip:

```
pip install -r requirements.txt
```

## Uso
Para ejecutar la aplicación, primero necesita obtener una clave de API de OpenAI. Luego, cree un archivo .env e incerte la clave:

```
OPENAI_API_KEY=<your-api-key>
```

Luego, puede iniciar la aplicación ejecutando el archivo `main.py`:

```
python main.py
```

Una vez que la aplicación esté en ejecución, puedes cargar un archivo de audio seleccionando "Cargar Audio", luego puedes transcribir el audio presionando "Transcribir". Una vez finalizada la transcripción, puedes guardar el resultado en un archivo de texto presionando "Guardar".

## Licencia
Esta aplicación está bajo la licencia MIT. Consulte el archivo [LICENSE](LICENSE) para obtener más detalles.

## Contribuir
Las contribuciones son bienvenidas! 

## Notas 

Por favor, ten en cuenta que este código utiliza el modelo Whisper de OpenAI que tiene costos asociados. Asegúrate de entender los costos antes de usar esta aplicación.

## Créditos
Esta aplicación fue creada por Santiago Manuel González en 2023.

