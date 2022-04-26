import random
import discord
import json
import os
from discord.ext import commands
from governmentsecrets import sustoken # :tro:

prefix = "r!"
bot = commands.Bot(command_prefix = prefix)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        arg = error.param.name
        await ctx.send(f"You are missing the following parameters:\n {arg}")

@bot.event
async def on_ready():
  await bot.change_presence(status = discord.Status.do_not_disturb, activity = discord.Game('School'))
  print("School Bot is ready!")

@bot.command(name="ping", description="See how long it takes to contact the bot!")
async def ping(ctx):
    best_latency = round(bot.latency)
    await ctx.send(f"🏓 Pong! {best_latency}ms!")

@bot.command(name = "calculate", aliases = ["cal"])
async def calculate(ctx,sum):
    await ctx.send(f"{eval(sum)}\nIf this didn't work, try using **no spaces**")

@bot.command(name = "dice")
async def dice(ctx,sides):
    intsides = int(sides)
    side = random.randint(1,intsides)
    await ctx.send(side)

async def open_account(user):

  with open("easter.json", "r") as f:
    users = json.load(f)

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["eggs"] = 0
    users[str(user.id)]["xp"] = 0
  with open("easter.json", "w") as f:
    json.dump(users,f)
  return True

async def get_bank_data():
    with open("easter.json", "r+") as f:
        users = json.load(f)

@bot.command(name = "seasonal", aliases = ["es"])
async def easter_seasonal(ctx):
    await open_account(ctx.author)
    with open("easter.json", "r+") as f:
        users = json.load(f)
    israretrip = random.randint(1, 20)
    if israretrip == 7:
        eggs = random.randint(1, 250)
        xp = eggs // 15
        trueeggs = eggs * 5
        await ctx.send(f"you got {eggs} rare eggs! (which is the same as {trueeggs} regular eggs) <:pog:948815010719748116>\nyou also got {xp} xp!")
        users[str(ctx.author.id)]["eggs"] += trueeggs
        users[str(ctx.author.id)]["xp"] += xp
    else:
        got_eggs = random.randint(1, 6)
        if got_eggs == 3:
            await ctx.send("you got 0 eggs lmao :rofl:")
        else:
            eggs = random.randint(1, 25)
            xp = eggs // 10
            await ctx.send(f"you got {eggs} regular easter eggs! :egg:\nyou also got {xp} xp!")
            users[str(ctx.author.id)]["eggs"] += eggs
            users[str(ctx.author.id)]["xp"] += xp
    with open("easter.json", "w") as f:
        json.dump(users, f)

@bot.command(name = "seasonalbalance", aliases = ["sb"])
async def easter_balance(ctx):
    await open_account(ctx.author)
    with open("easter.json", "r+") as f:
        users = json.load(f)
    eggs = users[str(ctx.author.id)]["eggs"]
    xp = users[str(ctx.author.id)]["xp"]
    em=discord.Embed(title=f"{ctx.author}'s Easter Seasonal Balance")
    em.set_author(name=ctx.author)
    em.add_field(name="Eggs", value=eggs, inline=False)
    em.add_field(name="XP", value=xp, inline=False)
    em.set_footer(text="r!balance by RHPS Bot")
    await ctx.send(embed=em)

#@bot.command(name = "beg")
#@commands.cooldown(1, 30, commands.BucketType.user)
#async def beg(ctx):
#  await open_account(ctx.author)
#  users = await get_bank_data()
#  wallet_amt = users[str(ctx.author.id)]["wallet"]
#  earnings = random.randint(25, 100)
#  await ctx.send(f"{ctx.author.mention} Someone gave you {earnings} dollars")
#  users[str(ctx.author.id)]["wallet"] += earnings
#  with open("mainbank.json", "w") as f:
#    json.dump(users,f)

#user = ctx.author
#    found_egg = random.randint(1, 3)
#    await open_account(ctx.author)
#    users = await get_bank_data()
#    if found_egg == 1:
#        await ctx.send("you found 1 egg! :egg:")
#        users[str(ctx.author.id)]["Eggs"] += 1
#    else:
#        await ctx.send("you found nothing :rofl:")
#    debug = str(found_egg)
#    await ctx.send(f"debug: {debug}")

bot.run(sustoken)