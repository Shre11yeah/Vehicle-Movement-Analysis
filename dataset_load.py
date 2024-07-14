import os
import pandas as pd
import cv2
from datetime import datetime

def load_metadata(data_dir):
    records = []
    timestamp_formats = ["%Y-%m-%d %H:%M:%S", "%Y%m%d_%H%M%S", "%Y%m%d_%H%M", "%Y-%m-%d %H:%M"]

    for filename in os.listdir(data_dir):
        if filename.endswith("_metadata.txt"):
            with open(os.path.join(data_dir, filename), 'r') as f:
                metadata = {}
                for line in f:
                    try:
                        key, value = line.strip().split(": ")
                        metadata[key.strip()] = value.strip()
                    except ValueError:
                        continue  # Handle lines that don't split correctly

                if 'vehicle_timestamp' in metadata:
                    timestamp_str = metadata['vehicle_timestamp']
                    parsed = False
                    for fmt in timestamp_formats:
                        try:
                            metadata['vehicle_timestamp'] = pd.to_datetime(timestamp_str, format=fmt)
                            parsed = True
                            break
                        except ValueError:
                            continue
                    if not parsed:
                        print(f"Error parsing timestamp in file {filename} with value {timestamp_str}")
                        continue
                    
                    if pd.notna(metadata['vehicle_timestamp']):
                        records.append(metadata)
                    else:
                        print(f"Error parsing timestamp in file {filename} with value {timestamp_str}")
                else:
                    print(f"Warning: 'vehicle_timestamp' not found in file {filename}")

    return pd.DataFrame(records)


# def display_sample_image(image_path):
#     if not os.path.exists(image_path):
#         print(f"Error: The file {image_path} does not exist.")
#         return
    
#     image = cv2.imread(image_path)
#     if image is None:
#         print(f"Error: Failed to load image {image_path}.")
#         return
    
#     cv2.imshow('Sample Image', image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# Example Usage
if __name__ == "_main_":
    data_dir = "C:\\Users\\user\\Desktop\\Vehicle-Movement-Analysis-main\\Vehicle-Movement-Analysis-main\\Result"
    metadata = load_metadata(data_dir)
    
    if not metadata.empty:
        print(metadata.head())
    else:
        print("No metadata found.")