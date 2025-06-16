import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("graduation-project.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://graduation-project-b2bae-default-rtdb.firebaseio.com/",
    'storageBucket': "graduation-project-b2bae.appspot.com"
})


#Importing the Student images
FolderPath = 'Celebs'
PathList = os.listdir(FolderPath)
print(PathList)
ImgList = []
StudentIds = []
for path in PathList:
      ImgList.append(cv2.imread(os.path.join(FolderPath,path)))
      StudentIds.append(os.path.splitext(path)[0])

      fileName = f'{FolderPath}/{path}'
      bucket = storage.bucket()
      blob = bucket.blob(fileName)
      blob.upload_from_filename(fileName)

      #print(os.path.splitext(path)[0])
print(StudentIds)

def findEncodings(ImagesList):
      EncodeList = []
      for img in ImagesList:
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            EncodeList.append(encode)
      return EncodeList
print ("Encoding started.....")
encodeListknown = findEncodings(ImgList)
encodeListknownwithIds = [encodeListknown, StudentIds]
print("Encoding Complete:)")


file=open("Encode.p", 'wb')
pickle.dump(encodeListknownwithIds,file)
file.close()
print("file saved")






