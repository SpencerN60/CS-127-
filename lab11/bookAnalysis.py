
        
        
    
    
    



f = open('nobodySaw.txt', 'r')
newStory = ""
def analyzeBook(book):
    newStory = ""
    count = {}
    for line in book:
        for word in line.split():
            newWord = word.replace('-','').replace('"', '').replace(',', '').replace('.', '').replace('-', '').replace('?', '').replace('!', '').replace("'", "").replace('(', '').replace(')', '').replace(':', '').replace('[', '').replace(']', '').replace(';', '')
            newStory = newStory + " " +  newWord
        newStory = newStory + "\n"
    newWords = newStory.split()
    x = 1
    for i in newWords:
        count[i] = x
        if i.isalpha():
            x += 1
        else:
            x += 0
    return count
    
    
    
def outputAnalysis(dict):
    keys = list(dict.keys())
    keys.sort()
    sorted = {i : dict[i] for i in keys}
    return sorted

def main():
    with open('nobodySaw.txt', 'r') as f:
        newBook = analyzeBook(f)
        sorted = outputAnalysis(newBook)
        print(sorted)
        keysSorted = sorted.keys()
    with open('nobodySawWords.txt', 'w') as out:
        for word in keysSorted:
            out.write(word + " " + str(newBook[word]))
            out.write('\n')

main()
    

        
        
        
        



        
            

        

    