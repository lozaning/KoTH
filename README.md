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
