# Raspberry_Pi_4_model_B

This is a project that using raspberry pi.

## 1. Install Raspberry Pi OS
  - Go to https://www.raspberrypi.com/software/  (Install Raspberry Pi OS using Raspberry Pi Imager)
  - Choose the option that fits your situation
    ![](https://github.com/Terrylin2023/raapberry_pi_4_model_B/blob/main/screenshot/Screenshot%202024-04-10%20at%2000.17.01.png)
    
There are many differnt ways to connect to Raspberry Pi, such as 
- **ssh**
- **ethernet**
- **VNC[https://magpi.raspberrypi.com/articles/vnc-raspberry-pi]**

Just make sure you edit the setting before you start writing .img file to SD card
![](https://github.com/Terrylin2023/raapberry_pi_4_model_B/blob/main/screenshot/Screenshot%202024-04-10%20at%2000.23.22.png)
Click **Enabled SSH**
![](https://github.com/Terrylin2023/raapberry_pi_4_model_B/blob/main/screenshot/Screenshot%202024-04-10%20at%2000.23.40.png)
Then, you must set up the **Username** and **Password**
![](https://github.com/Terrylin2023/raapberry_pi_4_model_B/blob/main/screenshot/Screenshot%202024-04-10%20at%2000.23.58.png)

> After writing the .img file to the SD card, boot your Raspberry Pi 3 for Raspbian installation.
## 2. Configure Raspberry Pi
  
   
## 3. Using camera module to capture picture and video
- capture picture
  ```
  libcamera-still -o demo.jpg
  ```
- capture video
  ```
  libcamrea-vid -o demo.h264 -t 5000
  ```
> **-o** set the file name **-t** record time


