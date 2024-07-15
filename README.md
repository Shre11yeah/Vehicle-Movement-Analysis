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
* Dataset :- We build and used our own dataset for this Project.

# Acknowledgements
Intel® Unnati: Data-Centric Labs in Emerging Technologies
Giving Students the Intel Edge: [https://www.intel.in/content/www/in/en/corporate/unnati/overview.html]

# Directory Structure 
project/
│
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

# Results 
* Detection : ![Detect](https://github.com/user-attachments/assets/0f6fd76b-f49f-43c2-a059-695b5689301d)
* Entry-Exit : ![entry-exit](https://github.com/user-attachments/assets/83e1c6d6-44ac-4a85-9ddd-7c6aa79c5243)
* Occupancy :![occupancy](https://github.com/user-attachments/assets/6713ce84-56ec-47e7-a68f-777fe0358069)
* Data-Storage : ![data-storage](https://github.com/user-attachments/assets/0e65d631-23d4-4b42-9b7f-6e3c73d2ad29)
