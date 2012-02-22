import inputdata
import numpy
import scipy.stats
#import pdb; pdb.set_trace()

data = inputdata.raw_scores


def main():
  newElements = elements()
  print newElements.ratings
  print newElements.similarities
  print newElements.pearsonCorr

class elements(object):
  #I am all elements needed for recommendation :) 
  def __init__(self):
    self.people = []
    self.papers = []
    

    #fill people[]
    for person,ratings in data.iteritems():
      self.people.append(person)

    #fill papers[]
    for person,readPapers in data.iteritems():
      for paper,rate in readPapers.iteritems():
        newPaper = True       
        for item in self.papers: 
          if item == paper:
	    newPaper = False
        if newPaper:
          self.papers.append(paper)

    
    #fill ratings
    self.ratings = numpy.zeros([len(self.people),len(self.papers)])
    for person in self.people:
      for paper in self.papers:
        #find match in dictionary
	for personInData,readPapers in data.iteritems():
	  for paperInData,rate in readPapers.iteritems():
	    if person == personInData and paper == paperInData:
	      i = self.people.index(person)
              j = self.papers.index(paper)
		
	      self.ratings[i][j] = rate


    #fill similarity norms and pearson correlation
    self.similarities = numpy.zeros([len(self.people),len(self.people)])    
    self.pearsonCorr = numpy.zeros([len(self.people),len(self.people)])    
    i=0
    for person in self.people:
      j=0
      for preson in self.people:
        self.similarities[i][j] = self.norm_finder(self.ratings[i],self.ratings[j])
	self.pearsonCorr[i][j] = self.pearson_finder(self.ratings[i],self.ratings[j])
	j+= 1
      i+= 1

  #------------------------- norm --------------------------------------------------  
  def norm_finder(self,v1,v2):
    return numpy.linalg.norm(v1-v2)

  #------------------------- pearson correlation------------------------------------  
  def pearson_finder(self,v1,v2):
    return scipy.stats.pearsonr(v1,v2)
      

main()

  

