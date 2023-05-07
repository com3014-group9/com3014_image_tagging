Sure! Here's an example README file for the updated code:

# Image Tagging Service

This is a Flask application that provides a RESTful API for image tagging. Given an image, the application uses a pre-trained Vision Transformer model (ViT) to predict the image's content and return the predicted tags to the client.

## Installation

1. Clone this repository.
2. Install the required dependencies with `pip install -r requirements.txt`.

## Usage

1. Start the application with `python app.py`.
2. Send a POST request to the `/get_tags` endpoint with an image file attached as `file`. The response will contain a JSON object with the predicted tags.

For example, using the `curl` command-line tool:

```
curl -X POST -H "Authorization: Bearer <your-access-token>" -F "file=@/path/to/image.jpg" http://localhost:3304/get_tags
```

### Authentication

Access to the API requires authentication. Send an HTTP `Authorization` header with a bearer token to the API endpoints.

To generate a bearer token for testing purposes, you can use the `/generate_token` endpoint with a valid user ID:

```
curl -X POST -d '{"user_id": 123}' -H "Content-Type: application/json" http://localhost:3304/generate_token
```

This will return a JSON object with a `token` field, which you can use as the bearer token in subsequent requests.

## Testing

1. Install the required testing dependencies with `pip install -r requirements-test.txt`.
2. Run the tests with `pytest`.

## Acknowledgements

This application uses the Hugging Face Transformers library for image processing and classification.
