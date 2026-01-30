def foo(a, b, *c):
    return len(c)

def bar(a, b, **kwargs):
    return kwargs["magicnumber"] == 7

if foo(1, 2, 3) == 1:
    print("Good")
if foo(1, 2, 3) == 2:
    print("Better")
if bar(1, 2, magicnumber=6) == False:
    print("Great")
if bar(1, 2, magicnumber=7) == True:
    print("Awesome")


