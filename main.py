import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ضع هنا ID القناة اللي حاب يرسل فيها رسالة التفعيل
VERIFICATION_CHANNEL_ID = 123456789012345678  # 🔴 غيّر الرقم

# ضع هنا اسم الرول اللي راح ينضاف لما يضغط ✅
VERIFIED_ROLE_NAME = "✅ Verified"

@bot.event
async def on_ready():
    print(f"✅ Bot online as {bot.user}")

    channel = bot.get_channel(VERIFICATION_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title="✅︱Verification",
            description=(
                "👋 أهلاً وسهلاً بك في السيرفر!\n\n"
                "🔐 قبل ما تدخل وتشوف كل القنوات، لازم تفعل نفسك:\n\n"
                "✅ اضغط على الريأكشن (✅) بالأسفل للحصول على رول التفعيل والدخول إلى السيرفر.\n\n"
                "🚫 إذا ما فعلت نفسك، ما رح تقدر تشوف باقي الرومات.\n\n"
                "✨ شكراً لتعاونك ونتمنى لك وقت ممتع معنا!"
            ),
            color=0x00ff00
        )
        message = await channel.send(embed=embed)
        await message.add_reaction("✅")


@bot.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == VERIFICATION_CHANNEL_ID and str(payload.emoji) == "✅":
        guild = bot.get_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name=VERIFIED_ROLE_NAME)
        if role:
            member = guild.get_member(payload.user_id)
            if member and not member.bot:
                await member.add_roles(role)
                print(f"✅ Added role {role.name} to {member.name}")


bot.run(os.getenv("TOKEN"))
