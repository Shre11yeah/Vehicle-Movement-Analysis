# Problem-Statement :- Vehicle Movement Analysis and Insight Generation in a College Campus using Edge AI
![temp1](https://github.com/user-attachments/assets/ba472301-8232-4c77-b02f-1274681e0980)

# Mentors:- 
* Institute Mentor : Prof. Saurabh Shah 
* External Mentor :  Kalyana Devulapally

# Contributors:-
* Aabha Lokhande:[https://github.com/gitwithaabha]
* Sanskruti Tidke:[https://github.com/Sanskruti0208]
* Shruti Arsode: [https://github.com/Shruti192903]

# Project-Team
![3](https://github.com/user-attachments/assets/c7e9bd66-e785-498c-8384-b923a30ded0c)

# Objective 
The primary objective of this project is to develop an Edge AI-based solution that can analyze vehicle movement in and out of a college campus using data from cameras capturing vehicle photos and license plates. The solution should provide insights on vehicle movement patterns, parking occupancy, and match vehicles to an approved vehicle database.
# Project Insights
Our solution is capable of processing image data in real-time and provide insights on:
* Vehicle Movement Patterns: Analyze the frequency and timing of vehicle movement in and out of the campus, identifying peak times and patterns.
* Parking Occupancy: Monitor the occupancy of parking lots in real-time, identifying which parking lots are frequently occupied and at what times.
* Vehicle Matching: Match captured vehicle images and license plates to an approved vehicle database to identify unauthorized vehicles.

# Technologies Used
* OpenCV: Used for image processing and computer vision tasks.
* YOLO (You Only Look Once): Employed for real-time object detection to identify vehicles in images.
* OCR (Optical Character Recognition): Utilized to recognize text from license plates.
* Python: The primary programming language for developing the application.
* Tkinter: Used for creating graphical user interfaces for image upload.
* Pandas: Utilized for data manipulation and analysis.
* Numpy: Used for numerical operations on image data.
* MySQL: Originally considered for database management but replaced with CSV for simplicity.
* Haar Cascade: Used for detecting license plates within the detected vehicles.
* imutils: Provides convenient image processing functions, including contour handling.
* datetime: Used for timestamping images and metadata.
* Edge AI: Implements real-time vehicle detection and license plate recognition directly on the device, reducing latency and reliance on cloud services.

# Features
* Real-time Vehicle Detection: Uses YOLO for detecting vehicles in captured images.
* License Plate Recognition: Employs OCR to extract text from vehicle license plates.
* Database Integration: Compares detected license plates with an existing approved vehicle dataset.
* Image Capture: Supports both live camera feed and image upload for processing.
* Metadata Generation: Creates and stores metadata for captured images, including vehicle type, dimensions, parking space, and license plate information.
* Dataset :- The dataset used in this project was created entirely by our team.

# Acknowledgements
Intel® Unnati: Data-Centric Labs in Emerging Technologies
Giving Students the Intel Edge: [https://www.intel.in/content/www/in/en/corporate/unnati/overview.html]

# Project-Guide
Here's a step-by-step guide for setting up the project environment, running the project, and using its features:
# Step 1: Install Required Software
1)Python: Ensure you have Python 3.x installed on your machine. You can download it from python.org.

2)Pip: Ensure that pip is installed to manage Python packages. It usually comes with Python installations. You can check if you have it installed by running:
# Copy code
=> pip --version
3)Install Required Packages: Open a terminal or command prompt and run the following commands to install the required packages:
# Copy code
* pip install opencv-python
* pip install opencv-python-headless
* pip install numpy
* pip install pandas
* pip install pytesseract
* pip install Flask
* pip install imutils
4)Tesseract OCR: Install Tesseract OCR, which is required for the OCR functionality. You can find installation instructions for your operating system here. After installation, ensure that Tesseract is added to your system's PATH.

# Step 2: Download YOLOv4 Weights and Configuration Files
1)Download YOLOv4: Get the YOLOv4 configuration and weights files. You can download them from the following links:
* yolov4.cfg
* yolov4.weights
  
2)Place Files: Place yolov4.cfg and yolov4.weights in the project directory.

3)Haar Cascade File: Ensure that haarcascade_russian_plate_number.xml is also in the project directory.

# Step 3: Project Directory Structure
Ensure your project directory structure looks like this:

# Copy code
project/
├── app.py
├── dataset_load.py
├── dataset_preprocess.py
├── eda.py
├── comparing_vehicles.py
├── generate_insights.py
├── dataset_create.py
├── haarcascade_russian_plate_number.xml
├── yolov4.cfg
├── yolov4.weights
└── Result/

# Step 4: Running the Project
1)Open a Terminal: Navigate to the project directory where your app.py is located.

2)Run the Application: Execute the following command:
# Copy code
python app.py
(This will start the application and the server.)
3)Access the Application: Open a web browser and go to http://127.0.0.1:5000 to access the application.

# Step 5: Using the Application Features
1)Real-time Vehicle Detection:
   Use the live camera feed option in the application to capture real-time vehicle images and 
   detect vehicles using YOLO.
   
2)License Plate Recognition:
    Once a vehicle is detected, the application will automatically extract the license plate 
    information using OCR.
    
3)Database Integration:
    The detected license plates will be compared with your approved vehicle dataset, and 
    results will be displayed.
    
4)Image Capture:
    You can upload images from your local storage for processing, and the application will 
    analyze them.
    
5)Metadata Generation:
    Captured images will generate and store metadata, including vehicle type, dimensions, 
    parking space, and license plate information, which can be viewed in the results directory.

# Step 6: Viewing Results
Check the Result/ directory for stored images and generated metadata after running the application.

# Results 
* Detection : ![Detect](https://github.com/user-attachments/assets/0f6fd76b-f49f-43c2-a059-695b5689301d)
* Entry-Exit : ![entry-exit](https://github.com/user-attachments/assets/83e1c6d6-44ac-4a85-9ddd-7c6aa79c5243)
* Occupancy :![occupancy](https://github.com/user-attachments/assets/6713ce84-56ec-47e7-a68f-777fe0358069)
* Data-Storage : ![data-storage](https://github.com/user-attachments/assets/0e65d631-23d4-4b42-9b7f-6e3c73d2ad29)
