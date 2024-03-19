# imports
import statistics
import math
from translate import Translator

# discord imports
import discord
from discord.ext import commands
from discord import channel

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".",intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='功能請見"command list"', type=1))
    await bot.tree.sync()

@bot.tree.command(name="cal",description="Basic calculation")
async def cal(interaction:discord.Interaction, calc_input:str):
    calc_input = calc_input.replace('=',' ')
    calc_input = calc_input.replace('^', '**')
    calc_input = calc_input.replace('x', '*')
    if calc_input[len(calc_input)-1] in "-x*/^":
        calc_input = calc_input[:-1]
    ans = eval(calc_input)
    calc_input = calc_input.replace('**', '^')
    calc_input = calc_input.replace('*', 'x')
    ans = calc_input + " = " + str(ans)
    await interaction.response.send_message("```" + ans + "```")    

@bot.tree.command(name="mid",description="Calculate the median of a list of numbers. Use comma to separate numbers.")
async def cal(interaction:discord.Interaction, mid_input:str):
    if mid_input.endswith(","):
        mid_input = mid_input[:-1] # remove the last comma if any.
    List=mid_input.split(',')
    ans=[]
    for i in List:
        ans.append(float(i))
    ans="mid(" + mid_input + ") = " + str(statistics.median(ans))
    await interaction.response.send_message("```"+ans+"```")    

@bot.tree.command(name="avg",description="Calculate the average of a list of numbers. Use comma to separate numbers.")
async def cal(interaction:discord.Interaction, avg_input:str):
        if avg_input.endswith(","):
            avg_input = avg_input[:-1] # remove the last comma if any.
        List=avg_input.split(',')
        ans=[]
        for i in List:
            ans.append(float(i))
        ans="avg(" + avg_input + ") = " +str(statistics.fmean(ans))
        await interaction.response.send_message("```"+ans+"```")

@bot.tree.command(name="mod",description="Calculate the mode of a list of numbers. Use comma to separate numbers.")
async def cal(interaction:discord.Interaction, mod_input:str):
        if mod_input.endswith(","):
            mod_input = mod_input[:-1] # remove the last comma if any.
        List=mod_input.split(',')
        ans=[]
        for i in List:
            ans.append(float(i))
        ans = "mode(" + mod_input + ") = " + str(statistics.multimode(ans))
        await interaction.response.send_message("```"+ans+"```")

@bot.tree.command(name="fac",description="Calculate the factorial of a number")
async def cal(interaction:discord.Interaction, fac_input:str):
        number = int(fac_input)
        ans = fac_input + "! = " + str(math.factorial(number))
        await interaction.response.send_message("```"+ans+"```")

@bot.tree.command(name="p",description="Calculate P(n,m)")
async def cal(interaction:discord.Interaction, p_input:str):
        p_input = p_input.split(',')
        p_input[0],p_input[1] = int(p_input[0]),int(p_input[1])
        ans = math.factorial(p_input[0]) / math.factorial(p_input[1])
        ans = ("P(%d,%d) = " % (p_input[0],p_input[1])) + str(ans)
        await interaction.response.send_message("```"+ans+"```")

@bot.tree.command(name="c",description="Calculate C(n,m)")
async def cal(interaction:discord.Interaction, p_input:str):
        p_input = p_input.split(',')
        p_input = p_input.split(',')
        p_input[0],p_input[1] = int(p_input[0]),int(p_input[1])
        ans = math.factorial(p_input[0]) / math.factorial(p_input[1]) / math.factorial(p_input[0]-p_input[1])
        ans = ("C(%d,%d) = " % (p_input[0],p_input[1])) + str(ans)
        await interaction.response.send_message("```"+ans+"```")

@bot.tree.command(name="fib",description="Evaluate term using given number as position in Fibonacci sequence")
async def cal(interaction:discord.Interaction, fib_input:str):
        number = int(fib_input)
        fibArray = [1,1]
        for i in range(2,number):
             fibArray.append(fibArray[i-1] + fibArray[i-2])
        ans = "fib(%d) = " % (number) + str(fibArray[number-1])
        await interaction.response.send_message("```"+ans+"```")

@bot.tree.command(name="log",description="Calculate the logarithm of a number. Default base is 10.")
async def cal(interaction:discord.Interaction,log_input:int):
        ans = "```" + str(math.log10(log_input)) + "```"
        await interaction.response.send_message(ans)

@bot.tree.command(name="translate",description="Translate English to Chinese")
async def cal(interaction:discord.Interaction,translate_input:str):
        translator= Translator(to_lang="zh")
        translation = translator.translate(translate_input)
        if translation == translate_input and translate_input != "fuck":
            await interaction.response.send_message("cant translate")
        else:
            ans = translate_input + " -> " + translation
            await interaction.response.send_message(ans)

@bot.tree.command(name="sig",description="Calculate properties of a linear regression between two given numbers.")
async def cal(interaction:discord.Interaction, sig_input:str):
        if sig_input.endswith(","):
            sig_input = sig_input[:-1] # remove the last comma if any.
        def round2(x):
            return str(round(x,2))
        if ' ' in sig_input:
            sigmaX = []
            Sx = 0
            sigmaY = []
            Sy = 0
            Sxy = 0
            totalX = 0
            totalY = 0
            n = 0
            data = "sig," + sig_input

            for i in range(data.count(",")):
                sigmaX.append(int(data.split(",")[i+1].split(" ")[0]))
                totalX += int(data.split(",")[i+1].split(" ")[0])

                sigmaY.append(int(data.split(",")[i+1].split(" ")[1]))
                totalY += int(data.split(",")[i+1].split(" ")[1])

                n += 1

            averageX , averageY = totalX/n , totalY/n

            for i in range(n):
                Sx += (sigmaX[i] - averageX) ** 2
                Sy += (sigmaY[i] - averageY) ** 2
                Sxy += (sigmaX[i] - averageX) * (sigmaY[i] - averageY)

            r = Sxy / (Sx ** (1/2)) / (Sy ** (1/2))
            m = Sxy / Sx

            ans = "sigma(%s)\n" % sig_input
            ans += "n = %d \n" % n
            ans += "μx = %s \n" % round2(averageX)
            ans += "μy = %s \n" % round2(averageY)
            ans += "σx = %s \n" % round2((Sx/n) ** (1/2))
            ans += "σy = %s \n" % round2((Sy/n) ** (1/2))
            ans += "Sx = %s \n" % round2(Sx)
            ans += "Sy = %s \n" % round2(Sy)
            ans += "Sxy = %s \n" % round2(Sxy)
            ans += "r = %s \n" % round2(r)
            ans += "m = %s \n" % round2(m)
            ans += "L: y - %s = %s(x - %s)" % (round2(averageY),round2(m),round2(averageX))

        if ' ' not in sig_input:
            sigmaX = []
            totalX = 0
            squareTotal = 0
            n = 0
            Sx = 0
            data = "sig," + sig_input

            for i in range(data.count(",")):
                sigmaX.append(int(data.split(",")[i+1].split(" ")[0]))
                totalX += int(data.split(",")[i+1].split(" ")[0])

                n += 1

            averageX = totalX/n

            for i in range(n):
                squareTotal += sigmaX[i] ** 2
            
            ans = (squareTotal / n - averageX ** 2) ** (1 / 2)
            ans = ("sigma(%s) = " % sig_input) + str(round2(ans))

        await interaction.response.send_message("```"+ans+"```")

@bot.tree.command(name="killbot",description="Stop markbot process")
async def killbot(interaction:discord.Interaction):
    await interaction.response.send_message("Goodbye world!")
    print("Markbot is killed")
    await bot.close()

bot.run('token')