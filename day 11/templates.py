import os

FILE_PATH=os.path.abspath(__file__)
BASE_DIR=os.path.dirname(FILE_PATH)
TEMPLATE_DIR=os.path.join(BASE_DIR,"templates")

class Template:
    temlate_name=""
    context=None

    def __init__(self,temlate_name="",context=None,*args,**kwargs):
        self.temlate_name=temlate_name
        self.context=context

    def get_template(self):
        temlate_path=os.path.join(TEMPLATE_DIR,self.temlate_name)
        if not os.path.exists(temlate_path):
            raise Exception("this path dose not exists")
        temlate_string=""
        with open(temlate_path,'r') as f:
            temlate_string=f.read()
        return temlate_string

    def render(self,context=None):
        render_ctx=context
        if self.context !=None:
            render_ctx=self.context
        if not isinstance(render_ctx,dict):
            render_ctx={}
        temlate_string=self.get_template()        
        return temlate_string.format(**render_ctx) #{"name":"abi"} ->name="abi"
