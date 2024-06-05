import discord
from discord.ext import commands
from utils.dice_roller_cyberpunk import roll_cyber, roll_cyber_dmg

class Cyberpunk(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='roll_cyber')
    async def roll_cyber_command(self, ctx, *, args):
        """
        Processes dice notation for Cyberpunk rolls and returns the results.

        Args:
            args (str): Dice notation, e.g., '10', '+5'.
        """
        result = roll_cyber(args)
        if isinstance(result, str):
            await ctx.send(result)
        else:
            rolls, final_result = result
            rolls_str = ', '.join(map(str, rolls))
            await ctx.send(f"Rolls: {rolls_str}\nFinal Result: {final_result}")

    @commands.command(name='roll_cyber_dmg')
    async def roll_cyber_dmg_command(self, ctx, *, args):
        """
        Processes dice notation for damage rolls in Cyberpunk and returns the results.

        Args:
            args (str): Dice notation, e.g., '10 2 head', '10 +5 head'.
        """
        result = roll_cyber_dmg(args)
        await ctx.send(result)

async def setup(client):
    await client.add_cog(Cyberpunk(client))
