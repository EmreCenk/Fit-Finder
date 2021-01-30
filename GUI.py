
import tkinter as tk
from gradient import GradientFrame

font_name="Segoe UI"
class page_displayer:

    def __init__(self):
        global font_name
        # self.BACKGROUND_COLOR = "#add8e6" #The background color
        self.HEIGHT = 500 #This is the initial window size, everything will be resized if you change the size of the
        # window
        self.WIDTH = 800

        self.root = tk.Tk()  # Initializing root
        self.root.title("Something")  # setting window title name
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry(f'{width}x{height}')
        #initializing background:


        self.screen = tk.Canvas(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.screen.pack()


        self.main_frame = GradientFrame(self.root, from_color= "#088BFE", to_color= "#058F06", height=1000)

        # Placing the background:
        self.main_frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor="n")

        # PLACE HOLDER VALUES:
        self.root.bind("<Configure>", self.on_resize)

        self.list_of_objects = []  # we will store a list of objects so that we can delete things on the screen
        self.list_of_attributes_to_resize=[]
        self.list_of_text_objects=[]

        self.screen_index=0
        self.screen_order = [self.welcome_screen,
                        self.question1]

    def clear_text(self):
        for text in self.list_of_text_objects:
            self.main_frame.delete(text)
        self.list_of_text_objects=[]
    def create_proper_text(self,relx,rely,text,fill,font_tuple):
        x=relx*self.WIDTH
        y=rely*self.HEIGHT
        params=[x,y,text,fill,font_tuple]
        created=self.main_frame.create_text(x,y,text=text,fill=fill,font=font_tuple)
        self.list_of_text_objects.append(created)
        self.list_of_attributes_to_resize.append([x,y,text,fill,font_tuple])
    def on_resize(self, event_object):

        updated=[]
        updated_text_objects=[]
        for text in self.list_of_attributes_to_resize:
            x=text[0]
            y=text[1]
            written = text[2]
            filling = text[3]
            font = text[4]
            font_size=int(font[1])
            newx= (x/self.WIDTH) * event_object.width
            newy= (y/self.HEIGHT) * event_object.height

            new_font=(font_name,int((font_size/(x*y))*(newx*newy)))
            new_formed=self.main_frame.create_text(newx,newy,text=written,fill=filling,font=new_font)
            updated_text_objects.append(new_formed)
            updated.append([newx,newy,written,filling,new_font])

        for text in self.list_of_text_objects:
            self.main_frame.delete(text)

        self.list_of_attributes_to_resize=updated
        self.list_of_text_objects=updated_text_objects
        self.WIDTH=event_object.width
        self.HEIGHT=event_object.height
    def clear_page(self ):
        # This function deletes every object on the page. It will be used when transitioning between pages.
        for object in self.list_of_objects:
            object.destroy()

        self.list_of_objects = []  # Just to make sure everything is fully wiped from memory

    def click_anywhere(self):
        self.create_proper_text(0.5,0.8,"Click anywhere to continue","white",(font_name,8))

    def question1(self):
        self.clear_page()
        self.clear_text()
        self.create_proper_text(relx=0.5,rely=0.5,text="Yaaa",fill="White",font_tuple=(font_name,20))
    def mouse_clicked(self,even_object):
        self.screen_order[self.screen_index]()


    def welcome_screen(self,):
        self.screen_index+=1
        self.create_proper_text(0.5,0.5,"Welcome to Fit Finder","white",(font_name,25))
        self.create_proper_text(0.5,0.4,"Hello.","White",(font_name,25))
        self.click_anywhere()
        self.root.bind("<Button-1>", self.mouse_clicked)

from gradient import GradientFrame
self=page_displayer()
self.welcome_screen()
self.screen.mainloop()
