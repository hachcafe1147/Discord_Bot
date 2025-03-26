import os
import discord
from dotenv import load_dotenv
import random
import re
import MeCab
import asyncio

intents = discord.Intents.default()
intents.members = True  # メンバー関連のIntentsを有効化
client = discord.Client(intents=intents)

m = MeCab.Tagger("-Owakati")

load_dotenv()  # .envファイルを読み込む

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if TOKEN is None:
    raise ValueError("DISCORD_BOT_TOKEN が設定されていません")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions:
        verb = extract_verb(message.content)
        if verb:
            neg_verb = negate_verb(verb)
            reply = f'筋肉に聞いてみましょう…。おい、俺の筋肉、{verb}のかい？{neg_verb}のかい？どっちなんだい！'
            response = await message.channel.send(reply)
            await asyncio.sleep(5)
            options = [f'{verb}!!! パワー!!!!!!ｯﾊ!', f'{neg_verb}!!! パワー!!!!!!ｯﾊ!', 'ﾃﾞﾝ!ﾃﾞﾝ!ﾃﾃﾃﾃｰﾝﾃﾝ…ﾃﾞﾝ!ﾃﾞﾝ!ﾃﾃﾃﾃｰﾝﾃﾝ…', '!!!!!!!!!!']
            pfmSpecial1 = 0.02
            pfmSpecial2 = 0.008
            pfmNormal = (1 * 100 - pfmSpecial1 * 100 -pfmSpecial2 * 100) / 2 / 100
            weights = [pfmNormal, pfmNormal, pfmSpecial1, pfmSpecial2]
            reply = random.choices(options, weights=weights)[0]
            await response.edit(content=f"{response.content}\n{reply}")
            if reply == options[2]:
                await asyncio.sleep(7)
                await response.edit(content=f"{response.content}\n𝑻𝒉𝒊𝒔 𝒂𝒊𝒏'𝒕 𝒂 𝒔𝒐𝒏𝒈 𝒇𝒐𝒓 𝒕𝒉𝒆 𝒃𝒓𝒐𝒌𝒆𝒏-𝒉𝒆𝒂𝒓𝒕𝒆𝒅")
                await asyncio.sleep(5)
                await response.edit(content=f"{response.content}\nﾃﾞﾝ!ﾃﾞﾝ!ﾃﾃﾃﾃｰﾝﾃﾝ…ﾃﾞﾝ!ﾃﾞﾝ!ﾃﾃﾃﾃｰﾝﾃﾝ…")
                await asyncio.sleep(5)
                await response.edit(content=f"{response.content}\n𝑰 𝒂𝒊𝒏'𝒕 𝒈𝒐𝒏𝒏𝒂 𝒃𝒆 𝒋𝒖𝒔𝒕 𝒂 𝒇𝒂𝒄𝒆 𝒊𝒏 𝒕𝒉𝒆 𝒄𝒓𝒐𝒘𝒅")
                await asyncio.sleep(6)
                await response.edit(content=f"{response.content}\n𝒀𝒐𝒖'𝒓𝒆 𝒈𝒐𝒏𝒏𝒂 𝒉𝒆𝒂𝒓 𝒎𝒚 𝒗𝒐𝒊𝒄𝒆 𝒘𝒉𝒆𝒏 𝑰 𝒔𝒉𝒐𝒖𝒕 𝒊𝒕 𝒐𝒖𝒕 𝒍𝒐𝒖𝒅")
                await asyncio.sleep(6)
                await response.edit(content=f"{response.content}\nﾃﾞﾝ!!!!!!ﾃﾞﾝ!!!!!! It's my")
                await asyncio.sleep(2)
                await response.edit(content=f"{response.content}\nﾔｰ!!!!!!!!!!!!!!!!!!:jar:\n         :cheese: :cheese: :cheese: :cheese: :cheese:\n         :cheese: :cheese: :spaghetti: :cheese: :cheese:\n         :cheese: :cheese: :cheese: :cheese: :cheese:")
                await asyncio.sleep(5)
                await response.edit(content=f"{response.content}\n𝑭𝒊𝒏")
            
            if reply == options[3]:
                await asyncio.sleep(3)
                await response.edit(content=f"{response.content}\n見てください…とんでもないマッチョが居た形跡があります。")
                await asyncio.sleep(5)
                await response.edit(content=f"{response.content}\nMAX（重量）で置かれています。")
                await asyncio.sleep(5)
                await response.edit(content=f"{response.content}\n(ﾟДﾟ；≡；ﾟДﾟ)")
                await asyncio.sleep(2)
                await response.edit(content=f"{response.content}\n…まだ温かい。")
                await asyncio.sleep(3)
                await response.edit(content=f"{response.content}\n(ﾟДﾟ；≡；ﾟДﾟ)")
                await asyncio.sleep(2)
                await response.edit(content=f"{response.content}\n近くにとんでもないマッチョが居るかもしれない…。")
                await asyncio.sleep(7)
                await response.edit(content=f"{response.content}\n𝑭𝒊𝒏")


def extract_verb(text):
    parsed = m.parse(text).split()
    for word in parsed:
        if word.endswith('る') or word.endswith('う') or word.endswith('く') or word.endswith('ぐ') or word.endswith('す') or word.endswith('つ') or word.endswith('ぬ') or word.endswith('ぶ') or word.endswith('む'):
            if 'を' in text:
                noun, _, verb = text.partition('を')
                if not noun.endswith('の'):
                    return verb.split()[0]
            else:
                return word
    return None

def negate_verb(verb):
    if verb.endswith('る'):
        if verb == '切る':
            return '切らない'
        elif verb == '食べる':
            return '食べない'
        elif verb == '煮る':
            return '煮ない'
        elif verb == '煎る':
            return '煎らない'
        elif verb == '開ける':
            return '開けない'
        elif verb == '射る':
            return '射らない'
        elif verb == '別れる':
            return '別れない'
        elif verb == '寝る':
            return '寝ない'
        elif verb == '育てる':
            return '育てない'
        elif verb == '入る':
            return '入らない'
        elif verb == '当たる' or verb == 'あたる':
            return verb[:-1] + 'らない'
        elif verb == '付き合う':
            return '付き合わない'
        elif verb == '入れる':
            return '入れない'
        elif verb == '凸る':
            return '凸らない'
        elif verb == 'かける':
            return 'かけない'
        elif verb == 'すこる':
            return 'すこらない'
        elif verb == '譲る':
            return '譲らない'
        elif verb == '駆ける':
            return '駆けない'
        elif verb == '賭ける':
            return '賭けない'
        elif verb == '欠ける':
            return '欠けない'
        elif verb == '透ける':
            return '透けない'
        elif verb == '得る':
            return '得ない'
        elif verb == '賜る':
            return '賜らない'
        elif verb == '参る':
            return '参らない'
        elif verb == '嬲る':
            return '嬲らない'
        elif verb == '貶める':
            return '貶めない'
        elif verb == '掛ける':
            return '掛けない'
        elif verb == '下げる':
            return '下げない'
        elif verb == '配る':
            return '配らない'
        elif verb == '上げる':
            return '上げない'
        elif verb == '祈る':
            return '祈らない'
        elif verb == 'キメる':
            return 'キメない'
        elif verb == '出る':
            return '出ない'
        elif verb == '与える':
            return '与えない'
        elif verb == '感じる':
            return '感じない'
        elif verb == '空ける':
            return '空けない'
        elif verb == '乗り換える':
            return '乗り換えない'
        elif verb == '知る':
            return '知ることはない'
        elif verb == '迎える':
            return '迎えない'
        elif verb == '貼る':
            return '貼らない'
        elif verb == '張る':
            return '張らない'
        elif verb == '出来る' or verb == 'できる':
            return verb[:-1] + 'ない'
        else:
            return verb[:-2] + 'しない'
    elif verb.endswith('る'):
        return verb[:-2] + 'しない'
    elif verb.endswith('う'):
        return verb[:-1] + 'わない'
    elif verb.endswith('つ'):
        return verb[:-1] + 'たない'
    elif verb.endswith('く'):
        return verb[:-1] + 'かない'
    elif verb.endswith('ぐ'):
        return verb[:-1] + 'がない'
    elif verb.endswith('す'):
        return verb[:-1] + 'さない'
    elif verb.endswith('ぬ'):
        return verb[:-1] + 'なない'
    elif verb.endswith('ぶ'):
        return verb[:-1] + 'ばない'
    elif verb.endswith('む'):
        return verb[:-1] + 'まない'
    else:
        return verb + 'ない'


client.run(TOKEN)
