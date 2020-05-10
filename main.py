import discord
from discord.ext import commands


botToken = 'Njg4MTQyMDY5MzMxNzg3Nzk3.XrfuAA.TXFmKVEuHzmK-GtqhgbqmV_D3JY'
bot = commands.Bot(command_prefix='*')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command(name='骂', help='使用方法： *骂 [脏话]')
# Print user messages to chat, only 1 whitespace between 2 words
async def 骂(ctx, *args):
    if len(args) < 1:
        await ctx.send(f' 你想骂啥？')
    else:
        user_mentioned = [user.mention for user in ctx.message.mentions]
        sentence = " ".join(args[len(user_mentioned)::])
        print(f"{' '.join(user_mentioned)} length of the user list: {len(user_mentioned)}")
        await ctx.send(f"{ ' '.join(user_mentioned) } {sentence}")

bot.run(botToken)


