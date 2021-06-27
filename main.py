from tkinter import*
from PIL import ImageTk, Image

names_list = []

class QuizStarter:
  def __init__(self, parent):
    background_color="Yellow"


    self.quiz_frame = Frame(parent, bg = background_color, padx=5, pady=5)
    self.quiz_frame.grid()

    #Label widget for heading
    self.heading_label = Label (self.quiz_frame, text = "SPORTS", font=("Helvetica", "30"), bg=background_color)
    self.heading_label.grid(row=0, padx=10, pady=10)
    
  
    #Start button
    self.start_button = Button (self.quiz_frame, text = "START", bg="steelblue", command=self.start)
    self.start_button.grid(row=2, padx=5, pady=5) 
   
   #Exit button
    self.exit_button = Button (self.quiz_frame, text = "EXIT", bg="red", command=self.quiz_frame.destroy)
    self.exit_button.grid(row=4, padx=5, pady=5)

    #Picture resize
    self.picture_image = Image.open("Sports.jpeg")
    self.picture_image = self.picture_image.resize((500, 200), Image.ANTIALIAS)
    self.picture_image = ImageTk.PhotoImage(self.picture_image)
    self.image_label= Label(self.quiz_frame, image=self.picture_image)
    self.image_label.grid(row=1, pady=5, padx=5)

    
  def start(self):
    self.quiz_frame.destroy()  
    NameEnter(root)


class NameEnter:
  def __init__(self, parent):
    background_color="Yellow"

    #Quiz Frame
    self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
    self.quiz_frame.grid()

    self.user_label = Label (self.quiz_frame, text = "Please enter your username", font=("Helvetica", "20"), bg=background_color)
    self.user_label.grid(row=0, padx=5, pady=5)
  
    #Name Enter
    self.entry_box=Entry(self.quiz_frame)
    self.entry_box.grid(row=1, pady=5, padx=5)

    self.continue_button = Button (self.quiz_frame, text = "CONTINUE", bg="steelblue", command=self.name_collection)
    self.continue_button.grid(row=4, pady=5, padx=5)

  def name_collection(self):
    name = self.entry_box.get()
    names_list.append(name)
    print(names_list)
    self.quiz_frame.destroy()
 

if __name__ == "__main__":
  root = Tk()
  root.title("Sports")
  quizStarter_object = QuizStarter(root)
  root.mainloop()