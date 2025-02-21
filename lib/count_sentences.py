#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value

  def is_sentence(self):
    if (self.value.endswith(".")):
      return True
    else:
      return False
    
  def is_question(self):
    if (self.value.endswith("?")):
      return True
    else:
      return False
  
  def is_exclamation(self):
    if (self.value.endswith("!")):
      return True
    else:
      return False
    
  def count_sentences(self):
    if (type(self.value) != str):
      print("The value must be a string.")
      return
    else:
      self.value = self.value.replace("!!", "!").replace("??", "!").replace("...", "!")
      sentences = self.value.replace("?", "!").replace(".", "!").split('!')
      sentences = [s.strip() for s in sentences if s.strip()]
      # sentences = self.value.split('!', self.value)
      return len(sentences)
    # words_list = (self.value.split("[.!?]"))
  


