import nextcord
import asyncio

from nextcord.ui import View, Button
from nextcord import Interaction, ButtonStyle
from . import embed, user


#pick a role
class roles(View):
    
    def __init__(self):
        super().__init__(timeout=10)
        self.value = None
        
    @nextcord.ui.button(label = 'alert analysis', style = ButtonStyle.red)
    async def alert_analysis(self, button: Button, interaction: Interaction):
        id = interaction.user.id
        if user.dic_user[id].ca == True:
            button.disabled = True
            await interaction.response.send_message(embed = embed.embed_error('You have done this stage \U0001F643'), delete_after = 5)
            await interaction.edit_original_message(view = self)
        else: 
            message = f'Alert analysis: là nhiệm vụ ở tier-1. Y như cái tên, bạn cần phải phân tích các cảnh báo xảy ra đối với hệ thống mà bạn cần quan tâm.'
            await interaction.response.send_message(embed = embed.embed_story(message))
            await asyncio.sleep(2)
            self.value = 'alert'
            self.stop()
    
    @nextcord.ui.button(label = 'incident response', style = ButtonStyle.green)
    async def incident_response(self, button: Button, interaction: Interaction):
        id = interaction.user.id
        if user.dic_user[id].ftp_process >= 100 and user.dic_user[id].pen_process['finish'] == True and user.dic_user[id].rep_process['finish'] == True and user.dic_user[id].ssh_process['finish'] == True:
            button.disabled = True
            await interaction.response.send_message(embed = embed.embed_error('You have done this stage \U0001F643'), delete_after = 5)
            await interaction.edit_original_message(view = self)
        else:
            message = f'Incident response: là nhiệm vụ ở tier-2. Sau những cảnh báo mà bạn đã phân tích được, bạn đương nhiên sẽ cần phải thực hiện triển khai khắc phục những sự cố xảy ra cho hệ thống rồi. Bạn được trả lương để làm việc này mà \U0001F92A.'
            await interaction.response.send_message(embed = embed.embed_story(message))
            await asyncio.sleep(2)
            self.value = 'response'
            self.stop()
        
    @nextcord.ui.button(label = 'simulating vulnarable environment', style = ButtonStyle.gray)
    async def environment(self, button: Button, interaction: Interaction):
        message = '''Simulating the vulnarable environment ------------'''
        await interaction.response.send_message(message)
        await asyncio.sleep(2)
        self.value = 'environment'
        self.stop()
        
        
#pick a task       
class tasks(View):
    
    def __init__(self):
        super().__init__(timeout=20)
        self.value = None
        
    @nextcord.ui.button(label = 'FTP requests from strange IP addresses', style=ButtonStyle.danger, row=1)
    async def ftp(self, button:Button, interaction: Interaction):
        id = interaction.user.id
        if user.dic_user[id].ftp_process >= 100:
            button.disabled = True
            await interaction.response.send_message(embed = embed.embed_error('You have done this task \U0001F643'), delete_after = 5)
            await interaction.edit_original_message(view = self)
        else:
            message = f'Từ alert, ta biết rằng Antoine đã thách thức chúng ta bằng việc dùng bot net gửi FTP requests tới server. Muốn khắc phục được việc này, giải pháp của chúng ta là deny mọi FTP requests trước sau đó muốn làm gì thì làm.'
            await interaction.response.send_message(embed = embed.embed_story(message), delete_after = 5)
            await asyncio.sleep(2)
            self.value = 'ftp'
            self.stop()
        
    @nextcord.ui.button(label = 'Penatration containing malware', style=ButtonStyle.gray, row=2)
    async def pen(self, button:Button, interaction: Interaction):
        id = interaction.user.id
        if user.dic_user[id].pen_process['finish'] == True:
            button.disabled = True
            await interaction.response.send_message(embed = embed.embed_error('You have done this task \U0001F643'), delete_after = 5)
            await interaction.edit_original_message(view = self)
        else:
            message = (
                f'Ayya, Antoine bằng cách nào đó đã thâm nhập được vào hệ thống của chúng ta rồi, đặc biệt hơn, lần thâm nhập này chứa malware.\n\n'
                f'Đùa không vui rồi. Hắn đã căng. \U0001F631 \U0001F631 \U0001F631'
            )
            await interaction.response.send_message(embed = embed.embed_story(message))
            await asyncio.sleep(2)
            self.value = 'pen'
            self.stop()
    
    @nextcord.ui.button(label = 'Report events', style=ButtonStyle.blurple, row=3)
    async def rep(self, button:Button, interaction: Interaction):
        id = interaction.user.id
        if user.dic_user[id].rep_process['finish'] == True:
            button.disabled = True
            await interaction.response.send_message(embed = embed.embed_error('You have done this task \U0001F643'), delete_after = 5)
            await interaction.edit_original_message(view = self)
        else:
            message = (
                f'Hệ thống của tổ chức cần phải đảm bảo được tính khả dụng cho khách hàng.\n\n'
                f'Họ không quan tâm rằng chúng ta đang bị tấn công dù cho kẻ tình nghi có là một tên khét tiếng như Antoine.\n\n'
                f'Do vậy, ta cần viết một bản báo cáo chi tiết về 2 incidents mà ta ghi nhận được cho cấp trên để họ có thể đưa ra những chính sách chăm sóc khách hàng tạm thời cũng như ước tính thiệt hại và đền bù cho họ.'
            )
            await interaction.response.send_message(embed = embed.embed_story(message))
            await asyncio.sleep(2)
            self.value = 'rep'
            self.stop()
        
    @nextcord.ui.button(label = 'SSH connection for Professors', style=ButtonStyle.green, row=4)
    async def ssh(self, button:Button, interaction: Interaction):
        id = interaction.user.id
        if user.dic_user[id].ssh_process['finish'] == True:
            button.disabled = True
            await interaction.response.send_message(embed = embed.embed_error('You have done this task \U0001F643'), delete_after = 5)
            await interaction.edit_original_message(view = self)
        else:
            if user.dic_user[id].pen_process['research'] == False or user.dic_user[id].pen_process['netflow'] == False:
                suggest = embed.embed_command()
                suggest.add_field(name = '1. !list_tasks', value = 'list all tasks', inline = False)
                suggest.add_field(name = '2. !stages', value = 'all stages you need to walk through as a blue team member', inline = False)
                suggest.add_field(name = '3. !help', value = 'display all commands', inline = False)
                await interaction.response.send_message(f'```Từ từ đã nào, chuyên viên đã đến đâu, thử giải quyết vụ Antoine cố thâm nhập vào server đã!!!```', embed = suggest)
                self.stop()
            else:
                message = (
                    f'Khá khen cho Antoine đã khiến chúng ta phải khốn đốn như vầy. ¯\_(ツ)_/¯\n\n'
                    f'Tuy nhiên, những người dùng của chúng ta đã đến, các chuyên viên an ning mạng đến từ khắp nơi trên thế giới.\n\n'
                )
                await interaction.response.send_message(embed = embed.embed_story(message))
                self.value = 'ssh'
                self.stop()
        
    