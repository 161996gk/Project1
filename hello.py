a=raw_input("enter your name")
a=len(a)
for i in range(a):
    for j in range(i):
        if j%2==0:
            print "*",
        else:
            print "#",
    print "\n"