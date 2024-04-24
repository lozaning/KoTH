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

## AiTM Network
This code is BYO(MITM), which is to say that it's left as an excersize to the reader to get hostapd installed along side DNSMasq and maybe a fLASK web server to reply. 

## Queen.ino
The repository now includes a file named `Queen.ino`, which is a modified version of the `WiFiProv.ino`. This sketch aims to replicate the functionality and function calls/methods of the contest ESP32. Note that it may not exactly match the contest ESP32, so avoid basing strategies on this code. Adjustments to timings and function calls may be necessary.

## Automated Provisioning
After exploring the use of protobuffs in my ESP32 code to provision the queen, I pivoted to using Espressif's Python code for provisioning, available [here](https://github.com/espressif/esp-idf/blob/master/tools/esp_prov/esp_prov.py).
The onboard BT module of a Raspberry Pi 4 works fine to run this software

I've created `BLEster.py`, a script to automate the provisioning process. Run the script, provide the SSID and password for your MITM setup, and the script will handle device scanning, CRC32 hashing, and provisioning calls. Once the 'Queen' is provisioned, the script returns to scanning for new devices.

## Do Know

That when i competed with this setup (actually an 'improved' version of this setup) at BSides charm, I managed to onboard and reply back to the contest ESP32 exactyl once, so know that if you use this code/tutorial you should not expect to do well without making some of your own imrprovments. 

## Do Know Even More

Im making even more improvmenets to my setup that I'll be bringing to DefCon, so you _really shouldnt expect to do well if you're just using this readme/code. This is mostly so you'vegot a good starting place for you to iterate off. After defcon i'll update this repo again with the setup i used to comepte there. 
