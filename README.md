DevopsFetch



DevOpsFetch is a powerful tool designed for DevOps professionals to easily retrieve and monitor system information. This tool gathers data about active ports, Docker images and containers, Nginx configurations, and user login activities. Additionally, it supports continuous monitoring through a systemd service, ensuring that logs are kept up-to-date and properly managed.

Features

- Port Information: Display all active ports and services, or detailed information about a specific port.
- Docker Information: List all Docker images and containers, or detailed information about a specific container.
- Nginx Information: Display all Nginx domains and their ports, or detailed configuration information for a specific domain.
- User Information: List all users and their last login times, or detailed information about a specific user.
- Continuous Monitoring: Implement a systemd service to monitor and log activities continuously with proper log rotation.

## Installation

### Prerequisites

- Python 3.x
- Pip
- Docker (for Docker-related functionality)
- Nginx (for Nginx-related functionality)
- Systemd (for setting up the monitoring service)

### Installation Steps

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-username/devopsfetch.git
    cd devopsfetch
    ```

2. **Run the Installation Script**:

    ```bash
    chmod +x install_devopsfetch.sh
    ./install_devopsfetch.sh
    ```

    This script will:
    - Install necessary dependencies.
    - Set up a systemd service for continuous monitoring.
    - Ensure the logs directory exists.

## Usage

### Command-Line Options

Run the `devopsfetch.py` script with the following options:

- **Ports**:
  - List all active ports: `python devopsfetch.py --port`
  - Get information about a specific port: `python devopsfetch.py --port <port_number>`

- **Docker**:
  - List all Docker images and containers: `python devopsfetch.py --docker`
  - Get information about a specific container: `python devopsfetch.py --docker <container_name>`

- **Nginx**:
  - List all Nginx domains and their ports: `python devopsfetch.py --nginx`
  - Get configuration information for a specific domain: `python devopsfetch.py --nginx <domain>`

- **Users**:
  - List all users and their last login times: `python devopsfetch.py --users`
  - Get information about a specific user: `python devopsfetch.py --users <username>`

- **Help**:
  - Display help message: `python devopsfetch.py -h`

### Examples

1. **List all active ports**:

    ```bash
    python devopsfetch.py --port
    ```

2. **Get information about port 80**:

    ```bash
    python devopsfetch.py --port 80
    ```

3. **List all Docker images**:

    ```bash
    python devopsfetch.py --docker
    ```

4. **Get information about a Docker container named `web_app`**:

    ```bash
    python devopsfetch.py --docker web_app
    ```

5. **List all Nginx domains**:

    ```bash
    python devopsfetch.py --nginx
    ```

6. **Get configuration information for the domain `example.com`**:

    ```bash
    python devopsfetch.py --nginx example.com
    ```

7. **List all users and their last login times**:

    ```bash
    python devopsfetch.py --users
    ```

8. **Get information about user `john_doe`**:

    ```bash
    python devopsfetch.py --users john_doe
    ```

## Continuous Monitoring

The installation script sets up a systemd service named `devopsfetch.service` for continuous monitoring. This service will run the DevOpsFetch script at startup and ensure logs are continuously updated.

### Managing the Service

- **Start the service**:

    ```bash
    sudo systemctl start devopsfetch.service
    ```

- **Stop the service**:

    ```bash
    sudo systemctl stop devopsfetch.service
    ```

- **Enable the service to start at boot**:

    ```bash
    sudo systemctl enable devopsfetch.service
    ```

- **Disable the service from starting at boot**:

    ```bash
    sudo systemctl disable devopsfetch.service
    ```

- **Check the status of the service**:

    ```bash
    sudo systemctl status devopsfetch.service
    ```

## Logging

Logs are stored in the `logs` directory within the `devopsfetch` directory. The log file is named `devopsfetch.log`.

### Log Rotation

The script ensures that logs are properly rotated to prevent disk space issues. Log rotation can be managed through the system's log rotation policies.

## Contribution

Feel free to fork this repository and contribute by submitting pull requests. Any improvements or suggestions are welcome!


With **DevOpsFetch**, system monitoring and information retrieval become straightforward and efficient, allowing DevOps professionals to focus on what truly matters—maintaining and improving system performance and reliability.
