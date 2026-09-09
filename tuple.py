#create a tuple(immutable sequence)
log_entry = ("192.168.1.1" , 80)
#access elements by index
print(log_entry[0])

#tuples are immutable - this below will cause an error
# uncomment to see the error press(ctrl & /)
# log_entry[0] = "10.0.0.1"

#checking tuple legth (len)
print ("tuple length",len(log_entry))