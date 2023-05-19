
# legal-summarizer
![Docker](https://img.shields.io/badge/Docker-19.03%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-orange.svg)

This is a Flask application that utilizes the Transformers library for text summarization. A abstractive text summarizer specifically designed to summarize complex Terms and Conditions article. 

## Prerequisites

- Python 3.9.2
- pip

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/immohann/legal-summarizer.git

2. Navigate to the project directory:
    ```bash
    cd legal-summarizer

3. Install requirements
    ```bash    
    pip install -r requirements.txt

4. Start the Flask application:
    ```bash
    python app.py

## Using Docker

You can also run the application using Docker. Follow these steps:

1. Pull the Docker image:
    ```bash
    docker pull immohannn/sux:latest
2. Run the container:
    ```bash
    docker run -d -p 5000:5000 immohannn/sux
3. Access the application:
    ```bash
    http://localhost:5000   

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.