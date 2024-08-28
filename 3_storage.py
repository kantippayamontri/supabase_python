from dotenv import load_dotenv

load_dotenv()

# TODO: connection with hosted supabase
import os
from supabase import create_client, Client
from datetime import datetime, timedelta
from storage3.utils import StorageException
from PIL import Image
import io

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# we alreay create storage for image call "image-bucket"
bucket_name: str = "image-bucket"

#upload image
new_file = "test_img.jpg"
try:
    data = supabase.storage.from_(bucket_name).upload("/user1/profile.jpg", new_file) # upload image to folder name user1 in image-bucket
except StorageException as e:
    print(e)
    # print(f"can not upload image may be this image already exist.")

#download image
data = supabase.storage.from_(bucket_name).download("/user1/profile.jpg")
data_stream = io.BytesIO(data)
image = Image.open(data_stream)
image.save("output_image.jpg")
# image.show()