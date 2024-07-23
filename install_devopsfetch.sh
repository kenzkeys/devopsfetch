#!/bin/bash

# Update the package list and install necessary dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-pip net-tools

# Install the required Python packages
pip3 install tabulate

# Create the logs directory if it doesn't exist
mkdir -p $HOME/Music/devopsfetch/logs

# Set up the systemd service
SERVICE_FILE=/etc/systemd/system/devopsfetch.service

sudo bash -c "cat > $SERVICE_FILE" <<EOL
[Unit]
Description=DevOpsFetch Service
After=network.target

[Service]
Type=simple
ExecStart=$HOME/Music/devopsfetch/devopsfetch.py --port
WorkingDirectory=$HOME/Music/devopsfetch
Restart=always

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd to apply the new service
sudo systemctl daemon-reload

# Enable and start the service
sudo systemctl enable devopsfetch.service
sudo systemctl start devopsfetch.service

echo "DevOpsFetch installation and service setup complete."
