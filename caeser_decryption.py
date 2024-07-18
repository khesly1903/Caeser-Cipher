msg = str(input("Message: "))

for i in range(0,26):
    msg_arr = []
    dec_msg = []
    
    for j in range(len(msg)):
        msg_arr.append(msg[j])
        
        if ord(msg_arr[j]) in range(65,91): #uppercase letters
            normal = ord(msg_arr[j]) - 65
            shifted = (normal + i ) % 26 + 65
            dec_msg.append(chr(shifted))
        
        elif ord(msg_arr[j]) in range(97,123): #lowecase letters
            normal = ord(msg_arr[j]) - 97
            shifted = (normal + i ) % 26 + 97
            dec_msg.append(chr(shifted))     
            
        if ord(msg_arr[j]) == 32: #space
            dec_msg.append(msg_arr[j])

    
    for i in range(len(dec_msg)):
        print(dec_msg[i], end = "")
    print("")
        
    
