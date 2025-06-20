I have made a real time drowsiness detection system using openCv to connect with camera and used CSRT tracker to detect face.
It uses dlib library to detect face and alert if face goes out of frame.
If it detects face then using cnn model it checks for closed eyes or open eyes,if the person closes eyes for a particular number of frames,it alerts for closed eyes.
Pygame library is used to add the buzzer sound.
For efficient working of the system the distance from the camera must not be too far and a normal sitting distance sound be maintained.
