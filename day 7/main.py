def my_print(txt):
    print(txt)

    
msg_template="""hello {name},
thank you for joing{website}.we are happy 
with us.
""" # .format(name="abi",website='abz.ij')

def format_msg(my_name="abi",my_website="abz.ij"):
my_msg=msg_template.format(name=my_name,website=my_website)
# print(my_msg)
return my_msg

"""
"{} {}".format("abc",123)
"{1} {0}".format("abc",123)
"{name} {number}".format(name="abc",number=123)

"{} {name} {number}".format("another",name="abc",number=123)

"""


def base_function(*args,**kwargs):
    print(args,kwargs)
    
