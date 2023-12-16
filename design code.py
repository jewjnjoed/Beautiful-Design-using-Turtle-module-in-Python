import turtle as t #importing turtle module
t.speed(0)  #providing speed to cursor
t.bgcolor("black")   #black background
t.pencolor("purple")
for i in range(2020):
    t.rt(i)
    t.circle(120,i)
    t.fd(i)
    t.rt(90)
t.done()
print()
