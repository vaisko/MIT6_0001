import string
import time
from datetime import datetime
import pytz


#text = 'What?!?!?!?   the@#FUCK is wrong with.this   programme the fucking audacity?!'
text = 'Purple!!! Cow!!!'

#Get rid of caps
text = text.lower()

#Get rid of punctuation
for i in string.punctuation:
    text = text.replace(i,' ')

#removes spacing
text = ' '.join(text.split())+' '

sample = 'the fuck'
sample = ' ' + sample + ' '

# if sample in text:
#             print(True)

# else:
#         print(False)

# new_text = ''

# for i in text.split():
#     new_text = new_text + i + ' '


# text_list = text.lower().split(' ')

# for i in text_list:

# for i in string.punctuation:
#     # new_text = text.lower().split(i)

#     new_text = new_text.replace(i,'')

# print(text)
# print(text_list)

time = '11 Apr 2023 23:47:59'
time2 = '15 Apr 2023'
time3 = '15 Apr 2023 23:48:59'

new_time = datetime.strptime(time, "%d %b %Y %H:%M:%S")
new_time2 = datetime.strptime(time2, "%d %b %Y %H:%M:%S")
new_time3 = datetime.strptime(time3, "%d %b %Y %H:%M:%S")

if new_time3 < new_time2:
    print(True)

else:
    print(False)