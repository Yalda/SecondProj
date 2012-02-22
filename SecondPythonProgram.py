import inputdata
import numpy
import pdb; pdb.set_trace()

data = inputdata.raw_scores


def main():
  newElements = elements()


class elements(object):
  ''' I am all elements needed for recommendation :) ''' 
  def __init__(self):
    self.people = []
    self.papers = []
    

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

    
    self.ratings = numpy.zeros([len(self.people),len(self.papers)])
    '''fill ratings'''
    for person in self.people:
      for paper in self.papers:
        ''' find match in dictionary '''
	for personInData,readPapers in data.iteritems():
	  for paperInData,rate in readPapers.iteritems():
	    if person == personInData and paper == paperInData:
	      i = self.people.index(person)
              j = self.papers.index(paper)
		
	      self.ratings[i][j] = rate

    print self.ratings


    ''' I'm finding similarity between each 2 people '''
    self.similarity = numpy.zeros([len(self.people),len(self.people)])
    i = 0
    j = 0
    for row in self.ratings:
      for row in self.ratings:
        vector = abs(ratings[i] - ratings[j])
        j +=1
      i += 1
        
        
      index +=1
     
      

main()

  

