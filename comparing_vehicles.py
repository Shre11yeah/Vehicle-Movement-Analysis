# import os
# from datetime import datetime
# import shutil

# # Paths to the directories
# dataset_directory = r"C:\Users\user\Desktop\Vehicle-Movement-Analysis-main\Vehicle-Movement-Analysis-main\data\vehicle_images"
# results_directory = r"C:\Users\user\Desktop\Vehicle-Movement-Analysis-main\Vehicle-Movement-Analysis-main\Result"

# # Function to compare images and create metadata for new captures
# def compare_and_create_metadata(dataset_dir, results_dir):
#     # Get the list of images in the dataset directory
#     dataset_images = {img for img in os.listdir(dataset_dir) if img.endswith(".jpg")}
    
#     # Get the list of images in the results directory
#     results_images = {img for img in os.listdir(results_dir) if img.endswith(".jpg")}
    
#     # Compare images and create metadata for new captures
#     for image_file in results_images:
#         base_name = os.path.splitext(image_file)[0]
        
#         # Check if the image is in the dataset
#         if image_file in dataset_images:
#             authorization_status = "Authorized"
#         else:
#             authorization_status = "Unauthorized"
        
#         # Create a metadata filename with "_metadata.txt"
#         metadata_filename = base_name + "_metadata.txt"
#         metadata_path = os.path.join(results_dir, metadata_filename)
        
#         # Use the current time as the timestamp for the captured images
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
#         # Write the metadata file
#         with open(metadata_path, 'w') as metadata_file:
#             metadata_file.write(f"vehicle_image_path: {os.path.join(results_dir, image_file)}\n")
#             metadata_file.write(f"vehicle_timestamp: {timestamp}\n")
#             metadata_file.write(f"authorization_status: {authorization_status}\n")
        
#         print(f"Created {metadata_filename} with timestamp {timestamp} and authorization status: {authorization_status}")
        
#         # Move the image and its metadata to the dataset directory
#         shutil.move(os.path.join(results_dir, image_file), os.path.join(dataset_dir, image_file))
#         shutil.move(metadata_path, os.path.join(dataset_dir, metadata_filename))

# # Call the function to compare images and create metadata for new captures
# compare_and_create_metadata(dataset_directory, results_directory)

# print("Comparison completed and metadata files created for new captures.")



# import os
# import cv2
# import pytesseract

# # Set the path to the Tesseract executable if it's not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# def preprocess_image(image):
#     """ Preprocess the image to enhance the license plate region. """
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
#     binary_image = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#     return binary_image

# def match_vehicle(license_plate_text, approved_db):
#     status = approved_db.get(license_plate_text, "Unauthorized")
#     print(f"License Plate: {license_plate_text}, Status: {status}")
#     return status

# if __name__ == "__main__":
#     try:
#         data_dir = r"C:\Users\user\Desktop\Vehicle-Movement-Analysis-main\Vehicle-Movement-Analysis-main\data\vehicle_images"
        
#         approved_db = {
#             "MH27BE6630": "Authorized", "MH27BV8448": "Authorized", "MH27BV6826": "Authorized",
#             "MH27DE7731": "Authorized", "MH27BE2954": "Authorized", "MH27DE8408": "Authorized",
#             "MH27BE7477": "Authorized", "MH01CP1574": "Authorized", "MH29R4300": "Authorized",
#             "MH27DL7212": "Authorized", "MH27BE9889": "Authorized", "MH27DL4474": "Authorized",
#             "MH27BZ4676": "Authorized", "MH27DE9744": "Authorized", "MH27BE4704": "Authorized",
#             "MH14JU4530": "Authorized", "MH27AC3897": "Authorized"
#         }
        
#         # Iterate over all files in the data directory
#         for filename in os.listdir(data_dir):
#             if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
#                 image_path = os.path.join(data_dir, filename)
#                 base_name = os.path.splitext(filename)[0]
#                 metadata_path = os.path.join(data_dir, base_name + "_metadata.txt")
                
#                 if os.path.exists(metadata_path):
#                     try:
#                         with open(metadata_path, 'r') as f:
#                             metadata = f.readlines()
#                             metadata_dict = {line.split(': ')[0]: line.split(': ')[1].strip() for line in metadata}
                        
#                         license_plate_text = metadata_dict.get('license_plate', None)
                        
#                         if license_plate_text:
#                             status = match_vehicle(license_plate_text, approved_db)
#                         else:
#                             print(f"License plate not found in metadata for image: {image_path}")
                    
#                     except Exception as e:
#                         print(f"Error reading metadata file: {metadata_path}")
#                         print(e)
#                 else:
#                     print(f"Metadata file not found for image: {image_path}")
    
#     except Exception as e:
#         print(f"Error processing images: {e}")


# shrutii 

# import os
# from datetime import datetime
# import shutil
# from detect import detect_license_plate

# # Paths to the directories
# dataset_directory = r"C:\Users\user\Desktop\Vehicle-Movement-Analysis-main\Vehicle-Movement-Analysis-main\data\vehicle_images"
# results_directory = r"C:\Users\user\Desktop\Vehicle-Movement-Analysis-main\Vehicle-Movement-Analysis-main\Result"



# # Function to compare images and create metadata for new captures
# def compare_and_create_metadata(dataset_dir, results_dir):
#     # Get the list of images in the dataset directory
#     dataset_images = {img for img in os.listdir(dataset_dir) if img.endswith(".jpg")}
    
#     # Get the list of images in the results directory
#     results_images = {img for img in os.listdir(results_dir) if img.endswith(".jpg")}
    
#     # Detect license plates in the results directory
#     detected_plates = detect_license_plate(results_dir)

#     approved_db = {"ABC123": "Authorized", "XYZ789": "Unauthorized"}  # Example approved database
    
#     # Compare images and create metadata for new captures
#     for image_file, license_plate_text in detected_plates.items():
#         base_name = os.path.splitext(image_file)[0]
        
#         # Check if the license plate is in the approved database
#         if license_plate_text in approved_db:
#             authorization_status = approved_db[license_plate_text]
#         else:
#             authorization_status = "Unauthorized"
        
#         # Create a metadata filename with "_metadata.txt"
#         metadata_filename = base_name + "_metadata.txt"
#         metadata_path = os.path.join(results_dir, metadata_filename)
        
#         # Use the current time as the timestamp for the captured images
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
#         # Write the metadata file
#         with open(metadata_path, 'w') as metadata_file:
#             metadata_file.write(f"vehicle_image_path: {os.path.join(results_dir, image_file)}\n")
#             metadata_file.write(f"vehicle_timestamp: {timestamp}\n")
#             metadata_file.write(f"license_plate_text: {license_plate_text}\n")
#             metadata_file.write(f"authorization_status: {authorization_status}\n")
        
#         print(f"Created {metadata_filename} with timestamp {timestamp} and authorization status: {authorization_status}")
        
#         # Move the image and its metadata to the dataset directory
#         shutil.copy(os.path.join(results_dir, image_file), os.path.join(dataset_dir, image_file))
#         shutil.copy(metadata_path, os.path.join(dataset_dir, metadata_filename))

# # Call the function to compare images and create metadata for new captures
# compare_and_create_metadata(dataset_directory, results_directory)

# print("Comparison completed and metadata files created for new captures.")


import cv2
import numpy as np
import easyocr
import os

def recognize_license_plate(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Failed to load image {image_path}.")
    
    # Preprocess the image for OCR
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Perform OCR using EasyOCR
    reader = easyocr.Reader(['en'])
    results = reader.readtext(binary_image)
    
    license_plates = []
    for (bbox, text, prob) in results:
        license_plates.append(text)
    
    return license_plates

def match_vehicle(captured_image_path, existing_metadata):
    # Recognize license plate from the captured image
    captured_license_plates = recognize_license_plate(captured_image_path)
    
    for captured_plate in captured_license_plates:
        for _, row in existing_metadata.iterrows():
            existing_license_plate = row['License-plate']
            if captured_plate == existing_license_plate:
                return {
                    'match': True,
                    'existing_data': row.to_dict()
                }
    
    return {'match': False}

# Test the functions if this file is executed directly
if __name__ == "__main__":
    sample_image_path = "path/to/sample_vehicle_image.jpg"
    sample_metadata = pd.DataFrame({
        'License-plate': ['ABC123', 'XYZ789'],
        'Other-data': ['Sample1', 'Sample2']
    })
    
    recognized_plates = recognize_license_plate(sample_image_path)
    print("Recognized license plates:", recognized_plates)
    
    match_result = match_vehicle(sample_image_path, sample_metadata)
    print("Match result:", match_result)



