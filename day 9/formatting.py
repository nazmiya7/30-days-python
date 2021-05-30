msg_template="""hello {name},
thank you for joing{website}.we are happy 
with us.
""" # .format(name="abi",website='abz.ij')

def format_msg(my_name="abi",my_website="abz.ij"):
    my_msg=msg_template.format(name=my_name,website=my_website)
    return my_msg