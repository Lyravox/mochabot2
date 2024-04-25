import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
from datetime import datetime

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
        
        await interaction.response.send_message(f"Pong! My latency is {latency}ms.")
        
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
        
    
def setup(bot):
    bot.add_cog(Information(bot))