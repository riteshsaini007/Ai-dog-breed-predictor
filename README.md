Dog Breed Classifier

AI-based dog breed classification system using Transfer Learning (MobileNetV2).
Yes, here I use a pre-trained model (MobileNetV2) because training from scratch is not possible on my machine. 
Also, here I use Supabase for the first time, and I don’t think Supabase is now my favorite database.
This is all I write in short and clear, but below I try to make it a professional README file, 
so please check this. Also, I have some future scope because sometimes it predicts the wrong dog, 
like Golden Retriever and another retriever, so I need more data to train the model again.

Features
Image-based breed prediction
Supabase integration for breed properties
Transfer learning using TensorFlow
Automatic dataset download from Supabase

1) Tech Stack
Python
TensorFlow / Keras
Supabase
NumPy

2) Project Structure
download_dataset.py
train_model.py
predict.py
Model
MobileNetV2 (Transfer Learning)

3)How It Works
Images stored in Supabase
Download locally for training
Model trained using CNN
Prediction fetches properties from Supabase
