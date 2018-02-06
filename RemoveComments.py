##This Is A Small Program To Remove Comments From Python Programs.
##We've All Done It. When A Program Is Overly Commented And We Need To Remove The Comments.
##This Can Run As A Stand Alone For A One Shot Fix Or Be Called By Another Program.
##If Calling From Another Program: Removal(**File Path Of Original**, **File Path Of Modified**).
##If Running Alone: Uncomment The Last 3 Lines.

##Writen By Lynton Brown 02/06/2018.

def Removal(originalFile, modifiedFile): ##Definition Takes 2 Files (Input And Output).
    charToStartRemoval = '#' ##Character To Search For.
    with open(originalFile, 'r') as inputFile, open(modifiedFile, 'w') as outputFile: ##Open Original File As ReadOnly And Create New File To Write.
        temp = inputFile.readlines() ##Hold Orignal File In Variable 'temp'.
        for x in temp: ##Go Through 'temp' Character By Character.
            x = x.split("#")[0] ##Remove '#' And Only Keep Cahracters That Came Before '#' Was Found. Disregard The Rest.
            outputFile.write(x) ##Write 'x' To The New File
            print x ##Print for Debuging
    print "Finished Processing" ##Notify When File Is Complete
            
##originalFile = '' #Enter File Path Of File To Be Modified
##modifiedFile = '' #Enter File Path Of New File Location            
##Removal(originalFile, modifiedFile) ##Call Function 

