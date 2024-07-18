msg = str(input("Message: "))
shift = int(input("Shift number: "))

msg_arr = []
enc_msg = []

for i in range(len(msg)):
    msg_arr.append(msg[i])
    
    if ord(msg_arr[i]) in range(65,91): #uppercase letters
        normal = ord(msg_arr[i]) - 65
        shifted = (normal + shift ) % 26 + 65
        enc_msg.append(chr(shifted))
    
    elif ord(msg_arr[i]) in range(97,123): #lowecase letters
            normal = ord(msg_arr[i]) - 97
            shifted = (normal + shift ) % 26 + 97
            enc_msg.append(chr(shifted))        
      
    if ord(msg_arr[i]) == 32: # space
        enc_msg.append(msg_arr[i])
        
for i in range(len(enc_msg)):
    print(enc_msg[i], end="")
print("")
