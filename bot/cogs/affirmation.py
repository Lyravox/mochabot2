import nextcord
from nextcord.ext import commands, tasks
from datetime import time
import aiohttp

class Affirmation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.channel_id = int(1232542270046081044)
        self.affirmation_ping = int(1232547788190122044)
        
        self.daily_affirmation.start()
        
    def cog_unload(self):
        self.daily_affirmation.cancel()
        
    async def fetch_affirmation(self):
        
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.affirmations.dev/") as response:
        
                if response.status == 200:
        
                    data = await response.json()
        
                    return data['affirmation']
        
                return None
            
    @tasks.loop(hours=24)
    async def daily_affirmation(self):
        
        channel = self.bot.get_channel(self.channel_id)
        
        if channel:
        
            affirmation = await self.fetch_affirmation()
    
            if affirmation:
                
                embed = nextcord.Embed(title="Todays Affirmation", color=0x703c2f, description=affirmation)
        
                embed.set_thumbnail(url="https://i.ibb.co/4SfxXBy/affirmation.jpg")
        
                await channel.send(f"<@&{self.affirmation_ping}>", embed=embed)
            
            else:
                
                await channel.send("Could not fetch a quote D:")
                
        else:
        
            print("Affirmations channel not found!")
            
    @daily_affirmation.before_loop
    async def before_daily_affirmation(self):
        
        await self.bot.wait_until_ready()
        
def setup(bot):
    bot.add_cog(Affirmation(bot))