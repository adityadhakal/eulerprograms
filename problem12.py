# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\adit__000\.spyder2\.temp.py
"""

def factors(n): #find the number of factors of number supplied
    print "Factorizing: ",n
    #we only use first 4 prime numbers
    var = 1
    while var == 1:
    #variables for loop condition
        var2 = 1
        var3 = 1
        var5 = 1
        var7 = 1
        
        factors = 0
    #counting the factors
        count2 = 0
        count3 = 0
        count5 = 0
        count7 = 0
        
        divided = n
        
        #factoring with 2
        while var2 == 1:
            if divided%2 == 0:
                count2 = count2+1
                divided = divided/2
            else:
                var2 = 2
        
        #factoring with 3
        while var3 == 1:
            if divided%3 == 0:
                count3 = count3+1
                divided =  divided/3
            else:
                var3 = 2
        
        #factoring with 5
        while var5 == 1:
            if divided%5 ==0:
                count5 = count5+1
                divided = divided/7
            else:
                var5 = 2
        
        #factoring with 7
        while var7 ==1:
            if divided%7 == 0:
                count7 = count7+1
                divided = divided/7
            else:
                var7 = 2
                
        #summing up total factors
        
        factors = (count2+1)*(count3+1)*(count5+1)*(count7+1)
        
        print "/n Number of factors", factors
        
        if factors >500:
            var = 2
            
                