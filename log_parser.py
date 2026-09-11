#loads regex module
import re

#log is the variable, Error message is string
log = "Error from 192.168.1.1"

# Variable "match" stores log, re.search searches through log, r means raw string, the string contains a regex pattern, "\." means literal period, d+ means one or more digits
# The search result is the ip itself
# log is telling Python where to search
# So re.search(r"pattern, where to search)
match = re.search(r"\d+\.\d+\.\d+\.\d+", log)

#Tells python if you found something and stored it in match run the code below
if match: 

    # "IP:" Is just a lable for the output 
    # match.group() pulls the text that regex found "192.168.1.1"
    print ("IP:", match.group())











