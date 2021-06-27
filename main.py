from tkinter import*
from PIL import ImageTk, Image

global questions_answers
names_list = []


questions_answers = {
 1: ["Who is the youngest player to score 10,000 points in the NBA", 'Kobe Bryant','Michael Jordan','Steph Curry','LeBron James', '21',4],
 2: ["What is Usain Bolt's world record time?", '10.03','9.21','9.43','9.58', '9.58',4],
 3: ["The olympic are held every how many years?", '5 Years', '2 Years', '3 Years', '4 Years', '4 Years',4],
 4: ["In the NFL how much points are a touchdown worth?", '5 points', '7 points', '8 points', '6 points', '6 points',4],
 5: ["What team holds the longest winning streak in NBA history?", 'Chicago Bulls', 'Milwaukee Bucks', 'Dallas Mavericks', 'Los Angeles Lakers',  'Los Angeles Lakers',4],
 6: ["How many rings are there on an olympic flag?", '6', '7', '3', '5', '5',4],
 7: ["Who is the president of the UFC?", 'Joe Rogan', 'Jon Jones', 'Michael Bisping', 'Dana White', 'Dana White',4]

}

def randomiser():
  global qnum
  qnum = random.randint(1,7)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()

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
 
randomiser
if __name__ == "__main__":
  root = Tk()
  root.title("Sports")
  quizStarter_object = QuizStarter(root)
  root.mainloop()