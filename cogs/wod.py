import discord
from discord.ext import commands
from utils.dice_roller_wod import roll_dice_wod


class WoD(commands.Cog):
    def __init__(self, client):
        """
        Initializes the WoD (World of Darkness) cog with the provided client.
        """
        self.client = client

    @commands.command(name='wod_roll')
    async def roll_skill(self, ctx, *, arg):
        """
        A command to roll dice for World of Darkness (WoD) based on the provided argument.

        Args:
            ctx: The context in which a command is called.
            arg: The dice notation or argument for rolling dice in WoD.

        Usage:
            !wod_roll 10/6 e9
        """
        result = roll_dice_wod(arg)
        await ctx.send(f"WoD roll results:\n{result}")


async def setup(client):
    """
    The setup function to add the WoD cog to the client.

    Args:
        client: The Discord bot client.
    """
    await client.add_cog(WoD(client))
