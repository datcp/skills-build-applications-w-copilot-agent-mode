DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "octofit_db",
        "HOST": "localhost",
        "PORT": 27017,
    }
}

# Enable CORS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]
CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
    "x-csrftoken",
]

ALLOWED_HOSTS = ["*"]