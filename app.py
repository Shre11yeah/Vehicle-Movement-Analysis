import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import cv2
import os
from dataset_create import capture_images
from generate_insights import generate_insights
from dataset_load import load_metadata
from comparing_vehicles import recognize_license_plate, match_vehicle

class VehicleAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Movement Analysis")
        self.root.geometry("800x600")  # Set the window size

        self.create_widgets()

    def create_widgets(self):
        self.capture_button = tk.Button(self.root, text="Capture Image", command=self.capture_image)
        self.capture_button.pack(pady=10)

        self.analyze_button = tk.Button(self.root, text="Analyze Dataset", command=self.analyze_dataset)
        self.analyze_button.pack(pady=10)

        self.eda_button = tk.Button(self.root, text="Show EDA", command=self.show_eda)
        self.eda_button.pack(pady=10)

        self.output_frame = ttk.Frame(self.root)
        self.output_frame.pack(fill='both', expand=True)

        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        self.metadata_text = tk.Text(self.root, height=5, width=70)
        self.metadata_text.pack(pady=10)

    def capture_image(self):
        output_dir = "C:\\Users\\user\\Desktop\\Vehicle-Movement-Analysis-main\\Vehicle-Movement-Analysis-main\\Result"
        image_path = capture_images(output_dir)
        messagebox.showinfo("Info", "Image captured successfully.")
        self.display_image(image_path)

    def display_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((250, 250), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)

        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

        license_plate, vehicle_data = self.get_metadata(image_path)
        self.display_metadata(license_plate, vehicle_data)

    def get_metadata(self, image_path):
        license_plate = recognize_license_plate(image_path)
        vehicle_data = match_vehicle(license_plate)
        return license_plate, vehicle_data

    def display_metadata(self, license_plate, vehicle_data):
        metadata_text = f"License Plate: {license_plate}\nVehicle Data: {vehicle_data}"
        self.metadata_text.delete('1.0', tk.END)
        self.metadata_text.insert(tk.END, metadata_text)

    def analyze_dataset(self):
        data_dir = "data/vehicle_images"
        metadata = load_metadata(data_dir)
        insights = generate_insights(metadata)
        messagebox.showinfo("Insights", "Analysis complete. Check console for details.")
        print(insights)

    def show_eda(self):
        for widget in self.output_frame.winfo_children():
            widget.destroy()

        data_dir = "data/vehicle_images"
        metadata = load_metadata(data_dir)

        # Example EDA: Vehicle Type Distribution
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        vehicle_types = metadata['vehicle_type'].value_counts()
        vehicle_types.plot(kind='bar', ax=ax, title='Vehicle Type Distribution')

        canvas = FigureCanvasTkAgg(fig, master=self.output_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleAnalysisApp(root)
    root.mainloop()
