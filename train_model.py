import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models


IMG_SIZE = 224
BATCH_SIZE = 8

# Load dataset
train_data = tf.keras.preprocessing.image_dataset_from_directory(
    "Dogs",
    image_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE
)

class_names = train_data.class_names
NUM_CLASSES = len(class_names)

print("Classes:", class_names)

# Load pretrained model
base_model = MobileNetV2(
    input_shape=(IMG_SIZE, IMG_SIZE, 3),
    include_top=False,
    weights="imagenet"
)

base_model.trainable = False  # freeze pretrained layers

# Build model
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(NUM_CLASSES, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train model
model.fit(train_data, epochs=10)

# Save model
model.save("dog_breed_model.h5")

print("\n✅ Model Training Complete!")
