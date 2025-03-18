import cv2
import numpy as np
import os
from keras.models import load_model

# Define the model path
model_path = os.path.join("FaceRecognition", "model.h5")

# Load the pre-trained model with error handling
if not os.path.exists(model_path):
    print("Error: Model not found! Please train the model first.")
    exit()

model = load_model(model_path)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Function to preprocess the input image
def preprocess_image(image_path):
    if not os.path.exists(image_path):
        print(f"Error: Image '{image_path}' not found!")
        exit()
        
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (160, 160))  # Resize to expected model input size
    img = img.astype('float32') / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Function to predict the face
def predict_face(image_path, class_names=None):
    img = preprocess_image(image_path)
    prediction = model.predict(img)
    
    # Get predicted class index
    predicted_class = np.argmax(prediction)
    
    # If class names exist, return label instead of index
    if class_names:
        predicted_label = class_names[predicted_class]
        return predicted_label
    return predicted_class

# Example usage
if __name__ == "__main__":
    image_path = os.path.join("FaceRecognition", "data", "1", "0.png")
    
    # Define class names (modify based on your dataset)
    class_names = [f"Person {i}" for i in range(100)]  # Example for 100 classes
    
    predicted_label = predict_face(image_path, class_names)
    print(f"Predicted Face: {predicted_label}")
