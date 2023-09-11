encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
msg_ltrs = [x for x in encrypted_message]
i = 1
len = len(msg_ltrs)
while (i < (len//2)):
    slot1 = msg_ltrs[i]
    slot2 = msg_ltrs[len-i-1]
    msg_ltrs[i] = slot2
    msg_ltrs[len-i-1] = slot1
    i += 2

answer = "".join(msg_ltrs)
print(answer)