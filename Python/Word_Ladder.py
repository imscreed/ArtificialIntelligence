__author__ = 'imscreed'
from heapq import heappush, heappop
from string import ascii_lowercase as chars


arg = float('inf')

def BFS_COMPUTATION(full_input, initial_Value, final_Value, PROGRAM_AI):

  ONE_LEVEL_ROOT, LIST_QUE = {}, [(PROGRAM_AI(initial_Value), None, initial_Value)]

  while LIST_QUE:
    distance, parent, element = heappop(LIST_QUE)

    if element in ONE_LEVEL_ROOT: continue
    ONE_LEVEL_ROOT[element] = parent

    if element == final_Value:
      return distance - PROGRAM_AI(final_Value), ONE_LEVEL_ROOT

    for neighbor in full_input[element]:
      weight = full_input[element][neighbor] - PROGRAM_AI(element) + PROGRAM_AI(neighbor)
      heappush(LIST_QUE, (distance + weight, element, neighbor))


  return arg, None


"""Change a word to a list and loop through each postiion and character"""
"""After checking make the word string and check whether it is a valid word"""

class Adjacency(object):

  def __init__(self, words):
    self.words = words
    self.adjacent_words = dict()

  def adjacency_looper(self, charac, words):
    WORD_LIST = list(charac)

    for i, j in enumerate(WORD_LIST):

      for x in chars:

        if j == x: continue
        WORD_LIST[i] = x
        FIXED = ''.join(WORD_LIST)

        if FIXED in words:
          yield FIXED

      WORD_LIST[i] = j


  def __getitem__(self, charc):

    """Determine the immediate neighbours, use looper to pass in the words and the number"""

    if charc not in self.adjacent_words:
      self.adjacent_words[charc] = dict.fromkeys(self.adjacency_looper(charc, self.words), 1)

    return self.adjacent_words[charc]


  def CHECK_SUM(self, iter1, iter2):

    return sum(val1!=val2 for val1, val2 in zip(iter1, iter2))


  def LADDER_AI(self, initial_value, final_value, h=None):
    if h is None:
      def h(word_arg):
        return self.CHECK_SUM(word_arg, final_value)

    _, word_traversal = BFS_COMPUTATION(self, initial_value, final_value, h)
    if word_traversal is None:
      return [initial_value, None, final_value]

    charac, list1 = final_value, []
    while charac is not None:
      list1.append(charac)
      charac = word_traversal[charac]

    """Traverse back"""
    list1.reverse()
    return list1


if __name__ == '__main__':
  x = set(line.strip().lower() for line in open("dictionary"))
  word_ladder = Adjacency(x)
  print word_ladder.LADDER_AI('dears', 'fears')
  print word_ladder.LADDER_AI('heart', 'heart')
  print word_ladder.LADDER_AI('monk', 'perl')
  print word_ladder.LADDER_AI('slow', 'fast')
  print word_ladder.LADDER_AI('blue', 'pink')
  print word_ladder.LADDER_AI('bluw', 'pink')
  print word_ladder.LADDER_AI('stone', 'money')
  print word_ladder.LADDER_AI('money', 'smart')
  print word_ladder.LADDER_AI('devil', 'angel')
  print word_ladder.LADDER_AI('atlas', 'zebra')
  print word_ladder.LADDER_AI('babes', 'child')
  print word_ladder.LADDER_AI('mumbo', 'ghost')
  print word_ladder.LADDER_AI('train', 'bikes')
  print word_ladder.LADDER_AI('babies', 'sleepy')
  print word_ladder.LADDER_AI('brewing', 'whiskey')