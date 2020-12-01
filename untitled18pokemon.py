 # -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:28:49 2020

@author: User
"""
import re 


def pokemon_names(file_name):
    with open(file_name,'r') as z:
        the_names=re.findall('/w+',z.read())
    longest_series=[]
    currentseries=[]
        
    def letter_starts_with(lastletter,names):
        for index, name in enumerate(names):
            if name.startswith(lastletter):
                   return index
        
        return False
    
    
    for name in names:
        currentname=name
        currentseries.append(currentname)
        
        pokename=names[:]
        pokename.pop(pokename.index(currentname))
        
        index=letter_starts_with(currentname[-1],pokename) 
        
        
        while index is not False:
            currentname=pokename[index]
            currentseries.append(currentname)
            pokename.pop(index)
            index=letter_starts_with(currentname[-1],pokename)
            
            
        if len(currenseries)> len(longes_series):
            longest_series=currentseries
            
        currentseries=[]
    
if __name__ == "__main__":
    print(longest_series)
    print(pokemon_names('pokemon.txt'))
        
        
    
    
                
