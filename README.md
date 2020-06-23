# SmartAttendanceSystem
SMART ATTENDANCE SYSTEM -> for real time marking the attendance of students using face recognition techniques. 

o Attendance maintenance is an important task in all the institutions to check the performance of students. Every institute has its own way to do so. Some use the old paper or file based approach and some have adopted methods of automatic attendance using some biometric techniques. There are many automatic methods available for this purpose. Face recognition is a technique of biometric recognition.
o It is considered to be one of the most successful applications of image analysis and processing; that is the main reason behind the great attention it has been given in the past several years. The facial recognition process can be divided into two main stages: processing before detection where face detection and alignment take place (localization and normalization), and afterwards recognition
occur through feature extraction and matching steps.
o This system uses the face recognition approach for the automatic attendance of students in the classroom without student’s intervention.
o This attendance is recorded by using a camera that captures images of students, detect the faces in images, compare the detected faces with the database and mark the attendance.


Face Detection
The main function of this step is to determine whether human faces appear in a given image, and where these faces are located at. The expected outputs of this step are patches containing each face in the input image. In order to make further face recognition system more robust and easy to design, face alignment are performed to justify the scales and orientations of these patches. Besides serving as the pre-processing for face recognition, face detection could be used for region of interest detection, retargeting, video and image classification, etc.

Feature Extraction
After the face detection step, human face patches are extracted from images. Directly using these patches for face recognition have some disadvantages, first, each patch usually contains over 1000 pixels, which are too large to build a robust recognition system. Second, face patches may be taken from different camera alignments, with different face expressions, illuminations, and may suffer from occlusion and clutter. To overcome these drawbacks, feature extractions are performed to do information packing, dimension reduction, salience extraction, and noise cleaning. After this step, a face patch is usually transformed into a vector with fixed dimension or a set of fiducial points and their corresponding locations. In some literatures, feature extraction is either included in face detection or face recognition.

.Face Recognition
After formulizing the representation of each face, the last step is to recognize the identities of these faces. In order to achieve automatic recognition, a face database is required to build. For each person, several images are taken and their features are extracted and stored in the database. Then when an input face image comes in, we perform face detection and feature extraction, and compare its feature to each face
class stored in the database. There are two general applications of face recognition, one is called identification and another one is called verification.
Face identification means given a face image, we want the system to tell who he / she is or the most probable identification; while in face verification, given a face image and a guess of the identification, we want the system to tell true or false about the guess.
