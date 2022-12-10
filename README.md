# Live Social Distancing and Mask Detection System using MediaPipe FaceDetection

- This application proctors examinee continuously throughout the exam using webcam and detects several methods of cheating with high accuracy and makes report of their cheating behaviour. 
- It has modules like Face detection, Face recognition, Face landmarks detection, Head pose estimation, Face spoof detection and Lips tracker.
- This application uses less cpu and RAM because we used robust and light weight models like BlazeFace face detector, FaceNet for face recogntion.
- Our application detects the following cheating methods:
  1. Detect if no person found in camera
  2. Detect if multiple people found in camera
  3. Unique Id assigned to each person
  4. Detect if people are wearing mask or not.
  5. Detect if two people are close to one another and are not practising social distance.
 


### Setup Instructions
1. Create and activate a virtual environment
2. Install dependencies `pip install -r requirements.txt`
3. Run main.py file for starting project `python main.py`

