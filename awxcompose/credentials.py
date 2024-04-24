DATABASES = {
    'default': {
        'ATOMIC_REQUESTS': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "awx",
        'USER': "awx",
        'PASSWORD': "Admin@123",
        'HOST': "postgres",
        'PORT': "5432",
    }
}

BROADCAST_WEBSOCKET_SECRET = "MlhjbDpGdFpXbE86NGtoZGUwMS13SkNlNlByS2hkeCxQU0swR2tnQ2VsSEJFMzY6RVdRUDZxQWpzaGZTbHZxdlB4cXZJRzkzWEkxVHQxUEFEenVfLHN5TC0wWWhNalJXdFQ3OixfeHM4Wl9UNFZ5bCxHc1p5ZS4uMml3Y01PbUU="
