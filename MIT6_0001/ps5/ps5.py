# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate

        


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError
    

# PHRASE TRIGGERS

#Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def is_phrase_in(self, text):
        """
        Returns True if self.phrase is present in text,
        otherwise returns False.
        """

        #Get rid of caps
        text = text.lower()

        #Get rid of punctuation
        for i in string.punctuation:
            text = text.replace(i,' ')

        #Get rid of spacing
        text = ' '+' '.join(text.split())+' '

        #Add spaces to avoid phrase being part of longer word
        phrase = ' '+self.phrase.lower()+' '

        if phrase in text:
            return True
        
        return False

        

# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        """
        Returns True if self.phrase is present in text,
        otherwise returns False.
        """
        if self.is_phrase_in(story.get_title()):
            return True

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        """
        Returns True if self.phrase is present in text,
        otherwise returns False.
        """
        if self.is_phrase_in(story.get_description()):
            return True


# TIME TRIGGERS

# Problem 5

class TimeTrigger(Trigger):
    def __init__(self, time):
        self.time = datetime.strptime(time, "%d %b %Y %H:%M:%S")


# Problem 6

class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        if story.get_pubdate() < self.time:
            return True

class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        if story.get_pubdate() > self.time:
            return True


# COMPOSITE TRIGGERS

# Problem 7

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        if not self.trigger.evaluate(story):
            return True

# Problem 8

class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        if self.trigger1.evaluate(story) and self.trigger2.evaluate(story):
            return True


# Problem 9

class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        AndTrigger.__init__(self, trigger1, trigger2)

    def evaluate(self, story):
        if self.trigger1.evaluate(story) or self.trigger2.evaluate(story):
            return True



#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    
    list = []

    for story in stories:
        for trigger in triggerlist:
                if trigger.evaluate(story):
                    list.append(story)

    return list

#======================
# User-Specified Triggers
#======================
# Problem 11

def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """

    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    triggers = {}
    triggerlist = []

    for line in lines:
        line = line.split(',')

        if line[0] != 'ADD':

                if line[1] == 'TITLE':
                    triggers[line[0]] = TitleTrigger(line[2])

                elif line[1] == 'DESCRIPTION':
                    triggers[line[0]] = DescriptionTrigger(line[2])

                elif line[1] == 'AFTER':
                    triggers[line[0]] = AfterTrigger(line[2])

                elif line[1] == 'BEFORE':
                    triggers[line[0]] = BeforeTrigger(line[2])

                elif line[1] == 'NOT':
                    triggers[line[0]] = NotTrigger(line[2])

                elif line[1] == 'AND':
                    triggers[line[0]] = AndTrigger(triggers.get(line[2]),triggers.get(line[3]))

                elif line[1] == 'OR':
                    triggers[line[0]] = OrTrigger(triggers.get(line[2]),triggers.get(line[3]))

        else:
            for i in line[1:]:
                triggerlist.append(triggers.get(i))
    
    return triggerlist

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        # Problem 11
        triggerlist = read_trigger_config('ps5/triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

