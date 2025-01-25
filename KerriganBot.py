import discord
import random
import os
import asyncio
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv, dotenv_values

class Client(commands.Bot):
    async def on_ready(self):
        print(f'I am the Swarm.... {self.user}')

        try:
            guild = discord.Object(id=1331434831044935870)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')

load_dotenv()

# Here we are initializing the discord object 
intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=int(os.getenv("CHANNEL_ID")))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('Hello Kerrigan'):
        sent_message = await message.channel.send(f'The <:hydralisk:1331472166323224697>Swarm<:hydralisk:1331472166323224697> Welcomes you {message.author}')
        await asyncio.sleep(2)
        await sent_message.edit(content='Actually...')
        await asyncio.sleep(2)
        await sent_message.edit(content='The <:hydralisk:1331472166323224697>***Swarm***<:hydralisk:1331472166323224697> is hungry...')
        await asyncio.sleep(2)
        await sent_message.edit(content='Prepare to be eaten...')
        await asyncio.sleep(2)
        await sent_message.edit(content='Not very substantial... At best an appetizer...')
        await asyncio.sleep(2)
        await sent_message.edit(content='Pathetic Mortal...')
        await asyncio.sleep(2)       
        await sent_message.delete()   

#Slash Command for rolling dice
@client.tree.command(name="rolldice", description="Roll Some Dice", guild=GUILD_ID)
async def rollDice(interaction: discord.Interaction, numberofdice: int, dicesize: int):
    sum = 0
    message = []
    response = ''

    if numberofdice < 1 or dicesize < 1:
        response = '<:zerg:1331472236330356836>Your Queen Disapproves of STUPIDITY!<:zerg:1331472236330356836> \nWe will feed your rotting corpse <:among_us_dead:1331474128875552813><:amongusdeadbody:1331474130331238450> to the Swarm <:hydralisk:1331472166323224697>'
    else:
        for x in range(numberofdice):
            roll = random.randint(1, dicesize)
            sum += roll
            # roll dice and append to message
            message.append(str(roll))
            if x != numberofdice-1:
                message.append(" + ")
            else:
                message.append(" ")

        if numberofdice > 1:
            message.append(f' = {sum}')
            response = '<:pride_d20:1331465613318557696> ' + ''.join(message) + ' <:pride_d20:1331465613318557696>'
        
        if numberofdice == 1:
            response = '<:pride_d20:1331465613318557696> ' + ''.join(message) + ' <:pride_d20:1331465613318557696>'
    
    
    await interaction.response.send_message(response)



client.run(os.getenv("QUEEN_OF_BLADES_DISCORD_BOT_KEY"))