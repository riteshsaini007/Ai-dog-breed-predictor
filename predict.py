import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from supabase import create_client

# ==============================
# 🔐 Supabase Credentials
# ==============================

SUPABASE_URL = "https://cnlanqegjktriwmumlnb.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNubGFucWVnamt0cml3bXVtbG5iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzEzMjk2ODcsImV4cCI6MjA4NjkwNTY4N30.oX8ssiw9uIB97IISshg8TRIbGy3iSA4Iar5h_6vBVsM"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ==============================
# 📦 Load Trained Model
# ==============================

model = tf.keras.models.load_model("dog_breed_model.h5")

# IMPORTANT: must match training order
class_names = ['Beagle', 'Dachshund', 'FrenchBullDog', 'German Shepherd',
               'Golden Retriever', 'Labrador Retriever',
               'Pembroke Welsh Corgi', 'Poodle',
               'Rottweiler', 'Shih Tzu']

# ==============================
# 🖼 Load Test Image
# ==============================

img_path = "test3-image.jpg"

img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

# ==============================
# 🔍 Predict Breed
# ==============================

prediction = model.predict(img_array)
predicted_index = np.argmax(prediction)
predicted_breed = class_names[predicted_index].strip()

print(f"\n🐶 Predicted Breed: {predicted_breed}")
# ==============================
# 📡 Fetch Properties From Supabase
# ==============================

response = supabase.table("Dogs") \
    .select("*") \
    .eq("Breed_Name", predicted_breed) \
    .execute()

if not response.data:
    print("\n❌ No matching breed found in database.")
    print("Predicted:", predicted_breed)
else:
    dog_info = response.data[0]

    print("\n📋 Dog Details:")
    print("Origin:", dog_info["Origin"])
    print("Weight:", dog_info["Weight"])
    print("Height:", dog_info["Height"])
    print("Temperament:", dog_info["Temperament"])
