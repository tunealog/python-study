# Basic of Python

# Title : Quiz(Formating, Escape)
# Date : 2020-06-25
# Creator : tunealog


# Quiz) Create a program for creating a password
#
# Rule1 : Except "http://"
# Rule2 : Except to "." which first meets
# Rule3 : Construct to password that
#         the first three digits of the remaining letters
#         and number of letters
#         and number of "e" in letters
#         and "1"
# Example : http://github.com = git60!

def CreatePassWord(code):
    code = code.replace("http://", "")
    n = code.find(".")
    code = code[:n]
    pass1 = code[:3]
    pass2 = len(code)
    pass3 = code.count("e")
    pass4 = pass1+str(pass2)+str(pass3)+"!"

    print(f"PassWord is : {pass4} ")


# PassWord is : goo61!
CreatePassWord("http://google.com")

# PassWord is : ama60!
CreatePassWord("http://amazon.com")

# PassWord is : eba41!
CreatePassWord("http://ebay.com")

# PassWord is : you71!
CreatePassWord("http://youtube.com")
