# Sketch to Art API

A FastAPI-based web service that transforms sketches into artistic renderings using Stable Diffusion and ControlNet. This service provides endpoints for converting line art into realistic images with various artistic styles.

## Features

- Sketch to realistic art conversion using ControlNet
- Support for multiple artistic styles and models 
- Built-in image resizing and processing
- FastAPI-based RESTful API
- Jinja2 template integration for web interface

## Prerequisites

- Python 3.8+
- FastAPI
- Pillow (PIL)
- webuiapi
- Stable Diffusion WebUI with ControlNet extension

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Irsalistic/AI_sketch_to_art/
cd AI_sketch_to_art
```

2. Install the required dependencies:
```bash
pip install requirements.txt
```

3. Set up the project structure:
```
project/
├── main.py
├── shared.py
├── sketch_to_art.py
├── templates/
│   └── index.html
└── static/
```

## Configuration

### API Settings
The API is configured to connect to a Stable Diffusion WebUI instance. You can modify the connection settings in `shared.py`:

```python
base_url = "192.168.0.1"  # Update with your WebUI host
port = 7861                  # Update with your WebUI port
```

### Available Models
The project uses the RealisticVision model by default. You can modify the model settings in `sketch_to_art.py`:

```python
desired_model_name = 'realisticVisionV60B1_v51VAE'
```

## API Endpoints

### Root Endpoint
- `GET /`: Returns the main web interface

### Sketch Processing
- `POST /sketch`
  - Parameters:
    - `key`: API authentication key (required)
    - `image`: Image file upload (required)
    - `prompt`: Text description for image generation (required)
  - Returns: Generated image in PNG format

## Usage Example

```python
import requests

url = "http://your-server/sketch"
files = {
    'image': open('sketch.png', 'rb'),
    'prompt': (None, 'your prompt here'),
    'key': (None, 'your-api-key')
}

response = requests.post(url, files=files)
with open('generated_image.png', 'wb') as f:
    f.write(response.content)
```

## Image Processing Features

- Automatic image resizing while maintaining aspect ratio
- Maximum dimension limit: 976px
- Support for various image formats
- HDR photo enhancement with detailed prompts
- ControlNet Lineart integration for sketch processing

## Security

- API key authentication required for sketch endpoint
- Configurable authorized keys list
- Input validation and error handling

## Error Handling

The API includes proper error handling for:
- Unauthorized access attempts
- Invalid file uploads
- Processing failures
- Model loading issues

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
