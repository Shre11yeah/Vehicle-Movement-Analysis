# # ######################## ORIGINAL ########################################

# # # Module: eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_entry_exit_times(metadata):
    metadata['vehicle_timestamp'] = pd.to_datetime(metadata['vehicle_timestamp'], format='%Y%m%d_%H%M%S')
    metadata['hour'] = metadata['vehicle_timestamp'].dt.hour
    sns.histplot(metadata['hour'], bins=24, kde=False)
    plt.title('Vehicle Entry/Exit Times')
    plt.xlabel('Hour of Day')
    plt.ylabel('Frequency')
    plt.show()

def plot_parking_occupancy(metadata):
    metadata['vehicle_timestamp'] = pd.to_datetime(metadata['vehicle_timestamp'])
    metadata['date'] = metadata['vehicle_timestamp'].dt.date
    occupancy = metadata.groupby('date').size()
    occupancy.plot(kind='bar')
    plt.title('Parking Occupancy by Day')
    plt.xlabel('Date')
    plt.ylabel('Number of Vehicles')
    plt.show()

if __name__ == "__main__":
    from dataset_load import load_metadata

    data_dir = "data/vehicle_images"
    metadata = load_metadata(data_dir)

    if not metadata.empty:
        plot_entry_exit_times(metadata)
        plot_parking_occupancy(metadata)
    else:
        print("No metadata found.")


# ################## MODIFIED #######################
# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Path to the directory containing the metadata files
# metadata_directory = r"C:\\Users\\user\\Desktop\\Vehicle-Movement-Analysis-main\\Vehicle-Movement-Analysis-main\\data\\vehicle_images"

# # Function to load metadata from the metadata files into a DataFrame
# # def load_metadata(directory):
# #     data = []
# #     for file in os.listdir(directory):
# #         if file.endswith("_metadata.txt"):
# #             file_path = os.path.join(directory, file)
# #             with open(file_path, 'r') as f:
# #                 metadata = {}
# #                 for line in f:
# #                     key, value = line.strip().split(': ', 1)
# #                     metadata[key] = value
# #                 data.append(metadata)
# #     return pd.DataFrame(data)

# # # Load metadata into DataFrame
# # df = load_metadata(metadata_directory)

# # # Print column names to check if 'vehicle_height' is present
# # print("Column Names:", df.columns)

# # # Check the first few rows to inspect the data
# # print(df.head())


# def load_metadata(metadata_directory):
#     metadata = []
#     for filename in os.listdir(metadata_directory):
#         file_path = os.path.join(metadata_directory, filename)
#         with open(file_path, 'r') as file:
#             file_metadata = {}
#             for line in file:
#                 if ': ' in line:  # Check if the line contains the separator
#                     key, value = line.strip().split(': ', 1)
#                     file_metadata[key] = value
#             metadata.append(file_metadata)
#     return pd.DataFrame(metadata)

# # Example usage
# metadata_directory = 'C:\\Users\\user\\Desktop\\Vehicle-Movement-Analysis-main\\Vehicle-Movement-Analysis-main\\Result'
# df = load_metadata(metadata_directory)
# print(df.head())

# # Convert appropriate columns to numeric types
# if 'vehicle_height' in df.columns:
#     df['vehicle_height'] = pd.to_numeric(df['vehicle_height'], errors='coerce')
# else:
#     print("'vehicle_height' column is missing in the metadata files")

# if 'vehicle_width' in df.columns:
#     df['vehicle_width'] = pd.to_numeric(df['vehicle_width'], errors='coerce')
# else:
#     print("'vehicle_width' column is missing in the metadata files")

# # Convert vehicle_timestamp to datetime
# if 'vehicle_timestamp' in df.columns:
#     df['vehicle_timestamp'] = pd.to_datetime(df['vehicle_timestamp'], errors='coerce')
# else:
#     print("'vehicle_timestamp' column is missing in the metadata files")

# # Drop rows with missing values if necessary
# df = df.dropna()

# # Show basic info about the DataFrame
# print(df.info())

# # Plot occupancy over time if 'vehicle_timestamp' column exists
# if 'vehicle_timestamp' in df.columns:
#     plt.figure(figsize=(12, 6))
#     df['vehicle_timestamp'].value_counts().sort_index().plot()
#     plt.xlabel('Time')
#     plt.ylabel('Number of Vehicles')
#     plt.title('Vehicle Occupancy Over Time')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()
# else:
#     print("Cannot plot occupancy over time as 'vehicle_timestamp' column is missing")

# # Plot the distribution of parking spaces if 'parking_space' column exists
# if 'parking_space' in df.columns:
#     plt.figure(figsize=(12, 6))
#     sns.countplot(data=df, x='parking_space', order=df['parking_space'].value_counts().index)
#     plt.xlabel('Parking Space')
#     plt.ylabel('Number of Vehicles')
#     plt.title('Distribution of Parking Spaces')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()
# else:
#     print("Cannot plot distribution of parking spaces as 'parking_space' column is missing")

# # Plot the height and width of vehicles if both 'vehicle_height' and 'vehicle_width' columns exist
# if 'vehicle_height' in df.columns and 'vehicle_width' in df.columns:
#     plt.figure(figsize=(12, 6))
#     sns.scatterplot(data=df, x='vehicle_width', y='vehicle_height', hue='vehicle_type')
#     plt.xlabel('Vehicle Width (m)')
#     plt.ylabel('Vehicle Height (m)')
#     plt.title('Vehicle Dimensions by Type')
#     plt.legend(title='Vehicle Type')
#     plt.tight_layout()
#     plt.show()
# else:
#     print("Cannot plot vehicle dimensions as 'vehicle_height' or 'vehicle_width' column is missing")



# Module: eda.py
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# def plot_entry_exit_times(metadata):
#     metadata['vehicle_timestamp'] = pd.to_datetime(metadata['vehicle_timestamp'], format='%Y%m%d_%H%M%S')
#     metadata['hour'] = metadata['vehicle_timestamp'].dt.hour
#     sns.histplot(metadata['hour'], bins=24, kde=False)
#     plt.title('Vehicle Entry/Exit Times')
#     plt.xlabel('Hour of Day')
#     plt.ylabel('Frequency')
#     plt.show()

# def plot_parking_occupancy(metadata):
#     metadata['vehicle_timestamp'] = pd.to_datetime(metadata['vehicle_timestamp'])
#     metadata['date'] = metadata['vehicle_timestamp'].dt.date
#     occupancy = metadata.groupby('date').size()
#     occupancy.plot(kind='bar')
#     plt.title('Parking Occupancy by Day')
#     plt.xlabel('Date')
#     plt.ylabel('Number of Vehicles')
#     plt.show()

# if __name__ == "_main_":
#     from dataset_load import load_metadata

#     # data_dir = "C:\\Users\\user\\Desktop\\Vehicle-Movement-Analysis-main\\Vehicle-Movement-Analysis-main\\data"
#     data_dir = "C:\\Users\\user\\Desktop\\Vehicle-Movement-Analysis-main\\Vehicle-Movement-Analysis-main\\Result"
#     metadata = load_metadata(data_dir)

#     if not metadata.empty:
#         plot_entry_exit_times(metadata)
#         plot_parking_occupancy(metadata)
#     else:
#         print("No metadata found.")

