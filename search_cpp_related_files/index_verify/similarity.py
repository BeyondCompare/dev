#coding = 'utf8'
from collections import namedtuple
import math

QueryDocInfo = namedtuple('QueryDocInfo', ['nDocFreq', 'nDocCount', 'nDocTerms','nFreq','nAvgTerms'])

class CTFIDFSimilarity: 
  def getSimilarity(self,queryDocInfo):
    idf_value = self.idf(queryDocInfo.nDocFreq,queryDocInfo.nDocCount);
    if idf_value < 0:
      idf_value = 0.00001
    tf_value = self.tf(queryDocInfo.nFreq);
    norm_value = self.norm(queryDocInfo.nDocTerms);
    #boost_value = self.boost(queryDocInfo.iField)
    return idf_value * idf_value * tf_value * norm_value * boost_value;
  
  def boost(self,ifield):
    if iField ==  NAME: 
      return 1.0
    if iField == CATEGOTY:
      return 1.2
    if iField == TAG:
      return 1.5
    return 0.5
    
  def tf(self,nFreq):
    return math.sqrt(nFreq)

  def idf(self,nDocFreq,nDocCount):
    return 1 + math.log(float(nDocCount) / (nDocFreq + 1))

  def norm(self,nTerms):
    return 1 / math.sqrt(nTerms + 1.0)


class CBM25Similarity:
  def __init__(self):
    self.k = 1.2;
    self.b = 0.75;

  def getSimilarity(self,queryDocInfo):
    idf_value = self.idf(queryDocInfo.nDocFreq,queryDocInfo.nDocCount)
    if idf_value < 0:
      idf_value = 0.00001
    norm_value = self.norm(queryDocInfo.nDocTerms,queryDocInfo.nAvgTerms)
    query_factor = queryDocInfo.nFreq * (self.k + 1) / (queryDocInfo.nFreq + self.k * (1 - self.b + self.b * norm_value))    
    return idf_value * query_factor

  def idf(self,nDocFreq,nDocCount):
    return math.log((nDocCount - nDocFreq + 0.5) / (nDocFreq + 0.5))

  def norm(self,nDocTerms,nAvgTerms):
    return  float(nDocTerms) / (1 + nAvgTerms)

  def boost(self,ifield):
    if ifield ==  NAME: 
      return 1.0
    if ifield == CATEGOTY:
      return 1.5
    if ifield == TAG:
      return 1.8
    return 0.5

tfidfSimilarity = CTFIDFSimilarity()
bm25Similarity = CBM25Similarity()
