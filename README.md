# AI-Based Facial Recognition Attendance System


This repository contains code for a face attendance system that utilizes Firebase for data storage. It consists of three main Python scripts: ADDDATATODATABASE.py, ENCODE.py, and main.py. The system captures images of team members, encodes their faces, stores the data in Firebase, and allows attendance tracking.

# Getting Started
To set up and use the system, follow these steps:
**************************************************
1. Firebase Setup
Create a Firebase project on the Firebase console.
Add the necessary authentication credentials to your project.
Create a Realtime Database on Firebase to store attendance data.
Note down the Firebase database URL for later use.
************************************************************************************************************************************************************************
2. Add Team Information
In the ADDDATATODATABASE.py file, add the information of the team members you want to track attendance for.
Run the script to add this data to the Firebase database.
************************************************************************************************************************************************************************
3. Image Directory Setup
Create a directory to store images of team members.
Place images of each team member in this directory.
************************************************************************************************************************************************************************
4. Encoding Faces
In the ENCODE.py file, set the path to the directory containing team member images.
Run the script to encode faces and create encodings for each image.
************************************************************************************************************************************************************************
5. Main Configuration
In the main.py file, update the Firebase database URL with the one obtained earlier.
Ensure all other configurations meet your requirements.
Usage
************************************************************************************************************************************************************************
To use the face attendance system:

Ensure all necessary steps in the setup section are completed.
Run the main.py script.
The system will capture images, encode faces, and update attendance data on the Firebase database.
Folder Structure
sql
Copy code
face-attendance-system/
│
├── ADDDATATODATABASE.py
├── ENCODE.py
├── main.py
│
├── images/ (Directory for team member images)
│   ├── member1.jpg
│   ├── member2.jpg
│   └── ...
│
└── README.md

# Dependencies
************
Python 3.x
OpenCV
NumPy
Firebase SDK
*************
