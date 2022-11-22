import asyncio
from nextcord import Embed
from discord_components import button, user, embed 
from nextcord.ext.commands import Cog, command, dm_only

class role_options(Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    
    @command(name = 'stages', description = 'all stages you need to walk through as a blue team member')
    @dm_only()
    async def stages(self, ctx): 
        roles = button.roles()
        author = ctx.message.author
        await ctx.send("```Hãy chọn tiến trình bạn muốn xử lý, chúng tôi sẽ hướng dẫn bạn thực hiện từng bước \U0001F44C```", view=roles, delete_after=10)
        await roles.wait()
        
        if roles.value == None:
            return
        
        
        elif roles.value == 'alert':
            user.dic_user[author.id].alert = True
            
            story = (
                f'Bạn cần kiểm tra và giám sát những files ghi lại các log và event, những hệ thống phát hiện và ngăn ngừa xâm nhập vào network (IDS, IPS được tích hợp trong firewall), ...\n\n'
                f'Theo đó, bạn cần đưa ra những đánh giá khẳng định được tính đúng sai của alert - kiểm chứng xem alert cảnh báo 1 sự cố thâm nhập là chính xác hay chỉ là 1 cảnh báo giả, ... - và còn nhiều việc bên lề khác nữa.\n\n'
                f'\U0001F4CC Note: đây là phần việc đầu tiên nhất và cần được thực hiện mỗi ngày để đảm bảo tính an toàn của hệ thống.'
            )
            
            suggest = embed.embed_command()
            suggest.add_field(name = '1. !log_files', value = 'check log files', inline = False)
            suggest.add_field(name = '2. !other_tasks', value = 'check for other messages', inline = False)
            suggest.add_field(name = '3. !help', value = 'display all commands', inline = False)
            
            await ctx.send(embed = embed.embed_story(story))
            await asyncio.sleep(3)
            await ctx.send(embed = suggest)
            
            
        elif roles.value == 'response':
            user.dic_user[author.id].incident = True
            
            story = (
                f'Đối với từng sự cố, sẽ có cách khắc phục khác nhau. Chúng ta sẽ cùng nhau tìm hiểu một vài cách thức cũng như những công cụ hỗ trợ hữu hiệu để giải quyết các vấn đề được ghi nhận lại tại stage Alert Analysis.\n\n' 
                f'Do lượng kiến thức cần thiêt để đảm nhận vị trí này trải rộng và sâu hơn nhiều so với việc bạn chỉ phân tích cảnh báo nên mức lương bạn nhận được cũng sẽ cao hơn nhiều đó \U0001F911.\n\n'
                f'Được rồi, xem những nhiệm vụ chúng ta có hôm nay nào !!!'
            )
            
            suggest = embed.embed_command()
            suggest.add_field(name = '1. !list_tasks', value = 'list all tasks', inline = False)
            suggest.add_field(name = '2. !help', value = 'display all commands', inline = False)
            await ctx.send(embed = embed.embed_story(story))
            await asyncio.sleep(3)
            await ctx.send(embed = suggest)
            
            
        elif roles.value == 'environment':
            await ctx.send('Checking for your process -----------')
            await asyncio.sleep(3)
            if user.dic_user[author.id].ca == True:
                await ctx.send('+) Analysed all alerts:  \U00002B55')
            elif user.dic_user[author.id].alert_check['check'] == False:
                await ctx.send('+) Check all log files:  \U0000274C')
            elif user.dic_user[author.id].alert_check['mess'] == False:
                await ctx.send('+) Check for other emails and messages:  \U0000274C')
                
            if user.dic_user[author.id].ftp_process >= 100:
                await ctx.send('+) Task no.1: deny ftp request:  \U00002B55')
            else:
                await ctx.send('+) Task no.1: deny ftp request:  \U0000274C')
                
            if user.dic_user[author.id].pen_process['finish'] == True:
                await ctx.send('+) Task no.2: actions to penetration that contain malware:  \U00002B55')
            else:
                await ctx.send('+) Task no.2: actions to penetration that contain malware:  \U0000274C')
                
            if user.dic_user[author.id].rep_process['finish'] == True:
                await ctx.send('+) Task no.3: report currently events happened to the server:  \U00002B55')
            else:
                await ctx.send('+) Task no.3: report currently events happened to the server:  \U0000274C')
                
            if user.dic_user[author.id].ssh_process['finish'] == True:
                await ctx.send('+) Task no.4: establish SSH connection:  \U00002B55')
            else:
                await ctx.send('+) Task no.4: establish SSH connection:  \U0000274C')
                
            if user.dic_user[author.id].ca == True and user.dic_user[author.id].ftp_process >= 100 and user.dic_user[author.id].pen_process['finish'] == True and user.dic_user[author.id].rep_process['finish'] == True and user.dic_user[author.id].ssh_process['finish'] == True:
                await asyncio.sleep(2)
                await ctx.send(embed = embed.embed_final('All tasks are finished'))
                await ctx.send('```EHC{Nguyễn_Doanh_Thịnh_Ethical_Hacker_Club}```')
        
def setup(bot):
    bot.add_cog(role_options(bot)) 