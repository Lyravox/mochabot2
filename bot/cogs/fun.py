import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
import os
from dotenv import load_dotenv
import aiohttp
import random

load_dotenv()

apod = os.getenv("APOD_KEY")

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
     
    # Cat command
            
    @nextcord.slash_command(description="Sends a random cat image.")
    async def cat(self, interaction: Interaction):
        
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.thecatapi.com/v1/images/search") as response:
        
                if response.status == 200:
        
                    data = await response.json()
                    url = data[0]['url']
              
                    embed = nextcord.Embed(title="Random Cat", color=0x703c2f)

                    embed.set_image(url=url)
                    
                    await interaction.response.send_message(embed=embed)
                    
                else:
                    
                    await interaction.response.send_message("Could not fetch a cat image D:")         
            
    # Duck command
    @nextcord.slash_command(description="Sends a random duck image.")
    async def duck(self, interaction: Interaction):
        
        async with aiohttp.ClientSession() as session:
            async with session.get("https://random-d.uk/api/random") as response:
                
                if response.status == 200:
                    
                    data = await response.json()
                    url =  data['url']
                    
                    embed = nextcord.Embed(title="Random Duck", color=0x703c2f)
                    
                    embed.set_image(url=url)
                    
                    await interaction.response.send_message(embed=embed)
                    
                else:
                    
                    await interaction.response.send_message("Could not fetch a duck image D:")
            
    # Dice command
    @nextcord.slash_command(description="Roll the dice.")
    async def dice(
        self,
        interaction: Interaction,
        sides: int = nextcord.SlashOption(
            description="Number of sides on the die",
            required=True,
            min_value=2,
            max_value=100
        ),
        amount: int = nextcord.SlashOption(
            description="Number of diec to roll.",
            required=True,
            min_value=1,
            max_value=100
        )
    ):
        
        rolls = [random.randint(1, sides) for _ in range(amount)]
        string = ", ".join(str(roll) for roll in rolls)
        
        embed = nextcord.Embed(title="Dice", color=0x703c2f, description=f"You rolled some dice and got: {string}")
        
        await interaction.response.send_message(embed=embed)
        
    # Coinflip command
    @nextcord.slash_command(description="Flips a coin")
    async def coinflip(self, interaction: Interaction):
        
        result = random.choice(['heads', 'tails'])
        
        embed = nextcord.Embed(title=":coin: Coinflip :coin:", color=0x703c2f, description=f"You got {result}!")
        
        await interaction.response.send_message(embed=embed)
        
    # APOD command
    @nextcord.slash_command(description="Provides the Astronomy Picture Of The Day (APOD)!")
    async def apod(self, interaction: Interaction):
        
        url = "https://api.nasa.gov/planetary/apod"
        
        params = {'api_key': apod}
        
        async with aiohttp.ClientSession() as session:
                        
            async with session.get(url, params=params) as response:
                
                if response.status == 200:
                    
                    data = await response.json()
                    
                    image = data.get("url")
                    explanation = data.get("explanation")

                    embed = nextcord.Embed(title="Astronomy Picture Of The Day", color=0x703c2f, description=explanation)
                    
                    embed.set_image(url=image)
                    
                    await interaction.response.send_message(embed=embed)
                    
                else:
                    
                    error = await response.text()
                    
                    print(f"Failed to retrive APOD. Status: {response.status}, Error: {error}")
                    
                    await interaction.response.send_message("Failed to fetch APOD :(")
        
def setup(bot):
    bot.add_cog(Fun(bot))