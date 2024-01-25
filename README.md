# KoTH
Documenting one way to reverse engineer the RF CTF KOTH challenge and an attempting at autmating becoming King



The repo (https://github.com/rfhs/rfhs-wiki/wiki/RF-CTF-King-Of-The-Hill) says that we need to:


    Host a Wi-Fi network for the ESP32 to connect to
    Scan for BLE devices matching: RFHS_XXXX
    Calculate CRC32("RFHS_XXXX") for Proof of Possession key
        Hint: CRC32("RFHS_1234") = 0xA84590D6 the proof of possession would be "a84590d6"
    Provision the ESP32 via BLE with the settings for their Wi-Fi network
    Successfully respond to the HTTP request made by the client in the allotted time
    Lather, rinse, repeat


Lets start by figuring out how the WiFi provisioning via BLE works for the esp32. 

Espressif thankfully have the demo code to do this in their arduino core repo: https://github.com/espressif/arduino-esp32/blob/master/libraries/WiFiProv/examples/WiFiProv/WiFiProv.ino
Additionally, they also provide a demo Android App for testing pruposes: https://play.google.com/store/apps/details?id=com.espressif.provble

This is greaat because it means that we can use each of those to test each other and validate that they both work if we make changes to either later


After installing the app and flashing the sketch it looks like we're able to both enter in a Prefix and enter our own POP. This means that if you dont want to mess with Arduiños and ESP32s, you could theoretically just use an android phone to try to quickly find the device, calculate the crc32 online using something like https://crc32.online/, connect to the 'Queen', enter the hash, and then provide the network creds to some network where you're drawing the rest of the owl when it comes to reply back to that get request with your team name and an OK 200.



I've modified the existing WifiProv.ino and the repo now contains a file called Queen.ino. That sketch should replicate the same functionality and funtion calls/methods that the contest ESP32 runs on, but I cant garentee that so I'd avoid making extremly specific stratagies based on this code. Additionally, you may want to mess around with the timings and order things are called, right now this replicates all the functionlaity (minus whatever the score keeping mechanis is) as closely as I care to make it, but it should be easy enough to figure out how to make the thing stop turning itself off every x minutes easyily enough.


