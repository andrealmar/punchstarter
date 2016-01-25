import os

DEBUG=True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR + "/app.db"

cloudinary.config(
  cloud_name = "sample",
  api_key = "874837483274837",
  api_secret = "a676b67565c6767a6767d6767f676fe1"
)
