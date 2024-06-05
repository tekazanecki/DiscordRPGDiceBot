from discord.ext import commands
from utils.dice_roller_general import roll_dice


class General(commands.Cog):
    def __init__(self, client):
        """
        Initializes the General cog with the provided client.
        """
        self.client = client

    @commands.command()
    async def roll(self, ctx, *, arg):
        """
        A command to roll dice based on the provided argument.

        Args:
            ctx: The context in which a command is called.
            arg: The dice notation or argument for rolling dice.

        Usage:
            !roll 2d6+3
        """
        result = roll_dice(arg)
        await ctx.send(f"Roll results:\n{result}")

    @commands.command(name='roll_sum')
    async def roll_sum(self, ctx, *, arg):
        """
        A command to roll dice and sum the results based on the provided argument.

        Args:
            ctx: The context in which a command is called.
            arg: The dice notation or argument for rolling dice.

        Usage:
            !roll_sum 2d6+3
        """
        result = roll_dice(arg)
        await ctx.send(f"Roll results:\n{result}")


async def setup(client):
    """
    The setup function to add the General cog to the client.

    Args:
        client: The Discord bot client.
    """
    await client.add_cog(General(client))
