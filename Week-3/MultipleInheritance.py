class Father:
  def gardening(self):
    print("I enjoy gardening")

class Mother:
  def cooking(self):
    print("I love cooking")

class child(Father,Mother):
  def sports(self):
    print("I love sports")


c=child()

c.gardening()
c.cooking()
c.sports()