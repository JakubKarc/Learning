from math import *

# ----------------------------------------------------------------
# Inicializes the user input
def get_input():
  command = input(">> ").split()
  verb_word = command[0]

  if verb_word in verb_dict:
    verb = verb_dict[verb_word]
  else:
    print("Unknown verb {}".format(verb_word))
    return

  if len(command) >= 2:
    noun_word = command[1]
    print(verb(noun_word))
  else:
    print(verb("nothing"))

# -----------------------------------------------------------------
# Main game object
class GameObject:
  class_name = ""
  desc = ""
  objects = {}

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self

  def get_desc(self):
    return self.class_name + "\n" + self.desc

# ------------------------------------------------------------------
# Goblin class that inherits form "GameObjects"
class Goblin(GameObject):
  class_name = "goblin"
  desc = "A foul creature."

  def __init__(self, name):
    self.class_name = "goblin"
    self.health = 3
    self._desc = "A foul creature"
    super().__init__(name)

  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "It has a wound on its knee."
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
    self._desc = value

goblin = Goblin("Gobbly")

# Functions ---------------------------------------------------------

# Func for "say"
def say(noun):
  return 'You said "{}"'.format(noun)

# Func for "examine"
def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)

# Func for "hit"
def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed the {}!".format(thing.class_name)
      else:
        msg = "You hit the {}".format(thing.class_name)
  else:
    msg ="There is no {} here.".format(noun)
  return msg

# ------------------------------------------------------------------
# Main dictionary for commands
verb_dict = {
  "say": say,
  "examine": examine,
  "hit": hit,
}

# -------------------------------------------------------------------
# Runs the whole thing
while True:
  get_input()
