# Module: data_preprocess.py
import os
import cv2
import numpy as np
from dataset_load import load_metadata

def preprocess_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file {image_path} does not exist.")
    
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Failed to load image {image_path}.")

    resized_image = cv2.resize(image, (640, 480))
    grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

if __name__ == "__main__":
    data_dir = "C:\\Users\\user\\Desktop\\Vehicle-Movement-Analysis-main\\Vehicle-Movement-Analysis-main\\Result"
    metadata = load_metadata(data_dir)
    
    if not metadata.empty:
        image_path = metadata.iloc[0]['vehicle_image_path']
        preprocessed_image = preprocess_image(image_path)
        
        cv2.imshow('Preprocessed Image', preprocessed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No metadata found.")