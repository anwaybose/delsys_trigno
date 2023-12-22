# delsys_trigno
ros2 data collection from Delsys Trigno sensors

## Installation and setup
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

## Initiate the broker
```
cd delsys_trigno
mosquitto -v -c test.conf
```

## Build and Launch the mqtt_client and the trigno data collection package
In a new terminal
```
cd delsys_trigno
colcon build
source ./install/setup.bash

ros2 launch trigno_multi trigno_mqtt.launch.py 
```
## check for available topics
In a new terminal
```
cd delsys_trigno
source ./install/setup.bash

ros2 topic list
```
