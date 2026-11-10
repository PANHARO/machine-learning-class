import subprocess
import re
from concurrent.futures import ThreadPoolExecutor

SUBNET = "192.168.1."

def ping(ip):
    subprocess.run(
        ["ping", "-n", "1", "-w", "300", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def scan_network():
    with ThreadPoolExecutor(max_workers=50) as executor:
        for i in range(1, 255):
            executor.submit(ping, f"{SUBNET}{i}")

def get_arp_table():
    output = subprocess.check_output(
        "arp -a",
        shell=True,
        text=True,
        encoding="utf-8"
    )

    pattern = r"(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F\-]+)\s+\w+"
    return re.findall(pattern, output)

if __name__ == "__main__":
    print("Scanning network...")
    scan_network()

    print("\nDevices found:\n")
    print(f"{'IP Address':<18} {'MAC Address'}")
    print("-" * 40)

    for ip, mac in get_arp_table():
        if ip.startswith(SUBNET):
            print(f"{ip:<18} {mac}")