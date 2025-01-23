# Smart-Traffic-Lights-using-YOLOv8
This project is made to give a solution the traffic. It uses a camera to count the number of cars in various lanes, and depending on which lane has the most number of cars, that lane will turn green.

To run this program you'll need to have packeges installed. These packages include, ultralytics, opencv, tensorflow and YOLOv8 from the ultralytics library.
This is the second version of this,the first version used an ESP32-CAM as the camera, this version uses the default webcam of the pc you are using.

Things you need:
    
1.Arduino UNO    

2.Jumper Wires

3.Python IDlE

4.The Packages Stated above

5.Arduino IDE

6.ESP32-Cam(if available)

7.ESP32 Extension in aarduino IDE(If using esp32-cam)

8.Bread Board

9.LED's(Red,Green, Yellow if wanted)

10.Resistors(220 ohms)

Open your terminal/cmd and add the python idle location as the path.

Install ultralytics using the:
```bash
pip install ultralytics
```

Intall TesnorFlow using:
```bash
pip install tensorflow
```

Install OpenCv using:
```bash
pip install opencv-python
```

Install YOLOv8 using:
```bash
pip install yolov8
```

Circuit Connections:

(I) Connect the Green LED:

1. Anode (longer leg): Connect to digital pin 12 on the Arduino.

2. Cathode (shorter leg): Connect to one end of a 220Ω resistor.

3. The other end of the resistor connects to the GND rail on the breadboard.

(II)Connect the Red LED:

1. Anode (longer leg): Connect to digital pin 13 on the Arduino.

2. Cathode (shorter leg): Connect to one end of another 220Ω resistor.

3. The other end of the resistor connects to the GND rail on the breadboard.

(III)Power the Breadboard:

1. Connect the 5V pin on the Arduino to the positive rail of the breadboard.

2. Connect the GND pin on the Arduino to the negative rail of the breadboard.


