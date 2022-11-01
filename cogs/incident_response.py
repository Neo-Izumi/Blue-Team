from email.mime import image
import nextcord
import discord_components.dropdown
from nextcord import slash_command, Interaction, Embed
from nextcord.ext.commands import Cog, command


class incident_response(Cog): 
    
    def __init__(self, bot):
        self.bot = bot
        
    ID = 1035593393381838888
    
    @slash_command(name='list_tasks', description='list all tasks you need to do', guild_ids=[ID])
    async def list_tasks(self, interaction: Interaction):
        tasks = discord_components.dropdown.list_tasks_view()
        await interaction.response.send_message('Here are all your tasks', view = tasks)
      
  
# Task 1:      
class fpt_request(Cog):
    def __init__(self, bot):
        self.bot = bot
        
    ID = 1035593393381838888
    process = 0
    
    @slash_command(name='cfg_firewall', description='configure firewall', guild_ids=[ID])
    async def cfg_firewall(self, interaction: Interaction):
        message = 'Firewall is a list of rules that can be used to mornitor the incoming/outcoming network traffic, block/permit data packets, ...\nTo block all ftp request, you need to type $config iptables --deny port 21'
        await interaction.response.send_message(message, ephemeral=False)
    
    @Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if '$config iptables --deny port 21' in message.content:
            channel = message.channel
            self.process += 1
            await channel.send('Configuring firewall --------------')
            await channel.send('Done!!!')
            await channel.send('Let\'s check our firewall again... type $iptables --list_rule')
    #     else:
    #         return
            
    # @Cog.listener()
    # async def on_message(self, message):
    #     if message.author == self.bot.user:
    #         return
        elif '$iptables --list_rule' in message.content:
            channel = message.channel
            self.process += 1
            await channel.send('Done!!!')
            await channel.send('Port 20: Anable\nPort 20: Disable\nPort 80: Disable\n...')
            await channel.send('Wait... a message from other partners:\n\'Hey, we\'ve just detected that the strange group of IP address come from network address: 178.76.9.0\nCan you please block this network address?\'') 
            await channel.send('Ok. So, to block an ipaddress, type $config blacklist -ip yourip')
    #     else: 
    #         return
            
    # @Cog.listener()
    # async def on_message(self, message):
    #     if message.author == self.bot.user:
    #         return
        elif '$config blacklist -ip 178.76.9.0' in message.content:
            channel = message.channel
            self.process += 1
            await channel.send('Done!!!')
            await channel.send('Good job boy!!!')
        else:
            return
  
  
# Task 2:      
class penatration(Cog):
    def __init__(self, bot):
        self.bot = bot
        
    ID = 1035593393381838888
    process = 0  
    
    @slash_command(name='disconnect', description='disconnect the injured server from other hosts', guild_ids=[ID])
    async def disconnect(self, interaction: Interaction):
        self.process += 1
        await interaction.response.send_message('Isolating your server --------------')
        await interaction.followup.send('Done!!!')
        await interaction.followup.send('Other servers: Disconnected\nAll clients: Disconneced\nNetworks: Disconnected')
        await interaction.followup.send('Next, you need to backup your system, trace back all sessions and restore the previous stage\nType \'/\' to see suggestion')
        
    @slash_command(name='backup', description='obtain backup files for the injured server', guild_ids=[ID])
    async def backup(self, interaction: Interaction):
        if self.process == 0: 
            await interaction.response.send_message('Permission denied :))')
            return
        else:
            self.process += 1
            await interaction.response.send_message('Performing backup process --------------')
            await interaction.followup.send('Done!!!')
        if self.process >= 4:
            await interaction.followup.send('Ok. Your server is now running normally.\nAre you curious to know what did the malware do to your server?\nLet\'s investigate the backup files')
        
    @slash_command(name='trace_back', description='trace back all sessions', guild_ids=[ID])
    async def trace_back(self, interaction: Interaction):
        if self.process == 0: 
            await interaction.response.send_message('Permission denied :))')
            return
        else:
            self.process += 1
            await interaction.response.send_message('Tracing back --------------')
            await interaction.followup.send('Done!!!')
        if self.process >= 4:
            await interaction.followup.send('Ok. Your server is now running normally.\nAre you curious to know what did the malware do to your server?\nLet\'s investigate the backup files')
            
    @slash_command(name='restore', description='trace back all sessions', guild_ids=[ID])
    async def restore(self, interaction: Interaction):
        if self.process == 0: 
            await interaction.response.send_message('Permission denied :))')
            return
        else:
            self.process += 1
            await interaction.response.send_message('Tracing back --------------')
            await interaction.followup.send('Done!!!')
        if self.process >= 4:
            await interaction.followup.send('Ok. Your server is now running normally.\nAre you curious to know what did the malware do to your server?\nLet\'s investigate the backup files')
            await interaction.followup.send('type /research or /trace_net_flow for more information')
            
    @slash_command(name='research', description='research for more information of that malware', guild_ids=[ID])
    async def research(self, interaction: Interaction):
        if self.process < 4: 
            await interaction.response.send_message('Permission denied :))')
            return
        await interaction.response.send_message('There is a new research for this malware and it will take a lot of time to fully understand.')
        await interaction.followup.send('Hurray!!! You\'ve done this task. \nHowever, if you want to see more, don\'t mind to try trace_net_flow.')
        self.process = 10
        
    
    @slash_command(name='trace_net_flow', description='research for more information of that malware', guild_ids=[ID])
    async def trace_net_flow(self, interaction: Interaction):
        if self.process < 4: 
            await interaction.response.send_message('Permission denied :))')
            return
        if self.process == 0: 
            await interaction.response.send_message('Permission denied :))')
            return
        await interaction.response.send_message('There is a huge amount of information you can get from this malware if you trace to network flow (such as: host, ip address, data packets, ...)')
        await interaction.followup.send('Hurray!!! You\'ve done this task. \nHowever, if you want to see more, don\'t mind to try trace_net_flow.')
        self.process = 10    
     
  
# Task 3:  
class report_event(Cog):
    
    def __init__(self,bot):
        self.bot = bot
        
    ID = 1035593393381838888
    process = 0
    
    @slash_command(name='check_system', description='perform checking for the whole system', guild_ids=[ID])
    async def check_system(self, interaction: Interaction):
        self.process = 1
        await interaction.response.send_message('There are so many helpless tools')
        await interaction.followup.send('Oh sorry, I missed spell. There are so many helpfull tools that can help you in collecting, organizing, analysing alerts, events and logs from your organization system.')
        await interaction.followup.send('Some of those that you can try now are Snort and Kibana. For details, please type \'!\' followed by tool name')
    
    @command(name='Snort', description='Introduction to Snort')
    async def Snort(self, ctx):
        self.process += 1
        snort = Embed(title='Snort', description='Snort is an Intrusion Detection System. It can be used to record all events happened to our network.', url='https://www.elastic.co/kibana/')
        snort.set_image(url='https://i.ytimg.com/vi/eDbNVSVoVQM/maxresdefault.jpg')
        await ctx.send(embed=snort)
        if self.process >= 3: 
            await ctx.send('After using these tools, you should try /record_all_events')
        
    @command(name='Kibana', description='Introduction to Kibana')
    async def Kibana(self, ctx):
        self.process += 1
        kibana = Embed(title='Kibana', description='Kibana is free and open user interface that lets you visualize your data', url='https://www.snort.org/')
        kibana.set_image(url='https://cdn.vidyard.com/thumbnails/NRw1o2Di0n-Qv6jIqRClhQ/3d34812ca9b4791aefe8f1.jpg')
        await ctx.send(embed=kibana)
        if self.process >= 3: 
            await ctx.send('After using these tools, you should try /record_all_events')
            
    @slash_command(name='record_all_events', description='Record all events and write a report to your manager.', guild_ids=[ID])
    async def record_all_events(self, interaction: Interaction):
        if self.process < 3:
            await interaction.response.send_message('Permission denied :))')
        else:
            self.process = 10
            await interaction.response.send_message('Collecting data -------------')
            await interaction.followup.send('Organizing data -------------')
            await interaction.followup.send('Writing report --------------')
            await interaction.followup.send('Sending the report to your manager -------------')
            await interaction.followup.send('Done!!!')

        
def setup(bot):
    bot.add_cog(incident_response(bot))
    bot.add_cog(fpt_request(bot))
    bot.add_cog(penatration(bot))
    bot.add_cog(report_event(bot))