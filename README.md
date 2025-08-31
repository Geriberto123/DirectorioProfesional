# Directorio Profesional - Aplicación Web con Flask y Firestore

Esta es una aplicación web que utiliza Python con el microframework Flask y se conecta a la base de datos NoSQL de Google Firestore para mostrar, buscar y filtrar un directorio de perfiles profesionales.

## Cómo Ejecutar la Aplicación en un Entorno Local

### Prerrequisitos

- Python 3.x instalado.
- Acceso a una terminal o línea de comandos.
- `git` instalado para clonar el repositorio.

### Pasos para la Instalación y Ejecución

1.  **Clonar el Repositorio**
    Abre tu terminal y clona el repositorio del proyecto desde GitHub.

    ```bash
    git clone https://github.com/Geriberto123/DirectorioProfesional.git
    cd DirectorioProfesional
    ```

2.  **Crear y Activar un Entorno Virtual**
    Es una buena práctica aislar las dependencias del proyecto en un entorno virtual.

    ```bash
    # Crea el entorno virtual
    python -m venv .venv

    # Actívalo (en Windows usa: .venv\Scripts\activate)
    source .venv/bin/activate
    ```

3.  **Instalar las Dependencias**
    Instala todos los paquetes de Python necesarios con un solo comando.

    ```bash
    pip install -r requirements.txt
    ```

4.  **Crear el Archivo de Entorno (`.env`)**
    La aplicación necesita saber el ID de tu proyecto de Firebase. Crea un archivo llamado `.env` en la raíz del proyecto.

    Dentro del archivo `.env`, añade la siguiente línea:
    ```
    FIREBASE_PROJECT_ID="directorioprofesional-81e46"
    ```

5.  **Autenticarse con Google Cloud**
    Para que tu máquina local pueda acceder a los servicios de Google Cloud de forma segura, ejecuta el siguiente comando. Se abrirá una ventana del navegador para que inicies sesión con la cuenta de Google a la que se le concedió acceso.

    ```bash
    gcloud auth application-default login
    ```

6.  **¡Ejecutar la Aplicación!**
    Finalmente, inicia el servidor de desarrollo de Flask.

    ```bash
    flask run
    ```

    Una vez ejecutado, verás una salida en la terminal indicando que el servidor está corriendo. Podrás acceder a la aplicación abriendo la siguiente URL en tu navegador web:

    **http://127.0.0.1:5000**
