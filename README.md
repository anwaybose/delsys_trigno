# delsys_trigno
ros2 data collection from Delsys Trigno sensors

## Step-1 Installation and setup
Download the package
```
git clone https://github.com/anwaybose/delsys_trigno.git
```
Install mosquitto and paho-mqtt
```
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients
sudo apt clean

pip3 install paho-mqtt
```

## Step-2 Initiate the broker
```
cd delsys_trigno
mosquitto -v -c test.conf
```

## Step-3 Build and Launch the mqtt_client and the trigno data collection package
In a new terminal
```
cd delsys_trigno
colcon build
source ./install/setup.bash

ros2 launch trigno_multi trigno_mqtt.launch.py 
```
## Step-4 check for available topics
In a new terminal
```
cd delsys_trigno
source ./install/setup.bash

ros2 topic list
```
