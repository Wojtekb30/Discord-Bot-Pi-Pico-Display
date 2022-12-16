# bot.py
import os
import random
import serial
import time
import discord
from dotenv import load_dotenv
#from textblob import TextBlob
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1) #you may have to set proper serial port
def write_read(x):
    y = str(x)
    l = len(y)
    t = str(l)
    if l<10:
        t="00"+t
    if l>10 and l<100:
        t="0"+t
    if l>=100:
        t="100"
    arduino.write(bytes(t+y, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, I am InkBot'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    if message.content:
        wiadomosc = str(message.author)+": "+str(message.content)
        print(wiadomosc)
        value = write_read(wiadomosc)
        print(value)
        

client.run(TOKEN)
