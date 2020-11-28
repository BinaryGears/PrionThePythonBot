"""  Copyright 2020 BinaryGears
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
     http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License. """

# main.py
import os

import random

import discord

from discord.ext import commands

from dotenv import load_dotenv

import json

load_dotenv()


TOKEN = os.getenv('DISCORD_TOKEN')
PATHJOKE = os.getenv('JOKE_PATH')
PATHMUSIC = os.getenv('MUSIC_PATH')
PATHCONFESSION = os.getenv('CONFESSION_PATH')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

with open(PATHJOKE) as f:
    jokes = json.load(f)
    
with open(PATHMUSIC) as f:
    music = json.load(f)
    
with open(PATHCONFESSION) as f:
    confessions = json.load(f)
    
X = 'X'
O = 'O'
Z = 'Z'
P = 'P'
N = '\n'
    
class pgamePlayer:
    PlayerPosX = 5
    PlayerPosY = 7
    PrionGame = []
    

    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!prion':
        response = 'Hi, type !pcommands for a list of commands.'
        await message.channel.send(response)
        
    if message.content == '!pcommands':
        response = 'Commands List:' '```!pjoke : Will give you a random joke``` ```!pgame : Will give you a small game that is in alpha state``` ```!pmusic : Will give you a random song from youtube```'
        await message.channel.send(response)
    
    if message.content == '!preadconfessions':
        tempVar = random.randint(0, len(confessions) - 1)
        response = list(confessions.values())[tempVar]
        await message.channel.send(response)
     
        
    if message.content.startswith('!pconfessions'):
        confessions[str(len(confessions))] = str(message.content)
        tempFile = open(PATHCONFESSION, "w")
        
        json.dump(confessions, tempFile)
        tempFile.close()
        
    
        
    if message.content == '!pjoke':
        tempVar = random.randint(0, len(jokes) - 1)
        response = list(jokes.values())[tempVar]
        await message.channel.send(response)
        
    if message.content == '!pmusic':
        tempVar = random.randint(0, len(music) - 1)
        response = list(music.values())[tempVar]
        await message.channel.send(response)
        
    if message.content == '!pgame':
        pgamePlayer.PrionGame = [[X,X,X,X,X,X,X,X,X,X,X,X],[X,X,X,X,X,X,X,X,X,X,X,X],[X,X,X,X,X,X,X,X,X,X,X,X],[X,X,X,X,X,X,X,X,X,X,X,X],[X,X,X,X,X,X,X,X,X,X,X,X],[X,X,X,X,X,X,X,X,X,X,X,X],[X,X,X,X,X,X,X,X,X,X,X,X],[X,X,X,X,X,O,X,X,X,X,X,X]]
        response = '``` Game Map Legend``` ``` X : Undiscovered Area ``` ``` O : Player Character ``` ``` Z : Zombie ``` ``` P : Area You Have Been ```'
        await message.channel.send(response)
        response = str(pgamePlayer.PrionGame[0]) + '\n' + str(pgamePlayer.PrionGame[1]) + '\n' + str(pgamePlayer.PrionGame[2]) + '\n' + str(pgamePlayer.PrionGame[3]) + '\n' + str(pgamePlayer.PrionGame[4]) + '\n' + str(pgamePlayer.PrionGame[5]) + '\n' + str(pgamePlayer.PrionGame[6]) + '\n' + str(pgamePlayer.PrionGame[7]) + '\n'
        await message.channel.send(response)
        
        
    if message.content == '!pgamedown':
        if pgamePlayer.PlayerPosY < 7:
            pgamePlayer.PrionGame[pgamePlayer.PlayerPosY][pgamePlayer.PlayerPosX] = P
            pgamePlayer.PlayerPosY = pgamePlayer.PlayerPosY + 1
            pgamePlayer.PrionGame[pgamePlayer.PlayerPosY][pgamePlayer.PlayerPosX] = O
            response = str(pgamePlayer.PrionGame[0]) + '\n' + str(pgamePlayer.PrionGame[1]) + '\n' + str(pgamePlayer.PrionGame[2]) + '\n' + str(pgamePlayer.PrionGame[3]) + '\n' + str(pgamePlayer.PrionGame[4]) + '\n' + str(pgamePlayer.PrionGame[5]) + '\n' + str(pgamePlayer.PrionGame[6]) + '\n' + str(pgamePlayer.PrionGame[7]) + '\n'
            await message.channel.send(response)
            
        elif pgamePlayer.PlayerPosY == 7:
            response = str(pgamePlayer.PrionGame[0]) + '\n' + str(pgamePlayer.PrionGame[1]) + '\n' + str(pgamePlayer.PrionGame[2]) + '\n' + str(pgamePlayer.PrionGame[3]) + '\n' + str(pgamePlayer.PrionGame[4]) + '\n' + str(pgamePlayer.PrionGame[5]) + '\n' + str(pgamePlayer.PrionGame[6]) + '\n' + str(pgamePlayer.PrionGame[7]) + '\n'
            await message.channel.send(response)
            
        elif pgamePlayer.PlayerPosY > 7:
            pgamePlayer.PlayerPosY = 7
            response = 'You were displaced but now you are not'
            await message.channel.send(response)
            pgamePlayer.PrionGame[pgamePlayer.PlayerPosY][pgamePlayer.PlayerPosX] = O
            response = str(pgamePlayer.PrionGame[0]) + '\n' + str(pgamePlayer.PrionGame[1]) + '\n' + str(pgamePlayer.PrionGame[2]) + '\n' + str(pgamePlayer.PrionGame[3]) + '\n' + str(pgamePlayer.PrionGame[4]) + '\n' + str(pgamePlayer.PrionGame[5]) + '\n' + str(pgamePlayer.PrionGame[6]) + '\n' + str(pgamePlayer.PrionGame[7]) + '\n'
            await message.channel.send(response)
        
    if message.content == '!pgameup':
        if pgamePlayer.PlayerPosY > 0:
            pgamePlayer.PrionGame[pgamePlayer.PlayerPosY][pgamePlayer.PlayerPosX] = P
            pgamePlayer.PlayerPosY = pgamePlayer.PlayerPosY - 1
            pgamePlayer.PrionGame[pgamePlayer.PlayerPosY][pgamePlayer.PlayerPosX] = O
            response = str(pgamePlayer.PrionGame[0]) + '\n' + str(pgamePlayer.PrionGame[1]) + '\n' + str(pgamePlayer.PrionGame[2]) + '\n' + str(pgamePlayer.PrionGame[3]) + '\n' + str(pgamePlayer.PrionGame[4]) + '\n' + str(pgamePlayer.PrionGame[5]) + '\n' + str(pgamePlayer.PrionGame[6]) + '\n' + str(pgamePlayer.PrionGame[7]) + '\n'
            await message.channel.send(response)
            
        elif pgamePlayer.PlayerPosY == 0:
            response = str(pgamePlayer.PrionGame[0]) + '\n' + str(pgamePlayer.PrionGame[1]) + '\n' + str(pgamePlayer.PrionGame[2]) + '\n' + str(pgamePlayer.PrionGame[3]) + '\n' + str(pgamePlayer.PrionGame[4]) + '\n' + str(pgamePlayer.PrionGame[5]) + '\n' + str(pgamePlayer.PrionGame[6]) + '\n' + str(pgamePlayer.PrionGame[7]) + '\n'
            await message.channel.send(response)
            
        elif pgamePlayer.PlayerPosY < 0:
            response = 'You were displaced but now you are not'
            await message.channel.send(response)
            response = str(pgamePlayer.PrionGame[0]) + '\n' + str(pgamePlayer.PrionGame[1]) + '\n' + str(pgamePlayer.PrionGame[2]) + '\n' + str(pgamePlayer.PrionGame[3]) + '\n' + str(pgamePlayer.PrionGame[4]) + '\n' + str(pgamePlayer.PrionGame[5]) + '\n' + str(pgamePlayer.PrionGame[6]) + '\n' + str(pgamePlayer.PrionGame[7]) + '\n'
            await message.channel.send(response)
    
    #if message.content == '!pgameleft':
    #if message.content == '!pgame':
    
client.run(TOKEN)