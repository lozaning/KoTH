from bleak import BleakScanner
import asyncio
import subprocess
import zlib

async def scan_for_devices():
    while True:
        print("Scanning for devices...")
        devices = await BleakScanner.discover()
        for device in devices:
            if device.name and device.name.startswith('RFHS'):
                print(f"Found device: {device.name}")
                yield device
        await asyncio.sleep(1)  # Optional delay between scans

def provision_device(device_name, ssid, password):
    print(f"Provisioning device: {device_name}")
    pop = hex(zlib.crc32(device_name.encode('utf-8')) & 0xffffffff).upper()
    command = f"python esp_prov.py --transport ble --service_name '{device_name}' --ssid '{ssid}' --passphrase '{password}' --pop '{pop}'"
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True)
    print(f"Command output: {result.stdout.decode()}")
    print(f"Command error (if any): {result.stderr.decode()}")

async def main():
    ssid = input("Enter the SSID of the network: ")
    password = input("Enter the password of the network: ")
    async for device in scan_for_devices():
        provision_device(device.name, ssid, password)

if __name__ == "__main__":
    asyncio.run(main())
