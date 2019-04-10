echo "Stopping WiFi"
screen -S WiFi -p 0 -X stuff "stop^M" || true
echo "Stopping GPIO"
screen -S GPIO -p 0 -X stuff "stop^M" || true

echo "Updating from GIT"
git pull

echo "Starting WiFi Service"
screen -dmS WiFi /home/pi/GPIOTEst/env/bin/python WiFiTest.py
echo "Starting GPIO Service"
screen -dmS GPIO /home/pi/GPIOTEst/env/bin/python GPIOTest.py
