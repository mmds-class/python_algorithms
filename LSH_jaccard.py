'''
Created on Oct 8, 2014

@author: derek farren
'''
import math

class HashFunc(object):
    '''universal hash function object'''
    
    #constructor that sets the number of buckets and the input dimension of the hash function
    def __init__(self): 
        pass
    
    #to evaluate the hash function
    def __call__(self):
        pass

    #to check if a number is prime (could be useful)    
    def is_prime(self, num):
        for j in range(2,int(math.sqrt(num)+1)):
            if (num % j) == 0:
                return False
        return True

            
class LSH(object):
    
    def __init__(self, nbr_of_bands, rows_per_band, nbr_documents):
        pass
    
    def classify_doc(self, doc_id, signature_lst):
        pass                  
    
    
def minhash(doc_shingles_dct, all_shingles_dct, hash_func_lst):
    doc_signature_dct = {}
    return doc_signature_dct

    
def load_shingles(file_location, k):
    shingles_dct = {}
    offset_lst = []
    return shingles_dct, offset_lst


def load_doc(file_location, offset):
    with open(file_location) as f:
        f.seek(offset)
        line = f.readline()
    idx = line.find(' ')
    return line[idx+1:]