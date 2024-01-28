# KoTH - RF CTF King of the Hill Automation

## Introduction
This repository documents a method for reverse-engineering the RF CTF King of the Hill (KoTH) challenge and attempts at automating the process of becoming the King.

## Requirements
According to the [RFHS Wiki](https://github.com/rfhs/rfhs-wiki/wiki/RF-CTF-King-Of-The-Hill), the challenge requires:

- Hosting a Wi-Fi network for the ESP32 to connect to.
- Scanning for BLE devices matching: `RFHS_XXXX`.
- Calculating CRC32("RFHS_XXXX") for the Proof of Possession key.
  - Hint: CRC32("RFHS_1234") = `0xA84590D6`. The proof of possession would be `a84590d6`.
- Provisioning the ESP32 via BLE with the settings for the Wi-Fi network.
- Successfully responding to the HTTP request made by the client within the allotted time.
- Lather, rinse, repeat.

## WiFi Provisioning via BLE
Espressif provides demo code for this purpose in their Arduino core repository, which can be found [here](https://github.com/espressif/arduino-esp32/blob/master/libraries/WiFiProv/examples/WiFiProv/WiFiProv.ino). They also offer a demo Android App for testing purposes, available on the [Google Play Store](https://play.google.com/store/apps/details?id=com.espressif.provble).

## Queen.ino
The repository now includes a file named `Queen.ino`, which is a modified version of the `WiFiProv.ino`. This sketch aims to replicate the functionality and function calls/methods of the contest ESP32. Note that it may not exactly match the contest ESP32, so avoid basing strategies on this code. Adjustments to timings and function calls may be necessary.

## Automated Provisioning
After exploring the use of protobuffs in my code to provision the queen, I pivoted to using Espressif's Python code for provisioning, available [here](https://github.com/espressif/esp-idf/blob/master/tools/esp_prov/esp_prov.py).

I've created `BLEster.py`, a script to automate the provisioning process. Run the script, provide the SSID and password for your MITM setup, and the script will handle device scanning, CRC32 hashing, and provisioning calls. Once the 'Queen' is provisioned, the script returns to scanning for new devices.

### Do Know

I've yet to participate in any of the in person CTF that this has been run at so I've got no clue if this will work. It will likely need some fidling to actually get it scoring once you're setup in the room. 
