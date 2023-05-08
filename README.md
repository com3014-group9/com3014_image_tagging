# Image Tagging Service

The Image Tagging Service is a Flask application that provides an API for tagging images using a Vision Transformer (ViT) model. The service requires user authentication before allowing access to the tagging endpoint.

## Installation

To install the Image Tagging Service, you can use Docker Compose. Run the following command from the root directory of the project:

```bash
docker-compose up
```

This will build and start two containers: one for the image tagging service, and one for MongoDB.

## Usage

The Image Tagging Service API is accessible at `http://localhost:3304`. You can use any HTTP client to interact with the API.

### Authentication

The Image Tagging Service requires user authentication before allowing access to the tagging endpoint. To authenticate, you must first create a user account. You can create a user account by sending a POST request to `http://localhost:3304/users` with a JSON payload containing the `username` and `password` fields.

Once you have created a user account, you can authenticate by sending a POST request to `http://localhost:3304/login` with a JSON payload containing the `username` and `password` fields. The response will include an access token that you can use to access the tagging endpoint.

### Tagging Images

To tag an image, you must first authenticate and obtain an access token. Once you have an access token, you can send a POST request to `http://localhost:3304/get_tags` with a `multipart/form-data` payload containing the image file.

The `get_tags` endpoint returns the predicted image tag as a string.

## Contributing

If you would like to contribute to the Image Tagging Service, please submit a pull request.
