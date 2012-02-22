import inputdata
import numpy

data = inputdata.raw_scores


def main():
  newElements = elements()


class elements(object):
  ''' I am all elements needed for recommendation :) ''' 
  def __init__(self):
    self.people = []
    self.papers = []
    self.ratings = [[]]

    ''' fill people[] '''
    for person,ratings in data.iteritems():
      self.people.append(person)

    ''' fill papers[] '''
    for person,readPapers in data.iteritems():
      for paper,rate in readPapers.iteritems():
        newPaper = True       
        for item in self.papers: 
          if item == paper:
	    newPaper = False
        if newPaper:
          self.papers.append(paper)

    '''fill ratings'''
    for person,readPapers in data.iteritems():
      for paper,rate in readPapers.iteritems():


    self.ratings[0].append(0)
    print self.ratings

    


main()

  

