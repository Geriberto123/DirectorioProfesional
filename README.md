# Directorio Profesional - Aplicación Web con Flask y Firestore

Esta es una aplicación web que utiliza Python/Flask y se conecta a Google Firestore para mostrar, buscar y filtrar un directorio de perfiles profesionales.

## Entrega del Proyecto

Para la evaluación, se proporcionan dos métodos de acceso. El **Método 1 es el recomendado**, ya que cumple con el requisito de "cargar al primer intento" sin necesidad de configuración por parte del evaluador.

---

### **Método 1: Acceder a la Aplicación en Ejecución (Recomendado)**

La aplicación ya está desplegada y en funcionamiento en un entorno de desarrollo en la nube. Se puede acceder y probar toda la funcionalidad directamente a través del siguiente enlace:

**[PEGA AQUÍ TU ENLACE DE PREVISUALIZACIÓN DE LA APLICACIÓN]**

---

### **Método 2: Ejecución en un Entorno Local (Alternativo)**

Este método permite al evaluador ejecutar el código fuente en su propia máquina. Gracias a que el propietario del proyecto (`Geriberto123`) ya ha concedido los permisos necesarios a la cuenta del evaluador, los siguientes pasos funcionarán correctamente.

**Pasos para la Instalación:**

1.  **Clonar el Repositorio**
    ```bash
    git clone https://github.com/Geriberto123/DirectorioProfesional.git
    cd DirectorioProfesional
    ```

2.  **Crear y Activar un Entorno Virtual**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instalar Dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Crear Archivo de Entorno (`.env`)**
    Crea un archivo llamado `.env` en la raíz del proyecto y añade la siguiente línea:
    ```
    FIREBASE_PROJECT_ID="directorioprofesional-81e46"
    ```

5.  **Autenticar con Google Cloud SDK**
    Instala `gcloud` (si no está disponible) y autentícate con la cuenta de Google a la que se le dio acceso.
    ```bash
    gcloud auth application-default login
    ```

6.  **Ejecutar la Aplicación**
    ```bash
    flask run
    ```
    La aplicación estará disponible en `http://127.0.0.1:5000`.
