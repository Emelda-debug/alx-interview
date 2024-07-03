#!/usr/bin/python3
"""
method that determines if all the boxes can be opened
given there are n number of boxes where
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes
"""

def canUnlockAll(boxes):
        """ function to check if all the boxes can be opened"""
        if (type(boxes)) is not list:
                return False
        elif (len(boxes)) == 0:
                return False
        for x in range(1, len(boxes) - 1):
                box_check = False
                for index in range(len(boxes)):
                        box_check = x in boxes[index] and x != index
                        if box_check:
                                break
                if box_check is False:
                        return box_check
        return True
                        







        














        """ """

        
                
        
                
        
        
                
                
                        
                        
                                
                        
                                
                                                                      
