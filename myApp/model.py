import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define parameters
img_height, img_width = 128, 128
batch_size = 32
num_classes = 25  # Update this based on your actual number of classes

# Define the model
def create_model(num_classes):
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
        layers.MaxPooling2D(pool_size=(2, 2)),
        
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Load training data
train_datagen = ImageDataGenerator(rescale = 1./255)
train_generator = train_datagen.flow_from_directory(
    'C:\Python\main\ScrapModel\Training Set',  # Path to training data
    target_size = (img_height, img_width),
    batch_size = batch_size,
    class_mode = 'categorical'  # Use 'sparse' for integer labels
)

# Create and train the model
model = create_model(num_classes)
model.fit(train_generator, epochs=10)  # Adjust epochs as needed

# Save the model
model.save('scrap_classifier.h5')