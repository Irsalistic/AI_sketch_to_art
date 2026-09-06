# Sketch to Art

FastAPI service that turns a sketch into a rendered image using **Stable Diffusion WebUI** and **ControlNet**.

## Features

- Sketch-to-art conversion with ControlNet lineart
- Prompt-driven style
- Built-in resize before generation
- Optional simple web UI

## Prerequisites

- Python 3.8+
- A running [Stable Diffusion WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) with the ControlNet extension
- The RealisticVision checkpoint (or change the model name in `sketch_to_art.py`)

## Setup

```bash
git clone https://github.com/Irsalistic/AI_sketch_to_art.git
cd AI_sketch_to_art
pip install -r requirements.txt
```

If this folder has no `requirements.txt`, install:

```bash
pip install fastapi uvicorn pillow webuiapi python-multipart jinja2
```

Point the client at your WebUI in `shared.py` (`base_url` and `port`).

## Run

```bash
uvicorn main:app --reload
```

## API

`POST /sketch` (multipart form)

| Field | Required | Description |
|-------|----------|-------------|
| `key` | yes | API key |
| `image` | yes | Sketch image |
| `prompt` | yes | Text description |

Returns a PNG.

```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/sketch",
    files={"image": open("sketch.png", "rb")},
    data={"prompt": "a watercolor house", "key": "your-api-key"},
)
open("out.png", "wb").write(response.content)
```

`GET /` serves the web UI when templates are present.

## Layout

```
main.py
shared.py           # WebUI host / port
sketch_to_art.py    # Generation logic
```
