import string

def alphabet_position(text):
    num=''
    for j in list(text):
        if j.isupper():
            index= str(string.ascii_uppercase.index(j)+1)
            num=str(num+index+" ")
        elif j.islower():
            index= str(string.ascii_lowercase.index(j)+1)
            num=str(num+index+" ")
        else:
            pass
    return (str(num).strip(" "))


def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


alphabet_position("The sunset sets at twelve o' clock.")
