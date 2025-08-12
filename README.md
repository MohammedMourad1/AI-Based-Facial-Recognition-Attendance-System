# AI-Based Facial Recognition Attendance System

This Python-based system automates attendance tracking using facial recognition technology. It captures images of team members, encodes their facial features, and stores the data in Firebase. The system then utilizes these encodings to recognize faces in real-time and mark attendance accordingly.([GitHub][1], [GitHub][2])

<img width="1428" height="721" alt="image" src="https://github.com/user-attachments/assets/813deb4f-cc0c-4cd5-93b7-427b091796cd" />
<img width="1519" height="781" alt="image" src="https://github.com/user-attachments/assets/985bc752-3817-447f-abd4-80b4f339eb98" />

## 🛠️ Project Structure

* **ADDDATATODATABASE.py**: Captures images of team members and uploads their data to Firebase.
* **ENCODE.py**: Encodes the facial features from the captured images for recognition purposes.
* **main.py**: The main script that runs the attendance system, capturing live images, recognizing faces, and updating attendance records.
* **images/**: Directory containing images of team members for encoding.([GitHub][2], [GitHub][3])

## ⚙️ Setup Instructions

1. **Firebase Setup**:

   * Create a Firebase project on the [Firebase Console](https://console.firebase.google.com/).
   * Add the necessary authentication credentials to your project.
   * Create a Realtime Database on Firebase to store attendance data.
   * Note down the Firebase database URL for later use.([GitHub][2])

2. **Add Team Information**:

   * In the `ADDDATATODATABASE.py` file, add the information of the team members you want to track attendance for.
   * Run the script to add this data to the Firebase database.([GitHub][2])

3. **Image Directory Setup**:

   * Create a directory named `images/` to store images of team members.
   * Place images of each team member in this directory.([GitHub][2])

4. **Encoding Faces**:

   * In the `ENCODE.py` file, set the path to the directory containing team member images.
   * Run the script to encode faces and create encodings for each image.([GitHub][2])

5. **Main Configuration**:

   * In the `main.py` file, update the Firebase database URL with the one obtained earlier.
   * Ensure all other configurations meet your requirements.([GitHub][2])

## 🚀 Usage

* Ensure all necessary steps in the setup section are completed.
* Run the `main.py` script.
* The system will capture images, encode faces, and update attendance data on the Firebase database.([GitHub][2])

## 📦 Dependencies

* Python 3.x
* OpenCV
* NumPy
* Firebase SDK([GitHub][2])

## 🤝 Contributions

Feel free to fork the repository, submit issues, or create pull requests. Contributions are welcome!
Mohammed
Python 3.x
OpenCV
NumPy
Firebase SDK
*************
