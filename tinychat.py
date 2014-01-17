#Tinychat spy plugin for JtRippers IRC bot framework written by di0de.
#Link to bot can be found here https://github.com/jtRIPper/plugin-based-irc-bot
#Capable of listing users in a tinychat room.
#No error handling, use at own risk
# coding: utf-8
import sys
import urllib2 
from xml.dom import minidom

class tinychat:
  def __init__(self, bot):
#Handler for the bot class (so the plugin can send messages)
    self.bot = bot
 
#Functions that users are allowed to call and their authentication level (in this case 1)
    self.allowed_functions = { 'users':1, 'help':1 }
 
#This function can be called with tinychat.users to the bot.
  def users(self, buffer):
#Listen for commands in buffer.
        args = buffer.msg.split()
        if len(args) == 2:
            rm = (args[1])
            self.bot.msg(buffer.to,"-" * 60)
            self.bot.msg(buffer.to,"Please wait, Gathering data on chat room %s " % rm)
            self.bot.msg(buffer.to, "-" * 60) 
		    #Grab xml from the tinychat api of the room
            xml_string = urllib2.urlopen("http://api.tinychat.com/%s.xml" % rm).read()
 
            xml_feed = minidom.parseString(xml_string)
            names = xml_feed.getElementsByTagName("names")
            #Look for the names tag and display all names in irc
            for name in names:
                 namez = name.firstChild.nodeValue
                 self.bot.msg(buffer.to, namez)

# the help function, this is required by all plugins.
def help(self, buffer):
    self.bot.msg(buffer.to, "Usage: ")
    self.bot.msg(buffer.to, " *tinychat.users <Name of chat room>")