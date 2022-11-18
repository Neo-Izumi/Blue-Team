from discord_components import user, embed
from nextcord import slash_command, Interaction, Embed
from nextcord.ext.commands import Cog
import asyncio

class start (Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    
    # ID = 1035593393381838888
    ID = 854547492670799932
    
    
        
    @slash_command(name = 'blue_team', description = 'choose to be a part of the blue team', guild_ids=[ID])
    async def blue_team(self, interaction: Interaction):
        userID = interaction.user.id
        author = interaction.user
        user.dic_user[userID] = user.user_attribute()
        await interaction.response.send_message('Yay!!!', delete_after=3, ephemeral=True)
        await author.create_dm()
        await author.dm_channel.send(f"""```ini\n[Hello {author.name}. Welcome to blue team]\n```""")
        
        story = (
            f'Chắc hẳn các bạn đã biết đến Antoine, một trong những hacker sừng sỏ và lừng danh trên thế giới và là kẻ thù truyền kiếp của tổ chức EHC chúng ta.\n\n'
            f'Ngay khi lọ huyết thanh siêu chiến binh được vận chuyển đến phòng thí nghiệm của tổ chức EHC, hắn ta nổ phát súng đầu tiên thách thức chúng ta bằng một vài hình thức tấn công sơ bộ vào hệ thống server của EHC.\n\n'
            f'Và bởi vì sự cố lần này, ngày hôm nay chắc chắn sẽ là một ngày rất bận rộn đối vói bạn.'
        )
        
        introduction = (
            f'OK. Là một thành viên hoạt động ở bộ phận Security, và đặc biệt là ở blue team, bạn sẽ cần thực hiện một số những công việc sau để ứng phó với sự cố sảy ra với server của tổ chức.\n\n'
            f'1. Thực hiện phân tích tất cả các alert, kiểm tra và xác minh được hệ thống của tổ chức có thực sự bị thâm nhập hay không.\n\n'
            f'2. Thực hiện những nhiệm vụ cần thiết và khắc phục từng sự cố mà chúng ta ghi nhận được.\n\n'
            f'3. Thực hiện giả lập môi trường để kiểm thử lại hệ thống bảo mật sau khi đã khắc phụ các sự cố.'
        )
        
        begin = embed.embed_story(story)
        intro = embed.embed_story(introduction)
        suggest = embed.embed_command()
        suggest.add_field(name = '!stages', value = 'all stages you need to walk through as a blue team member', inline = False)
        suggest.add_field(name = '!help', value = 'display all commands', inline = False)
        
        await author.dm_channel.send(embed = begin)
        await asyncio.sleep(5)
        await author.dm_channel.send(embed = intro)
        await asyncio.sleep(2)
        await author.dm_channel.send(embed = suggest)

        
def setup(bot):
    bot.add_cog(start(bot))
            

        
    
    



