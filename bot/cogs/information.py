import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
from datetime import datetime
import random

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # About/Help command
    @nextcord.slash_command(description="About the bot!")
    async def about(self, interaction: Interaction):
        
        url = str(self.bot.user.avatar.url)
        
        embed = nextcord.Embed(title=":coffee: About Me :coffee:", color=0x703c2f)
        embed.set_thumbnail(url=url)
        embed.add_field(name="", value="""Hello! 
                        
                        I am Mochabot, a bot developed by <@1136085806147182713> for The Witch's Hut Discord server.
                        The Witch's Hut: https://discord.gg/XF9hPFg69b
                        Github & Documentation: https://github.com/Lyravox/mochabot
                        
                        DM <@1136085806147182713> for any issues/questions related to me!""")
      
        await interaction.response.send_message(embed=embed)
      
    # Ping command  
    @nextcord.slash_command(description="Provides bot latency.")
    async def ping(self, interaction: Interaction):
        
        latency = int(self.bot.latency * 1000)
        
        embed = nextcord.Embed(title="Pong", color=0x703c2f, description=f"My latency is {latency}ms!")
        
        await interaction.response.send_message(embed=embed)
        
    # Rules command
    @nextcord.slash_command(description="Provides server rules.")
    async def rules(self, interaction: Interaction):
        
        embed = nextcord.Embed(title="Rules", color=0x703c2f, description="You can find server rules at <#1046164961845592074>!")
        
        embed.set_thumbnail(url=interaction.guild.icon.url)
                        
        await interaction.response.send_message(embed=embed)
        
    # Server information command
    @nextcord.slash_command(description="Provides server info.")
    async def server(self, interaction: Interaction):
        
        server = interaction.guild
        
        icon = server.icon.url
        owner = server.owner.mention
        creation = int(server.created_at.timestamp())
        timestamp = f"<t:{creation}:F>"
        
        embed = nextcord.Embed(title=f"{server} Information", color=0x703c2f)
        
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=f"{owner}")
        embed.add_field(name="Creation", value=f"{timestamp}")
        
        await interaction.response.send_message(embed=embed)
    
    # Member information command    
    @nextcord.slash_command(description="Provides information about a specific member.")
    async def user(self, interaction: Interaction, member: Member = None):
        
        if member is None:
            member = interaction.user
        
        avatar = member.avatar.url
        name = member.name
        mention = member.mention
        id = member.id
        creation = int(member.created_at.timestamp())
        timestamp = f"<t:{creation}:F>"
        
        embed = nextcord.Embed(title=f"{name}'s Information", color=0x703c2f)
        
        embed.set_thumbnail(url=avatar)
        embed.add_field(name="Member", value=mention)
        embed.add_field(name="Creation", value=timestamp)
        
        await interaction.response.send_message(embed=embed)
        
    # Avatar command
    @nextcord.slash_command(description="Provides a avatar of a specfic user.")
    async def avatar(self, interaction: Interaction, member: Member = None):
        
        if member is None:
            member = interaction.user
                    
        if member.avatar:
            
            url = member.avatar.url
            name = member.name
          
            embed = nextcord.Embed(title=f"{name}'s Avatar", color=0x703c2f)
        
            embed.set_image(url=url)
        
            await interaction.response.send_message(embed=embed)

        else:
          
          await interaction.response.send_message("That user dose not have a avatar!")          
      
    # Emoji command
    @nextcord.slash_command(description="Returns a list of server emojis")
    async def emojis(self, interaction: Interaction):
    
        emojis = interaction.guild.emojis
    
        if not emojis:
    
            await interaction.response.send_message("No custom emojis found in this guild.")
    
        list = [str(emoji) for emoji in emojis] 
    
        message = " ".join(list)
    
        embed = nextcord.Embed(title="Emoji List", color=0x703c2f, description=message)
        
        await interaction.response.send_message(embed=embed)
      
    # Random command
    @nextcord.slash_command(description="Picks a random number between two specified numbers.")
    async def random(self, interaction: Interaction, lower: int, upper: int):
        
        if lower >= upper:
            
            await interaction.response.send_message("The firs number must be less than the second number.")
            return
        
        result = random.randint(lower, upper)
        
        await interaction.response.send_message(f"Your random number is: {result}")
    
def setup(bot):
    bot.add_cog(Information(bot))