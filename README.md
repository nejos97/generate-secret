# Secret Generator API

Secret Generator API is a small application developed using [FastAPI](https://fastapi.tiangolo.com/) that allows generating customizable alphanumeric secrets. It also provides a health check endpoint to verify the API status.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Available Endpoints](#available-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Generate alphanumeric secrets with a custom length.
- Health check endpoint (`/healthz`) to verify the API status.
- Configurable maximum length for secrets (default: 10,000).

## Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (to run the application)

## Installation

1. Clone the repository:

   ```bash
   git clone <REPOSITORY_URL>
   cd <PROJECT_NAME>
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Run the application using Uvicorn:

```bash
uvicorn main:app --reload
```

This will start the local server at `http://127.0.0.1:8000`.

## Usage

### Generating a Secret

To generate an alphanumeric secret, use the following endpoint:

```http
GET /?length=<secret_length>
```

#### Example Request:

```bash
curl -X GET "http://127.0.0.1:8000/?length=16"
```

#### Example Response:

```json
{
  "secret": "a1b2c3d4e5f6g7h8"
}
```

> **Note**: The default length is 32 characters if `length` is not specified. The maximum allowed length is 10,000.

### Health Check

To check if the API is functioning correctly, use the `/healthz` endpoint:

```http
GET /healthz
```

#### Example Response:

```json
{
  "status": 200,
  "message": "OK"
}
```

## Available Endpoints

- **`GET /`**: Generates an alphanumeric secret.
- **`GET /healthz`**: Checks the API status.

## Contributing

Contributions are welcome! If you have suggestions for improvements, bug reports, or feature requests, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
