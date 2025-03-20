import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os

# Check for model existence
model_path = 'C:\\Django\\eWaste\\EWaste\\myApp\\scrap_classifier.h5'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

# Define your class names
class_names =  [
    "beverage-cans", "cardboard", "construction-scrap", "electrical-cables",
    "electronic-chips-or-device", "e-waste", "laptops", "medical", "metal",
    "metal-containers", "news-paper", "other-metal-objects", "paper",
    "paper-cups", "plastic", "plastic-bags", "plastic-bottles",
    "plastic-containers", "plastic-cups", "small-appliances", "smartphones",
    "spray-cans", "tetra-cups", "tetra-pak", "trash"
]

# Function to preprocess the image and make a prediction
def classify_image(img_path):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Image file not found at {img_path}")
    # Load the model
    model = load_model(model_path)
    # Load the image
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img)  # Convert to array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Rescale the image

    # Make predictions
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions, axis=1)[0]  # Get the index of the highest probability

    confidence = predictions[0][predicted_index] 
    # Map index to class name
    predicted_class = class_names[predicted_index]
    print(predicted_class, confidence)
    return predicted_class, confidence

'''
# MODEL CODE : 
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

'''
