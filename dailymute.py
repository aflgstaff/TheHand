import discord
from discord.ext import tasks, commands
from discord.utils import get
import asyncio
from random import choice
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='h!', intents=intents)

#REPLACE THIS WITH THE ID OF BEEP BOOP
LOWEST_ADMIN_ROLE = 799679984226009159
#REPLACE THIS WITH THE ID OF STINKY
MUTED_ROLE = 817792570901266442

@tasks.loop(hours=24)
async def dothemute():
    channel = bot.get_channel(871211262481170463)
    gld = channel.guild
    async def raffle(usr):
        embed=discord.Embed(title="Successful squash!", description=user.name + "#" + user.discriminator + " has been squashed!", color=0xff0000)
        embed.set_footer(text="User ID: " + user.id)
        await channel.send(embed=embed)
        await user.send("Sucks, you got squashed. DM mods if you want to be unsquashed.")
        mutedrole = gld.get_role(817792570901266442)
        await user.add_roles(mutedrole)
        await asyncio.sleep(86400)
        if mutedrole in user.roles:
            await user.remove_roles(mutedrole)
            embed=discord.Embed(title="De-squash successful!", description=user.name + "#" + user.discriminator + " has been de-squashed!", color=0x20c000)
            embed.set_footer(text="User ID: " + user.id)
            await channel.send(embed=embed)
            await user.send("You have been unsquashed...")
    user = choice(gld.members)

    while user.top_role >= gld.get_role(LOWEST_ADMIN_ROLE) and user.top_role >= gld.get_role(MUTED_ROLE):
        user = choice(gld.members)

    await raffle(user)
# async def on_command_error(ctx, error):
    # if isinstance(error, discord.HTTPException.Forbidden):

@bot.event
async def on_ready():
    dothemute.start()
bot.run(# token)
