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

> After writing the .img file to the SD card, boot your Raspberry Pi 4 for Raspbian installation.
## 2. Configure Raspberry Pi
  If you don't want to buy or you don't have a mouse and keybroad, VNC is a good choice. Raspberry Pi 4 model B provides WiFi module, so you  can just set up and use ssh to connect it.
  ```
  ssh cs244@192.168.xx.xxx
  ```
Its fromat is " **ssh username@your ip address** "
After that, you can just use CLI.
If you want to use GUI, I recommand to use VNC. Additionally, you don't need to worry about the problem about **dynamic IP address** (Usually the IP address will change in nowadays,or you set up a static IP address)
   You will need an ethernet cable (maybe also an adapter) and then connect to your Raspberry Pi and laptop.
   - Step 1 Open the termainal and check the IP address
 ```
    ifconfig
 ```
  You should see "bridge100" and see the **inet**
  ![](https://github.com/Terrylin2023/raapberry_pi_4_model_B/blob/main/screenshot/Screenshot%202024-04-11%20at%2023.16.17.png)
   - Step 2 Open the VNC(follow the installation from website and make sure you enable VNC on your Raspberry Pi) Ref:https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html
    ![](https://github.com/Terrylin2023/raapberry_pi_4_model_B/blob/main/screenshot/Screenshot%202024-04-11%20at%2023.24.53.png)
     Enter the "IP addrress **+1**" EX:ip=192.163.1.1

     You should enter 192.163.1.**2** Then you will be asked to enter your username and password.
### Success
![](https://github.com/Terrylin2023/raapberry_pi_4_model_B/blob/main/screenshot/Screenshot%202024-04-11%20at%2023.25.30.png)
     
     
## 3. Using camera module to capture picture and video
- capture picture
  ```
  libcamera-still -o demo.jpg
  ```
- capture video
  ```
  libcamera-vid -o demo.h264 -t 5000
  ```
> **-o** set the file name **-t** record time

## 4. Compile the code(usually it's opencv4 now)
```
g++ canny_util.c camera_canny.cpp -o camera_canny -I. `pkg-config --cflags --libs opencv4`
```
Test it
```
./camera_canny 1.0 0.2 0.6
```
## 5. Encoding the processed images into a video
```
ffmpeg -i frame%03d_s_1.00_l_0.20_h_0.60.pgm -pix_fmt yuvj420p frame_vid.h264
```
