import asyncio

from discord_components import button, user, embed
from nextcord.ext.commands import Cog, command, dm_only


class incident_response(Cog): 
    
    def __init__(self, bot):
        self.bot = bot
        
        
    
    @command(name='list_tasks', description='list all tasks you need to do')
    @dm_only()
    async def list_tasks(self, ctx):
        task = button.tasks()
        id = ctx.message.author.id
        if user.dic_user[id].incident == False:
            await ctx.send(
                embed = embed.embed_error('Permission denied \U0001F643'),
                delete_after = 5
            )
            return
        await ctx.send('Tất cả những cảnh báo mà bạn cần xử lý đây, cố lên nhé \U0001F609', view = task, delete_after=15)
        await task.wait()
        
        if task.value == None:
            return
        
        elif task.value == 'ftp':
            user.dic_user[id].ftp = True
            
            message = (
                f'Bạn muốn lọc gói tin gửi đến server của mình, bạn muốn chỉ định rõ request sử dụng giao thức nào được phép tới server, giao thức nào bị cấm, ... Chúng tôi xin trân trọng giới thiệu: Firewall.\n\n'
                f'Với Firewall, bạn có thể dễ dàng chặn lại các FTP request tới server của mình \U0001F91F.\n\n'
                f'Nào, mình cùng configure firewall thôi chứ nhỉ.'
            )
            
            suggest = embed.embed_command()
            suggest.add_field(name='1. !cfg_firewall', value='configure firewall', inline=False)
            suggest.add_field(name='2. !help', value='display all commands', inline=False)
            
            await ctx.send(embed = embed.embed_story(message))
            await asyncio.sleep(1)
            await ctx.send(embed = suggest)
        
        elif task.value == 'pen':
            user.dic_user[id].pen = True
            
            message1 = (
                f'Lần này khó à nha. Cần nhiều skills lắm đó.\n\n'
                f'Dưới đây là tất cả những lệnh bạn cần để giải quyết nhiệm vụ này.'
            )
            message2 = (
                f'Trông hỗn độn phết nhỉ \U0001F635 \U0001F635 \U0001F635\n\n'
                f'Trước hết, để tránh malware thể lây lan qua những hosts khác có cùng kết nối, chứ ta cứ thực hiện cô lập server bị thâm nhập cái đã.\n\n'
                f'Hãy ngắt mọi kết nối từ server này ra bên ngoài. Bao gồm cả những hosts con có nhiệm vụ liên quan, LAN, WAN và Internet.'
            )

            suggest = embed.embed_command()
            suggest.add_field(name='1. !disconnect', value='disconnect the penatrated server from other hosts', inline=False)
            suggest.add_field(name='3. !backup', value='obtain backup files for the injured server', inline=False)
            suggest.add_field(name='4. !roll_back', value='rolls back all sessions', inline=False)
            suggest.add_field(name='5. !restore', value='restore the whole system to previous daily backups', inline=False)
            suggest.add_field(name='6. !research', value='research for more information of that malware', inline=False)
            suggest.add_field(name='7. !trace_net_flow', value='trace to the network flow', inline=False)
            suggest.add_field(name='8. !help', value='display all commands', inline=False)
            
            await ctx.send(embed = embed.embed_story(message1))
            await asyncio.sleep(1)
            await ctx.send(embed = suggest)
            await asyncio.sleep(2)
            await ctx.send(embed = embed.embed_story(message2))
            
        elif task.value == 'rep': 
            user.dic_user[id].rep = True
            
            message = (
                f'Kiểm tra lại hệ thống là cần thiết để chắc chắn rằng chúng ta không gặp thêm một trục trặc gì.\n\n'
                f'Sau đó thu thập thông tin và ghi nhận lại các events để viết báo cáo.'
            )
            
            suggest = embed.embed_command()
            suggest.add_field(name='1. !check_system', value='perform checking for the whole system', inline=False)
            suggest.add_field(name='2. !record_all_events', value='Record all events and write a report to your manager.', inline=False)
            suggest.add_field(name='3. !help', value='display all commands', inline=False)
            
            await ctx.send(embed = embed.embed_story(message))
            await asyncio.sleep(1)
            await ctx.send(embed = suggest)
            
        elif task.value == 'ssh':
            user.dic_user[id].ssh = True
            
            message = (
                f'Họ sẽ là làm những việc còn lại giúp chúng ta như dọn dẹp back door hoặc thực hiện các biện pháp tăng cường phòng thủ trước những đợt tấn công tương tự trong tương lai.\n\n'
                f'Nhưng trước hết thì cứ phải là thiết lập kết nối ssh để họ có thể kết nối vào hệ thống của chúng ta đã.'
            )
            
            suggest = embed.embed_command()
            suggest.add_field(name='1. !ssh_connection', value='Establish SSH connection', inline=False)
            suggest.add_field(name='2. !help', value='display all commands', inline=False)
            
            await ctx.send(embed = embed.embed_story(message))
            await asyncio.sleep(1)
            await ctx.send(embed = suggest)
      
  
# Task 1:      
class ftp_request(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.deny = 'Permission denied \U0001F92A'
    
    @command(name='cfg_firewall', description='configure firewall')
    @dm_only()
    async def cfg_firewall(self, ctx):
        id = ctx.message.author.id
        user.dic_user[id].ftp_process = 1
        
        if user.dic_user[id].ftp == False:
            await ctx.send(
                embed = embed.embed_error(self.deny),
                delete_after = 5
            )
            return
        
        message = (
            f'Cho những bạn chưa biêt, firewall là tập hợp những rules mà chúng ta định nghĩa sao cho phù hợp với hệ thống mà chúng ta thiết lập firewall. Những rules này sẽ được dùng để giám sát, điều khiển network traffic (cả incoming và outcoming).\n\n'
            f'Để thực hiện configure firewall deny FTp requests, bạn sẽ cần dùng lệnh: '
        ) 
        suggest = embed.Embed(title='$config iptables --deny port 21', color=0x3498db)
        await ctx.send(embed = embed.embed_story(message))
        await ctx.send(embed = suggest)
        
    
    @Cog.listener()
    @dm_only()
    async def on_message(self, message):
        id = message.author.id
        channel = message.channel
        
        if message.author == self.bot.user or message.content.startswith('!'):
            return
        
        if '$config iptables --deny port 21' in message.content.strip():
            user.dic_user[id].ftp_process = 2
            suggest = embed.Embed(title='$iptables --list_rule', color=0x3498db)
            await channel.send('Configuring firewall --------------')
            await asyncio.sleep(2)
            await channel.send('Done!!!')
            await asyncio.sleep(1)
            await channel.send('```Tốt rồi, kiểm tra lại xem rule mới đã được áp dụng cho firewall chưa đã !!!```', embed=suggest)
            
        elif '$iptables --list_rule' in message.content.strip():
            if user.dic_user[id].ftp_process != 2:
                await channel.send(
                    embed = embed.embed_error(self.deny),
                    delete_after = 5
                )
                return
            user.dic_user[id].ftp_process = 3
            message = (
                f'Này {message.author.name}, bạn block hộ tôi cái network IP này cái 178.76.9.0, chúng ta vừa tìm ra được một nhóm bot net có network address như này.\n\n' 
                f'Mau mau nhé, không sếp trừ lương. Đang giục kia kìa.'
            )
            suggest = embed.Embed(title='$config blacklist -ip IP_address', description='replace IP_address with IP address you want to block.', color=0x3498db)
            await channel.send('Done!!!')
            await channel.send('''```Port 20: Anable\nPort 21: Disable\nPort 80: Disable\n...```''')
            await asyncio.sleep(3)
            await channel.send('```Chờ đã, bạn có 1 tin nhắn từ đồng nghiệp:```') 
            await channel.send(embed = embed.embed_story(message))
            await asyncio.sleep(1)
            await channel.send(embed = suggest)

        elif '$config blacklist -ip 178.76.9.0' in message.content.strip():
            if user.dic_user[id].ftp_process != 3:
                await channel.send(
                    embed = embed.embed_story(self.deny),
                    delete_after = 5
                )
                return
            user.dic_user[id].ftp = True
            message = (
                f'Chắc Antoine đang cay lắm đấy \U0001F923, tuy nhiên hắn sẽ sớm có động thái mới thôi.\n\n'
                f'Gấp rút lên, thời gian không chừa một ai. Antoine cũng vậy (chắc thế).'
            )
            suggest = embed.embed_command()
            suggest.add_field(name = '1. !list_tasks', value = 'list all tasks', inline = False)
            suggest.add_field(name = '2. !stages', value = 'all stages you need to walk through as a blue team member', inline = False)
            suggest.add_field(name = '3. !help', value = 'display all commands', inline = False)
            await channel.send('Done!!!')
            await asyncio.sleep(1)
            await channel.send(embed = embed.embed_final('deny FTP request'))
            await channel.send('Good job boy!!!')
            await asyncio.sleep(1)
            await channel.send(embed = embed.embed_story(message))
            await channel.send(embed = suggest)
            
        elif '$' in message.content and message.channel is message.author.dm_channel:
            await channel.send(embed = embed.embed_error('Please enter a proper command as the instruction!!!'))
            return
  
  
# Task 2:      
class penatration(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.deny = 'Permission denied \U0001F618'
        
    
    @command(name='disconnect', description='disconnect the penatrated server from other hosts')
    @dm_only()
    async def disconnect(self, ctx):
        id = ctx.message.author.id
        if user.dic_user[id].pen == False:
            await ctx.send(
                embed = embed.embed_error(self.deny),
                delete_after = 5
            )
            return
        user.dic_user[id].pen_process['disconnect'] = True
        
        suggest = embed.embed_command()
        suggest.add_field(name='1. !backup', value='obtain backup files for the injured server', inline=False)
        suggest.add_field(name='2. !roll_back', value='rolls back all sessions', inline=False)
        suggest.add_field(name='3. !restore', value='restore the whole system to previous daily backups', inline=False)
        suggest.add_field(name='4. !help', value='display all commands', inline=False)
        
        await ctx.send('Isolating your server --------------')
        await asyncio.sleep(3)
        await ctx.send('Done!!!')
        await asyncio.sleep(1)
        await ctx.send('''```Other servers: Disconnected\nAll clients: Disconneced\nNetworks: Disconnected\nInternets: Disconnected```''')
        await asyncio.sleep(1)
        await ctx.send('```Tiếp theo bạn cần phải back up hệ thống hiện tại, rolls back toàn bộ sessions, và khôi phục lại hệ thống ban đầu từ bản back up thường nhật gần nhất.```', embed = suggest)
        
    @command(name='backup', description='obtain backup files for the injured server')
    @dm_only()
    async def backup(self, ctx):
        id = ctx.message.author.id
        if user.dic_user[id].pen == False or user.dic_user[id].pen_process['disconnect'] == False:
            await ctx.send(
                embed = embed.embed_error(self.deny),
                delete_after = 5
            )
            return
        
        else:
            user.dic_user[id].pen_process['backup'] = True
            await ctx.send('Performing backup process --------------')
            await asyncio.sleep(3)
            await ctx.send('Done!!!')
            await asyncio.sleep(1)
            await ctx.send('```Một bản backup đã được ghi lại để phục vụ mục đích điều tra về sau```')
        if user.dic_user[id].pen_process['roll_back'] == True and user.dic_user[id].pen_process['restore'] == True:
            message = (
                f'Ok. hệ thống của tổ chức đã hoạt động bình thường rồi.\n\n'
                f'Tuy nhiên, bạn có tò mò muốn biết những gì malware đã gây ra cho hệ thống cũng như độ nghiêm trọng của nó không ?\n\n'
                f'Nào, chúng ta đi điều tra cái backup  đã tạo khi nãy nhé.'
            )
            suggest = embed.embed_command()
            suggest.add_field(name='1. !research', value='research for more information of that malware', inline=False)
            suggest.add_field(name='2. !trace_net_flow', value='trace to the network flow', inline=False)
            suggest.add_field(name='3. !help', value='display all commands', inline=False)
            await asyncio.sleep(1)
            await ctx.send(embed = embed.embed_story(message))
            await asyncio.sleep(1)
            await ctx.send(embed = suggest)
            
        
    @command(name='roll_back', description='rolls back all sessions')
    @dm_only()
    async def roll_back(self, ctx):
        id = ctx.message.author.id
        if user.dic_user[id].pen == False or user.dic_user[id].pen_process['disconnect'] == False:
            await ctx.send(
                embed = embed.embed_error(self.deny),
                delete_after = 5
            )
            return
        else:
            user.dic_user[id].pen_process['roll_back'] = True
            await ctx.send('Rolling back --------------')
            await asyncio.sleep(3)
            await ctx.send('Done!!!')
            await asyncio.sleep(1)
            await ctx.send('```Đã roll back lại các sessions.```')
        if user.dic_user[id].pen_process['backup'] == True and user.dic_user[id].pen_process['restore'] == True:
            message = (
                f'Ok. hệ thống của tổ chức đã hoạt động bình thường rồi.\n\n'
                f'Tuy nhiên, bạn có tò mò muốn biết những gì malware đã gây ra cho hệ thống cũng như độ nghiêm trọng của nó không ?\n\n'
                f'Nào, chúng ta đi điều tra cái backup  đã tạo khi nãy nhé.'
            )
            suggest = embed.embed_command()
            suggest.add_field(name='1. !research', value='research for more information of that malware', inline=False)
            suggest.add_field(name='2. !trace_net_flow', value='trace to the network flow', inline=False)
            suggest.add_field(name='3. !help', value='display all commands', inline=False)
            await asyncio.sleep(1)
            await ctx.send(embed = embed.embed_story(message))
            await asyncio.sleep(1)
            await ctx.send(embed = suggest)
                
    @command(name='restore', description='restore the whole system to previous daily backups')
    @dm_only()
    async def restore(self, ctx):
        id = ctx.message.author.id
        if user.dic_user[id].pen == False or user.dic_user[id].pen_process['disconnect'] == False:
            await ctx.send(
                embed = embed.embed_error(self.deny),
                delete_after = 5
            )
            return
        else:
            user.dic_user[id].pen_process['restore'] = True
            await ctx.send('Restoring this morning backup data--------------')
            await asyncio.sleep(3)
            await ctx.send('Done!!!')
            await asyncio.sleep(1)
            await ctx.send('```Đã khôi phục lại hệ thống bằng bản backup thường nhật gần nhất.```')
        if user.dic_user[id].pen_process['backup'] == True and user.dic_user[id].pen_process['roll_back'] == True:
            message = (
                f'Ok. hệ thống của tổ chức đã hoạt động bình thường rồi.\n\n'
                f'Tuy nhiên, bạn có tò mò muốn biết những gì malware đã gây ra cho hệ thống cũng như độ nghiêm trọng của nó không ?\n\n'
                f'Nào, chúng ta đi điều tra cái backup  đã tạo khi nãy nhé.'
            )
            suggest = embed.embed_command()
            suggest.add_field(name='1. !research', value='research for more information of that malware', inline=False)
            suggest.add_field(name='2. !trace_net_flow', value='trace to the network flow', inline=False)
            suggest.add_field(name='3. !help', value='display all commands', inline=False)
            await asyncio.sleep(1)
            await ctx.send(embed = embed.embed_story(message))
            await asyncio.sleep(1)
            await ctx.send(embed = suggest)
            
    @command(name='research', description='research for more information of that malware')
    @dm_only()
    async def research(self, ctx):
        id = ctx.message.author.id
        if user.dic_user[id].pen == False or user.dic_user[id].pen_process['disconnect'] == False or user.dic_user[id].pen_process['backup'] == False or user.dic_user[id].pen_process['restore'] == False or user.dic_user[id].pen_process['roll_back'] == False:
            await ctx.send(
                embed = embed.embed_error(self.deny),
                delete_after = 5
            )
            return
        user.dic_user[id].pen = True
        user.dic_user[id].pen_process['research'] = True
        await ctx.send('```Ồ có khá nhiều bàn viết về cái loại malware này này.```')
        await asyncio.sleep(1)
        await ctx.send('```Vừa dài vừa khó đọc.```')
        await asyncio.sleep(2)
        await ctx.send('...')
        await asyncio.sleep(1)
        await ctx.send(embed = embed.embed_final('Restore the System from Penetration'))
        if user.dic_user[id].pen_process['netflow'] == False:
            suggest = embed.Embed(title='!trace_net_flow', color=0x3498db)
            await asyncio.sleep(1)
            await ctx.send('```Bạn có thể thử điều tra cả net flow nữa nhé.```', embed = suggest)
        else: 
            message = (
                f'Hehe\n\n'
                f'Ta vừa chống trả 2 cuộc tấn công đến từ Antoine, không biết hắn có còn động thái gì nữa không.'
                f'À đúng rồi, chuyên viên đến rồi đó, ta cần thiết lập kết nối cho người ta nữa chứ.\n\n'
                f'Ngoài ra còn phải viết cả báo cáo cho ngày hôm nay.'
            )
            suggest = embed.embed_command()
            suggest = embed.embed_command()
            suggest.add_field(name = '1. !list_tasks', value = 'list all tasks', inline = False)
            suggest.add_field(name = '2. !stages', value = 'all stages you need to walk through as a blue team member', inline = False)
            suggest.add_field(name = '3. !help', value = 'display all commands', inline = False)
            await asyncio.sleep(1)
            await ctx.send(embed = embed.embed_story(message))
            await asyncio.sleep(1)
            await ctx.send(embed = suggest)
        
    
    @command(name='trace_net_flow', description='trace to the network flow')
    @dm_only()
    async def trace_net_flow(self, ctx):
        id = ctx.message.author.id
        if user.dic_user[id].pen == False or user.dic_user[id].pen_process['disconnect'] == False or user.dic_user[id].pen_process['backup'] == False or user.dic_user[id].pen_process['restore'] == False or user.dic_user[id].pen_process['roll_back'] == False:
            await ctx.send(
                embed = embed.embed_error(self.deny),
                delete_after = 5
            )
            return
        user.dic_user[id].pen = True
        user.dic_user[id].pen_process['netflow'] = True
        await ctx.send('```Có một lượng lớn thông tin bạn có thể thu thập được khi điều tra net flow.```')
        await asyncio.sleep(1)
        await ctx.send('```Bạn có thể lấy được địa chỉ IP, gói tin, host đã gửi gói tin và nhiều dữ liệu quan trọng cho việc xác minh thủ phạm tán công vào hệ thống của tổ chức```')
        await ctx.send('...')
        await asyncio.sleep(2)
        await ctx.send(embed = embed.embed_final('Restore the System from Penetration'))
        if user.dic_user[id].pen_process['research'] == False:
            suggest = embed.Embed(title='!research', color=0x3498db)
            await asyncio.sleep(1)
            await ctx.send('```Bạn có thể thử nghiên cứu về con malware nữa nhé.```', embed = suggest)  
        else: 
            message = (
                f'Hehe\n\n'
                f'Ta vừa chống trả 2 cuộc tấn công đến từ Antoine, không biết hắn có còn động thái gì nữa không.'
                f'À đúng rồi, chuyên viên đến rồi đó, ta cần thiết lập kết nối cho người ta nữa chứ.\n\n'
                f'Ngoài ra còn phải viết cả báo cáo cho ngày hôm nay'
            )
            suggest = embed.embed_command()
            suggest = embed.embed_command()
            suggest.add_field(name = '1. !list_tasks', value = 'list all tasks', inline = False)
            suggest.add_field(name = '2. !stages', value = 'all stages you need to walk through as a blue team member', inline = False)
            suggest.add_field(name = '3. !help', value = 'display all commands', inline = False)
            await asyncio.sleep(1)
            await ctx.send(embed = embed.embed_story(message))
            await asyncio.sleep(1)
            await ctx.send(embed = suggest)
        
     
  
# Task 3:  
class report_event(Cog):
    
    def __init__(self,bot):
        self.bot = bot
        self.deny = 'Permission denied \U0001F608'
        
    
    @command(name='check_system', description='perform checking for the whole system')
    @dm_only()
    async def check_system(self, ctx):
        id = ctx.message.author.id
        if user.dic_user[id].rep == False:
            await ctx.send(
                embed = embed.embed_error(self.deny),
                delete_after = 5
            )
            return
        user.dic_user[id].rep_process['check'] = True
        
        suggest = embed.embed_command()
        suggest.add_field(name='1. !Snort', value='Introduction to Snort', inline=False)
        suggest.add_field(name='2. !Kibana', value='Introduction to Kibana', inline=False)
        suggest.add_field(name='3. !help', value='display all commands', inline=False)
        await ctx.send(f'```Để hỗ trợ cho nhiệm vụ này, ta cần một số tools chuyên dụng.```')
        await asyncio.sleep(2)
        await ctx.send(f'```Có rất nhiều tools hữu ích giúp chúng ta thu thập, tổ chức và phần tích events và logs của hệ thống```')
        await asyncio.sleep(2)
        await ctx.send(f'```Hôm nay bạn sẽ làm việc với Snort và Kibana```')
        await asyncio.sleep(1)
        await ctx.send(embed = suggest)
    
    @command(name='Snort', description='Introduction to Snort')
    @dm_only()
    async def Snort(self, ctx):
        id = ctx.message.author.id
        if user.dic_user[id].rep == False or user.dic_user[id].rep_process['check'] == False:
            await ctx.send(
                embed = embed.embed_error(self.deny),
                delete_after = 5
            )
            return
        user.dic_user[id].rep_process['snort'] = True
        snort = embed.Embed(title='Snort', description='Snort is an Intrusion Detection System. It can be used to record all events happened to our network.', url='https://www.elastic.co/kibana/', color=0x3498db)
        snort.set_author(name=ctx.author.name, icon_url=ctx.author.avatar, url='https://www.facebook.com/profile.php?id=100013598988296')
        snort.set_thumbnail(url='https://raw.githubusercontent.com/FPTU-Ethical-Hackers-Club/FPTU-Ethical-Hackers-Club.github.io/main/assets/img/avatar.png')
        snort.set_image(url='https://i.ytimg.com/vi/eDbNVSVoVQM/maxresdefault.jpg')
        await ctx.send(embed=snort)
        await asyncio.sleep(2)
        if user.dic_user[id].rep_process['kibana'] ==  False:
            await ctx.send('Ok, then', embed = embed.Embed(title='!Kibana', color=0x3498db))
        else:
            await ctx.send(f'```Snort ghi lại toàn bộ events, Kibana hỗ trợ sắp xếp, tổ chức dữ liệu cho bản báo cáo.```') 
            
            await ctx.send('```Vậy là đủ để làm báo cáo. Triển thôi```', embed = embed.Embed(title='!record_all_events', color=0x3498db))
        
    @command(name='Kibana', description='Introduction to Kibana')
    @dm_only()
    async def Kibana(self, ctx):
        id = ctx.message.author.id
        if user.dic_user[id].rep == False or user.dic_user[id].rep_process['check'] == False:
            await ctx.send(
                embed = embed.embed_error(self.deny),
                delete_after = 5
            )
            return
        user.dic_user[id].rep_process['kibana'] = True
        kibana = embed.Embed(title='Kibana', description='Kibana is free and open user interface that lets you visualize your data', url='https://www.snort.org/')
        kibana.set_author(name=ctx.author.name, icon_url=ctx.author.avatar, url='https://www.facebook.com/profile.php?id=100013598988296')
        kibana.set_thumbnail(url='https://raw.githubusercontent.com/FPTU-Ethical-Hackers-Club/FPTU-Ethical-Hackers-Club.github.io/main/assets/img/avatar.png')
        kibana.set_image(url='https://cdn.vidyard.com/thumbnails/NRw1o2Di0n-Qv6jIqRClhQ/3d34812ca9b4791aefe8f1.jpg')
        await ctx.send(embed=kibana)
        await asyncio.sleep(1)
        if user.dic_user[id].rep_process['snort'] ==  False:
            await ctx.send('Ok, then', embed = embed.Embed(title='!Snort', color=0x3498db))
        else:
            await ctx.send(f'```Snort ghi lại toàn bộ events, Kibana hỗ trợ sắp xếp, tổ chức dữ liệu cho bản báo cáo.```') 
            
            await ctx.send(f'```Vậy là đủ để làm báo cáo. Triển thôi```', embed = embed.Embed(title='!record_all_events', color=0x3498db))
            
    @command(name='record_all_events', description='Record all events and write a report to your manager.')
    @dm_only()
    async def record_all_events(self, ctx):
        id = ctx.message.author.id
        if user.dic_user[id].rep == False or user.dic_user[id].rep_process['check'] == False or user.dic_user[id].rep_process['kibana'] == False or user.dic_user[id].rep_process['snort'] == False:
            await ctx.send(
                embed = embed.embed_error(self.deny),
                delete_after = 5
            )
            return
        else:
            user.dic_user[id].rep = True
            user.dic_user[id].rep_process['report'] = True
            
            message = (
                f'Bản báo cáo này sẽ rất có giá trị đó.\n\n'
                f'Nó sẽ được dùng trong nhiều việc như:\n'
                f'+) Đánh giá thiệt hại cho công ty.\n'
                f'+) Phân tích và giải quyết nhanh tình huống chúng ta gặp cùng sự cố trong tương lai.\n'
                f'+) Publish lên website của tổ chức nhằm thu thập thêm hướng giải quyết tối ưu từ nhiều nguồn.\n'
                f'+) ...\n\n'
                f'Tiếp theo chúng ta làm gì nhỉ? \U0001F615'
            )
            
            story = embed.embed_story(message)
            story.set_image(url = 'https://japana.vn/uploads/detail/2018/07/images/11(7).jpg')
            suggest = embed.embed_command()
            suggest = embed.embed_command()
            suggest.add_field(name = '1. !list_tasks', value = 'list all tasks', inline = False)
            suggest.add_field(name = '2. !stages', value = 'all stages you need to walk through as a blue team member', inline = False)
            suggest.add_field(name = '3. !help', value = 'display all commands', inline = False)
            
            await ctx.send('Collecting data -------------')
            await asyncio.sleep(2)
            await ctx.send('Organizing data -------------')
            await asyncio.sleep(2)
            await ctx.send('Writing report --------------')
            await asyncio.sleep(2)
            await ctx.send('Sending the report to your manager -------------')
            await asyncio.sleep(2)
            await ctx.send('Done!!!')
            await ctx.send(embed = embed.embed_final('Report events'))
            await asyncio.sleep(3)
            await ctx.send(embed = story)
            await ctx.send(embed = suggest)
            

class ssh_connection(Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.deny = 'Permission denied \U0001F643'
        
        
    @command(name='ssh_connection', description='Establish SSH connection')
    @dm_only()
    async def ssh_connection(self, ctx):
        id = ctx.message.author.id
        if user.dic_user[id].ssh == False:
            await ctx.send(
                embed = embed.embed_error(self.deny),
                delete_after = 5
            )
            return
        
        user.dic_user[id].ssh_process['ssh'] = True
        await ctx.send('Connecting to server -----------------')
        await asyncio.sleep(2)
        
        if user.dic_user[id].ssh_process['whitelist'] == False:
            await ctx.send('```Whitelist là một danh sách những users đặc biệt được cấp quyền truy cập vào hệ thống của tổ chức.```')
            await asyncio.sleep(2)
            await ctx.send('```Chúng ta cần phải add account của các chuyên gia vào whitelist để họ có thể dễ dàng truy cập được vào hệ thống.```')
            await asyncio.sleep(1)
            await ctx.send(embed = embed.Embed(title='!cfg_whitelist', color=0x3498db))
        
        elif user.dic_user[id].ssh_process['acl'] == False:
            message = (
                f'ACL (Access Control List) là danh sách những đặc quyền (read, write, hoặc execute) liên kết tới tài nguyên của hệ thống.'
                f'ACL xác định một nhóm user cố định (được configured) hoặc các tiến trình cố định được cấp quyền hướng tới tài nguyên của hệt thống.'
            )
            await ctx.send('```ACL (Access Control List) là danh sách những đặc quyền (read, write, hoặc execute) liên kết tới tài nguyên của hệ thống.```')
            await asyncio.sleep(2)
            await ctx.send('```ACL xác định một nhóm user cố định (được configured) hoặc các tiến trình cố định được cấp quyền hướng tới tài nguyên của hệt thống.```')
            await asyncio.sleep(1)
            await ctx.send('```Vì vài điều khoản của công ty, chúng ta chỉ cấp quyền cho họ vào một số tài nguyên thôi```', embed = embed.Embed(title='!cfg_acl', color=0x3498db))
        
        else:
            message1 = (
                f'Yay, rảnh tay hơn rồi.\n\n'
                f'Giao việc còn lại cho các chuyên gia thôi.\n\n'
            )
            message2 = (
                f'Ồ có vẻ họ xác định được vị trí của Antoine rồi.\n\n'
                f'Quả này hắn nguy to \U0001F60F'
            )
            
            suggest = embed.embed_command()
            suggest = embed.embed_command()
            suggest.add_field(name = '1. !stages', value = 'all stages you need to walk through as a blue team member', inline = False)
            suggest.add_field(name = '2. !help', value = 'display all commands', inline = False)
            
            await ctx.send('Done!!!')
            await asyncio.sleep(1)
            await ctx.send(embed = embed.embed_final('establish SSH connection'))
            await asyncio.sleep(2)
            await ctx.send(embed = embed.embed_story(message1))
            await asyncio.sleep(2)
            await ctx.send(embed = embed.embed_story(message2))
            await ctx.send(embed = suggest)
            user.dic_user[id].ssh = True
        
        
    @command(name='cfg_whitelist', description='Configure the whitelist')
    @dm_only()
    async def cfg_whitelist(self, ctx):
        id = ctx.message.author.id
        if user.dic_user[id].ssh == False or user.dic_user[id].ssh_process['ssh'] == False:
            await ctx.send(
                embed = embed.embed_error(self.deny),
                delete_after = 5
            )
            return
        user.dic_user[id].ssh_process['whitelist'] = True
        await ctx.send('Adding that user to the whitelist ------------')
        await asyncio.sleep(2)
        await ctx.send('Done!!!')
        await asyncio.sleep(1)
        await ctx.send('Ok, try establishing ssh connection again...')
        
    
    @command(name='cfg_acl', description='Configure the Access Control List')
    @dm_only()
    async def cfg_acl(self, ctx):
        id = ctx.message.author.id
        if user.dic_user[id].ssh == False or user.dic_user[id].ssh_process['ssh'] == False:
            await ctx.send(
                embed = embed.embed_error(self.deny),
                delete_after = 5
            )
            return
        user.dic_user[id].ssh_process['acl'] = True
        await ctx.send('Configuring Access Control List ------------')
        await asyncio.sleep(2)
        await ctx.send('Done!!!')
        await asyncio.sleep(1)
        await ctx.send('Ok, try establishing ssh connection again...')

        
def setup(bot):
    bot.add_cog(incident_response(bot))
    bot.add_cog(ftp_request(bot))
    bot.add_cog(penatration(bot))
    bot.add_cog(report_event(bot))
    bot.add_cog(ssh_connection(bot))