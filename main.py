from tkinter import*
from PIL import ImageTk, Image

class QuizStarter:
  def __init__(self, parent):
    background_color="Yellow" 
    #frame set up
    self.quiz_frame = Frame(parent, bg = background_color, padx=10, pady=10)
    self.quiz_frame.grid()

    #Label widget for heading
    self.heading_label = Label (self.quiz_frame, text = "SPORTS", font=("Helvetica", "30", "bold"), bg=background_color)
    self.heading_label.grid(row=0)
  
    #Start button
    self.start_button = Button (self.quiz_frame, text = "START", bg="steelblue")
    self.start_button.grid(row=2) 
   
   #Exit button
    self.exit_button = Button (self.quiz_frame, text = "EXIT", bg="Red")
    self.exit_button.grid(row=3)

    #Picture 
    self.picture_image = Image.open("Sports.jpeg")
    self.picture_image = self.picture_image.resize((500, 200), Image.ANTIALIAS)
    self.picture_image = ImageTk.PhotoImage(self.picture_image)

    self.image_label= Label(self.quiz_frame, image=self.picture_image)
    self.image_label.grid(row=1)
    



#************Starting point program************#
if __name__ == "__main__":
  root = Tk()
  root.title("Sports")
  quizStarter_object = QuizStarter(root)
  root.mainloop()