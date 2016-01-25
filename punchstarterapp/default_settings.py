import os
import cloudinary

DEBUG=True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR + "/app.db"

cloudinary.config(
  cloud_name = "andrealmar",
  api_key = "668886311822753",
  api_secret = "69dYS6OFx-hDtNZmZ6YLW1P3tX8"
)
