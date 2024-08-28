from dotenv import load_dotenv
from gotrue.errors import AuthApiError

load_dotenv()

# TODO: connection with hosted supabase
import os
from supabase import create_client, Client
from datetime import datetime, timedelta

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

random_email = "kantippayamontri@gmail.com"
random_password = "Kan130241_"

session = None
# sign up/ create user
# sign up and sign in with email -> for free version max 3 request/hour
# try:
#     session = supabase.auth.sign_up({"email": random_email, "password": random_password}) #after that go to email provider to verify email.
#     print("create user success.")
# except AuthApiError:
#     print(f"create user fail.")

# sign in/ log in 
try:
    session = supabase.auth.sign_in_with_password({ "email": random_email, "password": random_password })
    print(f"log in success.")
except AuthApiError:
    print(f'log in fail.')


    
# supabase.auth.sign_out() #log out
