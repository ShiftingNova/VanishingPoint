#
# Jordan Walker
# CSC10
# Main runs a while loop for the graphics. 
#There is a second while loop for the blades of grass.
#
from graphics import graphics
def main():
    gui = graphics(500,500, "Vashiing Point")
    #i=50
    while i<True:

        y = gui.mouse_y
        x = gui.mouse_x
        gui.text(0,100,"Text ="+str(y),"black",20)
        gui.rectangle(0,200,500,500,'green')
        gui.rectangle(0, 0, 500, 250, 'light blue')
        gui.ellipse(450,100,50,50,"yellow")
        gui.triangle(250,50-y,400,250,100,250,"brown")
        u = 0
        e = 0
        while u < 100000:
            gui.rectangle(e, 240, 2, 10, "darkgreen")
            u += 1
            e += (10+y/100)
        gui.ellipse(250,300+y/25,150+y/2,50+y/50,"blue")
        gui.rectangle(400+y/15,300,50+y/10,150+y,"brown")
        gui.ellipse(425+y/15,250+y/25,100+y/10,150+y/2,"dark green")
        gui.rectangle(50-y/15, 300, 50+y/10, 150+y, "brown")
        gui.ellipse(75-y/15, 250+y/25, 100+y/10, 150+y/2, "dark green")

        gui.update_frame(60)
        i+=1
    gui.primary.mainloop()
main()
