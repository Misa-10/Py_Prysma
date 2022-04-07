x = "global "

def test():
 def foo():
     global x
     y = "local"
     x = x * 2
    
 foo()
 
 
def test2():
     print(x)
     
test()

test2()