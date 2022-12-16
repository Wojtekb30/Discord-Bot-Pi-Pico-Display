# Discord-Bot-Pi-Pico-Display
This bot recieves messages from a Discord server and then displays them over USB on E-Ink screen connected to Raspberry Pi Pico.

<b> How it works and more details: </b>

The Raspberry Pi Pico requires the 3-colour 7,5" 800x480 Waveshare Pico-ePaper-7.5-B. Pi Pico is connected to the computer via USB and runs its MicroPython program.

The Discord bot runs on the computer. When it recieves a message, it sends the text and message author over USB to the Pi Pico, which then displays the data on the E-Ink (and displays new messages and who written them in new rows).

This way you can track messages from the Discord server the bot is on.

This program is also a example/demo of USB Serial communication between computer and Pi Pico.

The WaveShare E-Ink is equipped with a reset button, you can use it to force clear the E-Ink screen and reset the Pico's program. This may crash the Discord bot on the PC though.

![image](https://user-images.githubusercontent.com/112283903/208149847-b6543520-6000-4bcf-acb2-a762e603fb13.png)
