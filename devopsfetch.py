#!/usr/bin/env python3

import argparse
import subprocess
import logging
import os
from tabulate import tabulate

# Ensure the logs directory exists
log_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(log_dir, exist_ok=True)

# Configure logging
log_file = os.path.join(log_dir, 'devopsfetch.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(message)s')

def log_info(message):
    logging.info(message)

def get_active_ports():
    result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)
    log_info("Retrieved active ports")
    return parse_ports(result.stdout)

def get_port_info(port):
    result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)
    port_info = [line for line in result.stdout.splitlines() if f":{port} " in line]
    log_info(f"Retrieved information for port {port}")
    return parse_ports("\n".join(port_info))

def parse_ports(output):
    lines = output.splitlines()
    headers = ["Proto", "Local Address", "Foreign Address", "State"]
    data = []
    for line in lines:
        parts = line.split()
        if len(parts) >= 4:
            data.append(parts[:4])
    return headers, data

def list_docker_images():
    result = subprocess.run(['docker', 'images'], capture_output=True, text=True)
    log_info("Listed Docker images")
    return parse_docker_images(result.stdout)

def get_docker_info(container_name):
    result = subprocess.run(['docker', 'inspect', container_name], capture_output=True, text=True)
    log_info(f"Retrieved information for Docker container {container_name}")
    return result.stdout

def parse_docker_images(output):
    lines = output.splitlines()
    headers = lines[0].split()
    data = [line.split() for line in lines[1:]]
    return headers, data

def list_nginx_domains():
    result = subprocess.run(['nginx', '-T'], capture_output=True, text=True)
    log_info("Listed Nginx domains")
    return parse_nginx_domains(result.stdout)

def get_nginx_domain_info(domain):
    result = subprocess.run(['nginx', '-T'], capture_output=True, text=True)
    domain_info = parse_nginx_domain_info(result.stdout, domain)
    log_info(f"Retrieved configuration for Nginx domain {domain}")
    return domain_info

def parse_nginx_domains(output):
    lines = output.splitlines()
    headers = ["Server", "Proxy", "Port"]
    data = []
    for line in lines:
        if "server_name" in line:
            server_name = line.split()[1].strip(';')
            # Find the proxy and port
            proxy, port = None, None
            for i in range(1, 10):
                if "proxy_pass" in lines[lines.index(line) + i]:
                    proxy = lines[lines.index(line) + i].split()[1].strip(';')
                if "listen" in lines[lines.index(line) + i]:
                    port = lines[lines.index(line) + i].split()[1].strip(';')
            data.append([server_name, proxy, port])
    return headers, data

def parse_nginx_domain_info(output, domain):
    lines = output.splitlines()
    config = []
    capture = False
    for line in lines:
        if f"server_name {domain};" in line:
            capture = True
        if capture:
            config.append(line)
            if "}" in line:
                break
    return "\n".join(config)

def list_users():
    result = subprocess.run(['query', 'user'], capture_output=True, text=True)
    log_info("Listed users and their last login times")
    return parse_users(result.stdout)

def get_user_info(username):
    result = subprocess.run(['net', 'user', username], capture_output=True, text=True)
    log_info(f"Retrieved information for user {username}")
    return parse_user_info(result.stdout)

def parse_users(output):
    lines = output.splitlines()
    headers = ["Username", "Login ID"]
    data = [line.split()[:2] for line in lines[1:]]
    return headers, data

def parse_user_info(output):
    lines = output.splitlines()
    headers = ["Field", "Value"]
    data = [line.split(':', 1) for line in lines if ':' in line]
    return headers, data

def main():
    parser = argparse.ArgumentParser(description="DevOps system information retrieval tool")
    parser.add_argument('-p', '--port', nargs='?', const=True, help="Display active ports or specific port info")
    parser.add_argument('-d', '--docker', nargs='?', const=True, help="List Docker images/containers or specific container info")
    parser.add_argument('-n', '--nginx', nargs='?', const=True, help="List Nginx domains or specific domain info")
    parser.add_argument('-u', '--users', nargs='?', const=True, help="List users or specific user info")
    parser.add_argument('-t', '--time', help="Display activities within a specified time range")

    args = parser.parse_args()

    if args.port is not None:
        if args.port is True:
            headers, data = get_active_ports()
        else:
            headers, data = get_port_info(args.port)
        print(tabulate(data, headers=headers, tablefmt="grid"))

    elif args.docker is not None:
        if args.docker is True:
            headers, data = list_docker_images()
        else:
            data = get_docker_info(args.docker)
            headers = []
        print(tabulate(data, headers=headers, tablefmt="grid"))

    elif args.nginx is not None:
        if args.nginx is True:
            headers, data = list_nginx_domains()
        else:
            data = get_nginx_domain_info(args.nginx)
            headers = []
        print(tabulate(data, headers=headers, tablefmt="grid"))

    elif args.users is not None:
        if args.users is True:
            headers, data = list_users()
        else:
            headers, data = parse_user_info(get_user_info(args.users))
        print(tabulate(data, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
