import asyncio

from discord_components import user, embed
from nextcord.ext.commands import Cog, command, dm_only


class alert_analysis(Cog):

    def __init__(self, bot):
        self.bot = bot
        self.final = 'Khá nhiều việc bạn phải làm hôm nay ha!'
        self.next = (
            f'Tốt lắm, bạn vừa hoàn thành một nhiệm vụ cũng được coi là hàng ngày của chúng tôi. Bạn đang dần trở thành 1 thành viên của blue team rồi đó.\n\n'
            f'Tuy nhiên, mọi thứ chỉ vừa mới bắt đầu thôi, chúng ta đã xác định được những gì cần làm, giờ thì triển khai thôi.\n\n'
            f'Next stage \U000023ED'
        )
        
        

    @command(name='log_files', description='check log files')
    @dm_only()
    async def log_files(self, ctx):
        author = ctx.message.author
        if user.dic_user[author.id].alert == False: 
            deny = embed.embed_error('Permission denied \U0001F643')
            await ctx.send(
                embed = deny,
                delete_after = 5
            )
            return
        
        message1 = (
            f'Chà! nếu như bạn chưa biết thì log files là những files ghi lại những sự kiện đã xảy ra đối với hệ thống của bạn.\n\n'
            f'Hmmm... Có vẻ như Antoine đang cố gắng thực hiện rà soát đầu vào của server chúng ta thông qua việc gửi những FTP requests bằng bot net vào hệ thống\n\n'
            f'Hắn thậm chí còn cố gắng thâm nhập vào server nữa kìa. Âu mài gót nẹt \U0001F624 \U0001F624 \U0001F624'
        )
        
        await ctx.send('Performing analysing process-----------')
        await asyncio.sleep(2)
        await ctx.send('Done!!!')
        await asyncio.sleep(2)
        await ctx.send(embed = embed.embed_story(message1))
        await asyncio.sleep(5)
        user.dic_user[author.id].alert_check['check'] = True 
        
        if user.dic_user[author.id].alert_check['mess'] == False: 
            message2 = 'Còn nữa, hãy thử check những nhiệm vụ khác xem sao, biêt đâu lại có biến \U0001F9D0'
            suggest = embed.embed_command()
            suggest.add_field(name = '1. !other_tasks', value = 'check for other tasks', inline = False)
            suggest.add_field(name = '2. !help', value = 'display all commands', inline = False)
            await ctx.send(embed = embed.embed_story(message2))
            await asyncio.sleep(1)
            await ctx.send(embed = suggest)
        else:
            user.dic_user[author.id].ca = True
            suggest = embed.embed_command()
            suggest.add_field(name = '1. !stages', value = 'all stages you need to walk through as a blue team member', inline = False)
            suggest.add_field(name = '2. !help', value = 'display all commands', inline = False)
            congrat = embed.embed_final('Alert analysis')
            await ctx.send(self.final, embed = congrat)
            await asyncio.sleep(2)
            await ctx.send(embed = embed.embed_story(self.next))
            await asyncio.sleep(1)
            await ctx.send(embed = suggest)
            
            
            
    @command(name='other_tasks', description='check for other tasks')
    @dm_only()
    async def other_tasks(self, ctx):
        author = ctx.message.author
        if user.dic_user[author.id].alert == False: 
            deny = embed.embed_error('Permission denied \U0001F600')
            await ctx.send(
                embed = deny,
                delete_after = 5
            )
            return
        
        message1 = (
            f'Do tính chất đặc biệt của nhiệm vụ lần này (việc Antoine chiếm được huyết thanh siêu chiến binh có thể ảnh hưởng tới cả quốc gia), mà ngay cả bạn cũng cần phải làm báo cáo về những thứ đã diễn ra đối với hệ thống của EHC.\n\n'
            f'Bên cạnh đó, chúng ta đương nhiên đã nhờ những chuyên gia hàng đầu về an toàn an ninh mạng đến ứng phó với Antoine, họ cũng cần bạn thiết lập kết nối SSH tới server của tổ chức.'
        )
        
        await ctx.send(embed = embed.embed_story(message1))
        await asyncio.sleep(2)
        user.dic_user[author.id].alert_check['mess'] = True 
        
        if user.dic_user[author.id].alert_check['check'] == False:
            message2 = 'Này, đừng quên check cả log files nhé, bình thường chúng ta luôn bắt đầu với việc này mà'
            suggest = embed.embed_command()
            suggest.add_field(name = '1. !log_files', value = 'check log files', inline = False)
            suggest.add_field(name = '2. !help', value = 'display all commands', inline = False)
            await ctx.send(embed = embed.embed_story(message2))
            await asyncio.sleep(1)
            await ctx.send(embed = suggest)
        else:
            user.dic_user[author.id].ca = True
            suggest = embed.embed_command()
            suggest.add_field(name = '1. !stages', value = 'all stages you need to walk through as a blue team member', inline = False)
            suggest.add_field(name = '2. !help', value = 'display all commands', inline = False)
            congrat = embed.embed_final('Alert analysis')
            await ctx.send(self.final, embed = congrat)
            await asyncio.sleep(2)
            await ctx.send(embed = embed.embed_story(self.next))
            await asyncio.sleep(1)
            await ctx.send(embed = suggest)

def setup(bot):
    bot.add_cog(alert_analysis(bot))