# CodeT5-Gradio

CodeT5-Gradio is a web application that allows generating code based on natural language descriptions using the CodeT5 model and Gradio interface.

## Features

- Code generation based on task descriptions in natural language.
- Supports multiple programming languages (depends on the pre-trained CodeT5 model).
- Interactive web interface for convenient input of requests and viewing results.

## Getting Started

To run the project locally, follow these steps:

### Prerequisites

- Docker
- Docker Compose (for running with `docker-compose`) #TODO

### Installation and Running

1. Clone the repository:

```bash
git clone https://github.com/emd1tey/codet5-gradio.git
cd codet5-gradio
docker build -t codet5-gradio:local . 
docker run -d --rm -p 7860:7860 --name codet5-gradio codet5-gradio:local 
