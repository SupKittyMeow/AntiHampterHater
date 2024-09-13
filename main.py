import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def getuser(ctx, role: discord.Role):
    await ctx.send("\n".join(str(member) for member in role.members))
                   
@bot.event
async def on_ready():
    print(f'Ready and logged in on {bot.user}')

@bot.event
async def on_member_update(before, after):
        for role in after.roles:
            if role.name == 'hates hampter':
                try:
                    await after.kick(reason='You wanted this!')
                    print('Kicked!')
                except discord.errors.Forbidden:
                     print('Oops... they are too strong to be kicked!')
                break


bot.run(os.environ['BOT_TOKEN'])
