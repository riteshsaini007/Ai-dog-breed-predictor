from supabase import create_client
import requests
import os

# ==============================
# 🔐 Supabase Credentials
# ==============================

SUPABASE_URL = "https://cnlanqegjktriwmumlnb.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNubGFucWVnamt0cml3bXVtbG5iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEzMjk2ODcsImV4cCI6MjA4NjkwNTY4N30.oX8ssiw9uIB97IISshg8TRIbGy3iSA4Iar5h_6vBVsM"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

BUCKET_NAME = "Dogs_Images"

# ==============================
# 📂 Fetch all breeds from table
# ==============================

response = supabase.table("Dogs").select("Breed_Name, folder_name").execute()
breeds = response.data

# ==============================
# 📥 Download images breed-wise
# ==============================

for breed in breeds:
    folder = breed["folder_name"]
    
    print(f"\nDownloading images for: {folder}")
    
    # Create local folder
    os.makedirs(f"dataset/{folder}", exist_ok=True)
    
    # List files in storage folder
    files = supabase.storage.from_(BUCKET_NAME).list(folder)
    
    for file in files:
        file_name = file["name"]
        
        public_url = supabase.storage.from_(BUCKET_NAME).get_public_url(
            f"{folder}/{file_name}"
        )
        
        img_data = requests.get(public_url).content
        
        with open(f"dataset/{folder}/{file_name}", "wb") as f:
            f.write(img_data)

print("\n✅ Dataset Download Complete!")
