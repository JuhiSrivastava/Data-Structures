#Python3
#week -1 - assign1
inputStr = input()
ipStrLen = len(inputStr)
li =[['0',0]]
j = 0
for i in range(ipStrLen):
    if inputStr[i] == "[" or inputStr[i] == "(" or inputStr[i] == "{":
        li.append([inputStr[i],i])
        j = j+1
    elif (inputStr[i] == "]" and li[j][0] == "[") or (inputStr[i] == ")" and li[j][0] == "(") or (inputStr[i] == "}" and li[j][0] == "{"):
        del li[j]
        j = j-1
    elif inputStr[i] == "]" or inputStr[i] == ")" or inputStr[i] == "}":
        li.append([inputStr[i],i])
        j = j+1
        break
if len(li) == 1:
    print("Success")
else:
    print(li[j][1] +1)
        
    
    
        

