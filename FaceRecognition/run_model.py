import cv2
import numpy as np
import os
from keras.models import load_model

# === CONFIG ===
MODEL_PATH = os.path.join("FaceRecognition", "best_model.h5")
INPUT_SIZE = (160, 160)  # Match your model input size
class_names = [f"Person {i}" for i in range(100)] + ["me"]  # Adjust if needed

# === LOAD MODEL ===
model = load_model(MODEL_PATH)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print("✅ Model loaded.")

# === FACE DETECTION (OPTIONAL) ===
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# === Predict Function ===
def predict_face_from_frame(frame):
    face_img = cv2.resize(frame, INPUT_SIZE)
    face_img = face_img.astype('float32') / 255.0
    face_img = np.expand_dims(face_img, axis=0)
    
    prediction = model.predict(face_img, verbose=0)
    predicted_class = int(np.argmax(prediction))
    confidence = float(np.max(prediction))

    if predicted_class < len(class_names):
        return class_names[predicted_class], confidence
    return f"Unknown ({predicted_class})", confidence

# === WEBCAM LOOP ===
cap = cv2.VideoCapture(0)
print("🎥 Starting webcam... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Optional: detect faces
    faces = face_cascade.detectMultiScale(frame_rgb, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_crop = frame_rgb[y:y+h, x:x+w]
        label, confidence = predict_face_from_frame(face_crop)

        # Draw bounding box & label
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        text = f"{label} ({confidence:.1%})"
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)
    
    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
