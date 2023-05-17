import os # 导入 os模块

def main():
    clearFlag = "y"
    while(1):
        if clearFlag == "y" or clearFlag == "Y":
            os.system("cls") # 执行cls命令清屏命令行
        clearFlag = ""
        string = input("请输入需要转换的字符串 :")
        type = input("请选择操作类型(1：加密 2：解密 3:二次加密) :")
        while(type != "1" and type != "2" and type != "3"):
            type = input("操作类型输入错误，请重新选择(1：加密 2：解密 3：二次加密) :")
        if type == "1" :
            encode_string = encode(string) # encode_string=编码
            print("编码结果为："+encode_string+"")
        if type == "2" :
            decode_string = decode(string)
            print("解码结果为："+decode_string+"【请注意前后空格】")
        if type == "3" :
            trencode_string = trencode(string) # encode_string=编码
            print("编码结果为："+trencode_string+"")
        clearFlag = input("按Y/y清空屏幕继续:")
#编码
def encode(string):
    encode_string = ""
    for char in string:
        encode_char = hex(ord(char)).replace("0x","%") #先转ASCII编码再转16进制，把0x替换为%
        # 例如 i+=1 == i=i+1;所以 encode_string = encode_string + encode_char
        encode_string += encode_char # encode_string += 空字符+结果
    return encode_string

#解码
def decode(string):
    decode_string = ""
    # 以%为分隔符
    # %61%6e%64
    # ['%61','%6e','%64']
    #string_arr.pop(0)删除第一个元素
    # ['61','6e','64']
    string_arr = string.split("%") # 以%为分隔符
    string_arr.pop(0)           #删除第一个元素
    for char in string_arr:
        decode_char = chr(eval("0x"+char)) # chr(eval("0x"+ 61.....))，先输出0x61再通过chr转换为ASCII编码
        decode_string += decode_char
    return decode_string

#二次编码
def trencode(string):
    trencode_string = ""
    for char in string:
        trencode_char = hex(ord(char)).replace("0x","%25") #先转ASCII编码再转16进制，把0x替换为%
        # 例如 i+=1 == i=i+1;所以 encode_string = encode_string + encode_char
        trencode_string += trencode_char # encode_string += 空字符+结果
    return trencode_string

main()