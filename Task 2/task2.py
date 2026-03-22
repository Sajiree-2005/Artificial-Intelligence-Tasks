import cv2
import os
# Create output folder
os.makedirs("output_images", exist_ok=True)
# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
# Input images
image_paths = [
    "sample_images/input1.jpg",
    "sample_images/input2.jpg",
    "sample_images/input3.jpg"
]
for i, path in enumerate(image_paths):
    img = cv2.imread(path)
    if img is None:
        print(f"Error loading {path}")
        continue
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(f"{path} → Faces detected: {len(faces)}")
    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Save output
    output_path = f"output_images/output{i+1}.jpg"
    cv2.imwrite(output_path, img)
    # SHOW IMAGE
    cv2.imshow(f"Detected Faces {i+1}", img)
    cv2.waitKey(0)   # wait until key press
    cv2.destroyAllWindows()
    print(f"Saved: {output_path}")