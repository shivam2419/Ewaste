import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os

# Check for model existence
model_path = 'C:\\Python\\main\\ScrapModel\\classification_model.h5'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

# Load the model
model = load_model(model_path)

# Define your class names
class_names = ['beverage-cans',
    'cardboard',
    'construction-scrap',
    'e-waste',
    'electrical-cables',
    'electronic-chips',
    'gloves',
    'laptops',
    'masks',
    'medical',
    'medicines',
    'metal',
    'metal-containers',
    'news-paper',
    'other-metal-objects',
    'paper',
    'paper-cups',
    'plastic',
    'plastic-bags',
    'plastic-bottles',
    'plastic-containers',
    'plastic-cups',
    'small-appliances',
    'smartphones',
    'spray-cans',
    'syringe',
    'tetra-cups',
    'tetra-pak',
    'trash']

# Function to preprocess the image and make a prediction
def predict_image(img_path):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Image file not found at {img_path}")

    # Load the image
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img)  # Convert to array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Rescale the image

    # Make predictions
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions, axis=1)[0]  # Get the index of the highest probability

    # Map index to class name
    predicted_class = class_names[predicted_index]

    return predicted_class

# Example usage
img_path = r'C:\Users\LENOVO\Downloads\dlt4.jpeg'
predicted_class = predict_image(img_path)
print(f'Predicted class: {predicted_class}')
