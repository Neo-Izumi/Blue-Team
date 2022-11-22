from nextcord import Embed, Colour
import random



gif = [
    'https://media.tenor.com/sZAFBih2R54AAAAC/minions.gif',
    'https://media1.giphy.com/media/BPJmthQ3YRwD6QqcVD/giphy.gif?cid=790b7611b30d847fc98c6510b0d9d182369ec04a977fc234&rid=giphy.gif&ct=g',
    'https://media.tenor.com/OMTs4-UMRvEAAAAM/happy-for-you-congrats.gif',
    'https://media3.giphy.com/media/jJQC2puVZpTMO4vUs0/giphy.gif?cid=790b7611f433703f9ae86bb43c11a0eb15a2e5bcc1c2ef47&rid=giphy.gif&ct=g',
    'https://i.gifer.com/origin/16/162b41786d99b9d7e7b03549c4e19ae2_w200.gif',
    'https://www.reactiongifs.us/wp-content/uploads/2017/09/Brilliant-Americas-got-Talent.gif',
    'https://znews-photo.zingcdn.me/w660/Uploaded/yqdlcqrwq/2020_05_18/Z12518052020.png'
]

image = [
    'https://s.memehay.com/files/posts/20201014/be-gai-ao-hong-co-cai-nhin-nheo-mat-kho-hieu-2aa700ebb0abf0a8b85a9a6a43e6e31b.jpg',
    'https://image-us.eva.vn/upload/2-2019/images/2019-05-28/b-1559009233-57-width1200height628-watermark.jpg',
    'https://i.pinimg.com/originals/e8/ca/da/e8cada09c9cfb868cc1b5c50f33938bd.jpg',
    'https://img5.thuthuatphanmem.vn/uploads/2022/01/05/hinh-anh-khoc-mat-nhan-nhu-khi_043023144.jpg',
    'https://s.memehay.com/files/posts/20210217/be-gai-ao-hong-tro-mat-cuoi-kha-o.jpg',
    'https://cdn.g-smart.vn/2022/10/86380892dc98db8e48cafa7b967da31agau-truc-mat-cuoi-sau-mat-khoc.jpg'
]


def embed_command():
    embed = Embed(
        title = '----- Commands -----',
        color = Colour.random()
    )
    embed.set_thumbnail(url = 'https://raw.githubusercontent.com/FPTU-Ethical-Hackers-Club/FPTU-Ethical-Hackers-Club.github.io/main/assets/img/avatar.png')
    return embed
    
def embed_story(message):
    embed = Embed(
        title = '----- Story ------',
        color = Colour.random()
    )
    text = f'```{message}```'
    embed.add_field(
        name = '\U00002694  \U00002694  \U00002694  \U00002694  \U00002694  \U00002694  \U00002694  \U00002694  \U00002694  \U00002694',
        value = text, 
        inline = False
    )
    # embed.set_thumbnail(url = 'https://raw.githubusercontent.com/FPTU-Ethical-Hackers-Club/FPTU-Ethical-Hackers-Club.github.io/main/assets/img/avatar.png')
    return embed

def embed_error(message):
    embed = Embed(
        title = '----- Error -----',
        color = Colour.red(),
    )
    text = f"""```css\n[{message}]\n```"""
    embed.add_field(
        name = '\U0000274c  \U0000274c  \U0000274c  \U0000274c  \U0000274c  \U0000274c  \U0000274c  \U0000274c  \U0000274c  \U0000274c',
        value = text,
        inline = False
    )
    embed.set_image(url = random.choice(image))
    return embed

def embed_final(message):
    embed = Embed(
        title = f'\U0001F389 \U0001F389 Hurray!!! You\'ve done: {message} \U0001F38A \U0001F38A',
        colour = Colour.random(), 
    )
    embed.set_image(url = random.choice(gif))
    return embed

