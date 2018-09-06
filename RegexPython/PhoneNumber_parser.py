#Parser tool to show regex vs functions


#Parsing through a function

#creating a function to find phone numbers in text

#test cases
text_a = 'Here is a number 415-555-4242 is a phone number:'
text_b =  'Moshi moshi is a phone number:'
text_c = "@sorin: uhm, that doesn't exactly 415-766-4242 matter, does it? If I compare against (2,6,4) the 'final' doesn't seem to affect the comparison and it isn't supposed to. Apparently no slicing is needed when I compare the most significant parts of the tuple. This seems to be how it's treated and that's what my question was about. I'm not saying this solution doesn't have its merit, I'm just wondering why its the best - i.e. what I am missin"

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdigit():
            return False
    #hyphen check        
    if text[3] != '-':
        return False
    #period check
    #if text[3] != '.':
        #return False
    for i in range(4,7):
        if not text[i].isdigit():
            return False
    #hyphen check        
    if text[7] != '-':
        return False
    #period check
    #if text[7] != '.':
        #return False
    for i in range(8,12):
        if not text[i].isdigit():
            return False
    print('End')
    return True
 
 
        
    
message = text_c

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found ' + chunk)
print('Done')
  
    

    
    
#calling our functions    
#isPhoneNumber(text_a)
#isPhoneNumber(text_b)
#isPhoneNumber(text_c)