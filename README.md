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

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (gestor de paquetes)
- Cisco Packet Tracer corriendo en `localhost:58000`

## Instalacion

### 1. Clonar el repositorio

```bash
git clone <URL_del_repositorio>
cd <nombre_de_la_carpeta>
```

### 2. Instalar dependencias con uv

```bash
uv sync
```

Esto crea un entorno virtual en `.venv/` e instala todas las dependencias automaticamente.

### 3. Configurar variables de entorno

Copiar la plantilla y completar con tu token:

```bash
cp .env.template .env
```

Editar `.env` con tu token de autenticacion:

```
AUTH_TOKEN=tu_token_aqui
```

### 4. Ejecutar los scripts

```bash
uv run python src/01_get-ticket.py
uv run python src/02_get-network-device.py
uv run python src/03_get-host.py
uv run python src/04_tabulate.py
```

## Dependencias

- **requests** - Cliente HTTP para consumir la API REST
- **tabulate** - Formateo de datos en tablas
- **python-dotenv** - Carga de variables de entorno desde `.env`
