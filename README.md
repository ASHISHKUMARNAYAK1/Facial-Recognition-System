# Facial-Recognition-System
Face recognition is one of the important issues in object recognition and computer vision. In our day to day activities, a number of biometric applications are available for recognizing humans such as eye or iris recognition, fingerprint recognition, face recognition. Face is an important part of human being and requires detection for different applications such as security, forensic investigation. It requires proper techniques for face detection and recognition with challenges of different facial expressions, pose variations, occlusion, aging and resolution either in the frame of stationary object or video sequencing images Facial recognition is a way of identifying or confirming an individual’s identity using their face. Facial recognition systems can be used to identify people in photos, videos, or in real-time.•Facial recognition is a category of biometric security. Other forms of biometric software include voice recognition, fingerprint recognition, and eye retina or iris recognition. The technology is mostly used for security and law enforcement, though there is increasing interest in other areas of use.

HOW DOES FACIAL RECOGNITION WORK?
Any facial recognition algorithm uses biometrics to map out facial features captured in a video still or a photograph. That information is then compared to a database of faces. There are four general steps in the process, which we’ll explain further.

STEP 1: FACE DETECTION First, a camera will detect and recognize a human’s face – one that can either be in a crowd or alone. It is most easily detected when the person is looking straight at the camera. However, modern technological advances allow face recognition software to still work if the person’s face is angled slightly.

STEP 2: FACE ANALYSIS After detection and recognition, a photo will capture the face and will then be analyzed. The majority of face recognition technology use 2D images instead of 3D. This is because 2D photos are more readily correlated with public photos or pictures in a database (these are typically 2D as well). During analysis, the face will be separated into distinguishable landmarks – we can call these nodal points. A human face has eight nodal points. Face recognition technology will analyze each of these points – for example, the distance between your eyebrows.

STEP 3: CONVERTING AN IMAGE INTO DATA After analysis, each nodal point becomes a number in the application database. The entire numerical code is referred to as a faceprint. Just like how everybody has a unique thumbprint, everyone also has a unique faceprint.

STEP 4: MATCHING The final step of the process is finding a match. Your faceprint is compared to a database of other facial codes. The number of faces that are compared depends on the database and how many databases the software has access to. For instance, the FBA has access to 21 state databases, with 641 million photos across them. The facial recognition technology then identifies a match for your exact facial features – it returns the user with the found match and other relevant information, such as an address and a name


# In this two video link you will see how i made the project.
witch the full video
1. video link  https://drive.google.com/file/d/11g07o4PvQHHrKHiSU6Xtts6Jo3wpaVmI/view?usp=sharing
2. Video link  https://drive.google.com/file/d/1Y7qp-gh8QX-D_JC1oaPKs9_3BJeymbEB/view?usp=sharing

# How do you run my project in your pc.
1. First download the zip file .
2. Go to your python folder and open window power shell creat a virtual enviroment folder in a python following this command (python -m venv AzureVision) and activate the enviroment following this command (scripts/activate).you know your enviroment is activate when you see the enviroment name is the beginning.
3. Insatll following  libraries in the enviroment folder.
   pip install --upgrade azure-cognitiveservies-vision-face
   pip install pillow
   pip install pandas
4. Extract the zip file . And remove all the files in your environment folder  and add the zip file material(extract file) in your environment folder.
5. Go to your window power shell run the project. you write follwing command
   python Facial.py   
   and you see the output.
