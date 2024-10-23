import os
import platform
from monitoring.alert import send_alert  # Import the send_alert function to notify in case of network issues

# Target host for network diagnostics
TARGET_HOST = "www.alphavantage.co"


def ping_host(host):
    """
    Function to ping the host to check if it is reachable.
    """
    # Use `ping -c 1` for Unix/Linux or `ping -n 1` for Windows
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 1 {host}"
    response = os.system(command)

    if response == 0:
        print(f"{host} is reachable.")
    else:
        print(f"{host} is not reachable. Check your network settings.")
        send_alert("Network Diagnostic Alert", f"Host {host} is not reachable.")


def traceroute_host(host):
    """
    Function to perform traceroute to the host.
    """
    print(f"Performing traceroute to {host}...")
    param = "tracert" if platform.system().lower() == "windows" else "traceroute"
    command = f"{param} {host}"
    os.system(command)


if __name__ == "__main__":
    print("Starting Network Diagnostics...")
    ping_host(TARGET_HOST)
    traceroute_host(TARGET_HOST)
