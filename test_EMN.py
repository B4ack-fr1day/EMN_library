from os import system

try:
    from EMN import _funny
except ModuleNotFoundError:
    system("pip install EMN==0.0.0")
    
print(_funny.create_banner(text="hi"))
