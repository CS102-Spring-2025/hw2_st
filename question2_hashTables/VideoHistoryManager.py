from VideoHistoryHashTable import *

#Takes in list of Dictionaries in format[{},{}] 
# Returns HashTable in the Format [{'ID':..,"DATA":{}}]
def create_VideoHistory(VideoRecords):
    size=7
    pass
    
        
    
    
#Takes as input the Hashtable and Name of Operation file 
# Returns a Tuple with two items 
#   1. collision Path in the format {1:[],2:[]} where the keys are the Operation number
#   2. Final HashTable After All Operations performed.
def perform_Operations(H,operationFile):

    pass

            

            
#Takes the File name is input 
# Returns the list of Dictionaries to be converted to a hashtable in format [{},{}...]
def main(filename):
    pass
    

# Driver Code
VideoRecords=main('watchedVideos.csv')
print(VideoRecords)
H=create_VideoHistory(VideoRecords)
print(H)
print(perform_Operations(H,'Operations1.csv'))