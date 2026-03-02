# API Python - Cisco Packet Tracer

Scripts en Python para interactuar con la API REST de Cisco Packet Tracer. Permite obtener tickets de autenticacion, consultar dispositivos de red y hosts.

## Estructura del proyecto

```
├── src/
│   ├── constants.py             # Configuracion (URL base, credenciales)
│   ├── 01_get-ticket.py         # Obtener ticket de autenticacion
│   ├── 02_get-network-device.py # Listar dispositivos de red
│   ├── 03_get-host.py           # Listar hosts de la red
│   └── 04_tabulate.py           # Vista completa en formato tabla
├── .env                         # Variables de entorno (no se sube al repo)
├── .env.template                # Plantilla de variables de entorno
├── pyproject.toml               # Configuracion del proyecto y dependencias
└── README.md
```

## Scripts

| Script | Descripcion |
|--------|-------------|
| `01_get-ticket.py` | Autentica contra la API y obtiene un service ticket |
| `02_get-network-device.py` | Consulta los dispositivos de red usando el token del `.env` |
| `03_get-host.py` | Consulta los hosts conectados a la red |
| `04_tabulate.py` | Obtiene ticket, dispositivos y hosts, mostrando todo en tablas formateadas |

## Requisitos previos

- [Visual Studio Code](https://code.visualstudio.com/) (editor de codigo)
- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (gestor de paquetes)
- Cisco Packet Tracer corriendo en `localhost:58000`

## Instalacion

### 1. Abrir el proyecto en Visual Studio Code

1. Abrir **Visual Studio Code**
2. Ir a **Archivo > Abrir carpeta** (o `Ctrl + K` seguido de `Ctrl + O`)
3. Seleccionar la carpeta del proyecto

### 2. Abrir la terminal integrada

Para ejecutar los comandos que siguen, necesitas abrir la **terminal** dentro de VSCode:

- Ir a **Terminal > Nueva terminal** en el menu superior
- O usar el atajo de teclado: `` Ctrl + ` `` (la tecla debajo del `Esc`)

Se va a abrir un panel en la parte inferior de VSCode donde podes escribir comandos.

### 3. Clonar el repositorio

En la terminal, escribir:

```bash
git clone https://github.com/matimoya/grupo5-tercer-cuatrimestre-2025.git
cd grupo5-tercer-cuatrimestre-2025
```

> **Nota:** `git clone` descarga el proyecto y `cd` entra a la carpeta descargada.

### 4. Instalar dependencias con uv

```bash
uv sync
```

Esto crea un entorno virtual en `.venv/` e instala todas las dependencias automaticamente. No hace falta hacer nada mas.

### 5. Configurar variables de entorno

El token de autenticacion se obtiene al ejecutar el script `01_get-ticket.py` (ver paso 6). Una vez que lo tengas, copiar la plantilla y completar con tu token:

```bash
cp .env.template .env
```

Luego abrir el archivo `.env` desde el explorador de archivos de VSCode (panel izquierdo) y reemplazar `your_auth_token` con el token obtenido:

```
AUTH_TOKEN=NC-xx-xxxxxxxxxx-nbi
```

> **Nota:** Los scripts `02`, `03` y `04` necesitan este token para funcionar. El script `01` es el que lo genera.

### 6. Ejecutar los scripts

En la terminal de VSCode, escribir cualquiera de estos comandos:

```bash
uv run python src/01_get-ticket.py
uv run python src/02_get-network-device.py
uv run python src/03_get-host.py
uv run python src/04_tabulate.py
```

> **Tip:** Podes usar la flecha hacia arriba en la terminal para repetir el ultimo comando ejecutado.

## Dependencias

- **requests** - Cliente HTTP para consumir la API REST
- **tabulate** - Formateo de datos en tablas
- **python-dotenv** - Carga de variables de entorno desde `.env`
