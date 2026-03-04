class Human:
  def __init__(self,name,occupation):
    self.name=name
    self.occupation=occupation

  def do_work(self):
    if self.occupation=="tennis":
      print(self.name,"Plays tennis")
    elif self.occupation=="actor":
      print(self.name,"Shoots a film")

  def speaks(self):
    print(self.name,"says how are you")


tom=Human("tome cruise","actor")
tom.do_work()
tom.speaks()