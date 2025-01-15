# utils.py
import requests
from supabase import create_client
from django.conf import settings

# Initialize Supabase client
supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

def upload_image_to_supabase(file):

    # Define file path in Supabase Storage
    file_path = f"images/{file.name}"
    
    # Upload image to Supabase Storage
    file_content = file.read()
    response = supabase.storage.from_("images").upload(file_path, file_content)
    
    if response.status_code != 200:
        raise Exception("Failed to upload image to Supabase Storage")
    
    # Get public URL of the uploaded image
    file_url = supabase.storage.from_("images").get_public_url(file_path)["publicURL"]

    return file_url
