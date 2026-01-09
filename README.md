Connect momentary switch on pin 23 and ground. 

TO RUN AT START UP AS SERVICE: 

sudo nano /etc/systemd/system/pi_button_shutdown.service

"""

[Unit]

Description=Button Power Control (gpiozero)

After=multi-user.target



[Service]

ExecStart=/usr/bin/python3 /home/pi/python/pi_button_shutdown/main.py

Restart=always

User=root


[Install]

WantedBy=multi-user.target

"""


ENABLE SERVICE AT STARTUP:

sudo systemctl daemon-reload

sudo systemctl enable pi_button_shutdown

sudo systemctl start pi_button_shutdown

