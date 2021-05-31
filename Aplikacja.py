#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


from collections import namedtuple
from random import randint  
from itertools import combinations

class BreakIt(Exception): pass



#-----------------------------------------------FUNCTIONS----------------------------------------------------

#Function removing all off-alphabet chars from text
#INPUT 
    #text - string with off-alphabet chars
    #alphabet - string of acceptable chars
#OUTPUT
    #text - text without off-alphabet chars
def clear(text, alphabet):
    i= 0
    while i<len(text):
        if text[i] not in alphabet:
            text = text.replace(text[i], u'')
        else:
            i+=1
    return text

#Encryption - substitution cipher
#INPUT 
    #plaintext - string
    #key - string defining  permutation "<encrypted A>, <encrypted B>,...,<encrytped Z>"
    #alphabet - string defining set of used chars
#OUTPUT
    #ciphertext - string
def encrypt(plaintext, key, alphabet):
    ciphertext = ""
    c = [key[alphabet.index(l)] for l in plaintext]
    ciphertext = "".join(c)         
    return ciphertext

#Decryption - substitution cipher
#INPUT 
    #ciphertext - string
    #key - string defining  permutation "<encrypted A>, <encrypted B>,...,<encrytped Z>"
    #alphabet - string defining set of used chars
#OUTPUT
    #plaintext - string
def decrypt(ciphertext, key, alphabet):
    p = [alphabet[key.index(l)] for l in ciphertext]
    plaintext = "".join(p)    
    return plaintext

#Frequency counter
#INPUT 
    #text - string
    #alphabet - string defining set of used chars
#OUTPUT
    #frequency table - list of frequency letters [<frequency of A>,<frequancy of B>,..,<frequency of Z>]
def countFrequency(text, alphabet):
    frequency = []
    lenText = len(text)
    for a in alphabet:
        counter = 0
        for l in text:
            if l == a:
                counter+=1
        frequency.append((a,counter))      
    return sorted(frequency,key  = lambda x: x[1], reverse= True)

#Dictionary maker
#INPUT
   #file - with word from dictionary (class _io.TextIOWrapper)
   #alphabet - string
   #size - minimal length to join to dictionary (int)
#OUTPUT
   #D- dictionary type: dictionary
def makedictionary(file,alphabet,mini,maxi):
    #print("otrzymałem mini = %d , maxi = %d"%(mini,maxi))
    D = {}
    index = 0   
    for slowo in file:
        slowo = slowo.upper()        
        slowo = clear(slowo,alphabet)  
        if len(slowo) < mini or len(slowo) > maxi:
            continue
        #print("dodaje slowo o dluosci %d"%len(slowo))
        #slowo = slowo.rstrip()        
        #slowo = slowo.decode('windows-1250')              
        D.update({slowo:index})
        index+=1    
    return D



#Random key generator
#INPUT   
   #alphabet - string
#OUTPUT
   #key - random key 
def randKey(alphabet):
    l = len(alphabet)
    pula = alphabet
    key = ''
    for i in range(l):
        ind = randint(0,len(pula)-1)
        key = key + pula[ind]
        pula = pula.replace(pula[ind],"")
    return key

#Difference calculator 
#INPUT   
   #pattern - string
   #argument - string to compare
#OUTPUT
   #diffference - number of wrong letter
def diffCalc(pattern, argument):
    if len(pattern) != len(argument):
        raise Exception("Wrong number of letter. Comparing impossible")
    counter = 0
    for i in range(len(pattern)):
        if argument[i] != pattern[i]:
            counter += 1
    return counter

#Frequency digram counter
#INPUT 
    #text - string
    #alphabet - string defining set of used chars
#OUTPUT
    #frequency table - list of digrams frequency  [<frequency of TB>,<frequancy of DC>,..,<frequency of GF>]
def countDigramFrequency(text):
    frequency = []
    used =  []
    lenText = len(text)
    for i in range(lenText-1):
        pattern = text[i]+text[i+1]
        if pattern in used:
            continue
        else:
            used.append(pattern)
        counter = 0
        for j in range(i,lenText-1):            
            if text[j] == pattern[0] and text[j+1] == pattern[1]:
                counter+=1
        if counter > 4:
            frequency.append((pattern,counter))
    frequency = sorted(frequency, key = lambda x: x[1], reverse= True)
    return frequency

#Frequency trigram counter
#INPUT 
    #text - string
    #alphabet - string defining set of used chars
#OUTPUT
    #frequency table - list of trigrams frequency  [<frequency of TBF>,<frequancy of DCG>,..,<frequency of GFE>]
def countTrigramFrequency(text):
    frequency = []
    used =  []
    lenText = len(text)
    for i in range(lenText-2):
        pattern = text[i]+text[i+1]+text[i+2]
        if pattern in used:
            continue
        else:
            used.append(pattern)
        counter = 0        
        for j in range(i,lenText-2):            
            if text[j] == pattern[0] and text[j+1] == pattern[1] and text[j+2] == pattern[2]:
                counter+=1
        if counter > 3:
            frequency.append((pattern,counter))            
    frequency = sorted(frequency, key = lambda x: x[1], reverse= True)
    return frequency

#--------------------------------------------------DATA-------------------------------------------------------
    
alphabetEnglish = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lenAlphabetEnglish = len(alphabetEnglish)
correctChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz \"'.?!():;,‘’"
freqTuple = namedtuple("freqTuple", "letter frequency")
diffTuple = namedtuple("diffTuple", "letter difference")
frequencyEnglish =  [freqTuple( "E", 0.111620),freqTuple( "T", 0.093560),freqTuple( "A", 0.084970),
                     freqTuple( "R", 0.075870),freqTuple( "I", 0.075460),freqTuple( "O", 0.075070),
                     freqTuple( "N", 0.067490),freqTuple( "S", 0.063270),freqTuple( "H", 0.060940),
                     freqTuple( "D", 0.042530),freqTuple( "L", 0.040250),freqTuple( "U", 0.027580),
                     freqTuple( "W", 0.025600),freqTuple( "M", 0.024060),freqTuple( "F", 0.022800),
                     freqTuple( "C", 0.022020),freqTuple( "G", 0.020150),freqTuple( "Y", 0.019940),
                     freqTuple( "P", 0.019290),freqTuple( "B", 0.014920),freqTuple( "K", 0.012920),
                     freqTuple( "V", 0.009780),freqTuple( "J", 0.001530),freqTuple( "X", 0.001500),
                     freqTuple( "Q", 0.000950),freqTuple( "Z", 0.000770)]

vowelsDictionairy = ["A","O","E","I","O","U","Y"]
consonantsDictionairy = ["B","C","D","F","G","H","J","K","L","M","N","P","R","S","T","V","W","X","Z"]

correspondenceSequence = []
for tup1, tup2 in combinations(frequencyEnglish,2):
    correspondenceSequence.append((tup1[0],tup2[0],abs(tup1[1]-tup2[1])))
correspondenceSequence = sorted(correspondenceSequence,key=lambda x: x[2])
#print(correspondenceSequence)

dictionary = {}
with open("dictionary.txt", "r") as fileDictionary:
    dictionary = makedictionary(fileDictionary,alphabetEnglish,1,100)    
    
    
#--------------------------------------------------CONTROL---------------------------------------------------------------------
while(True):
    print("------------------------APLIKACJA DO KRYPTOANALIZY SZYFRÓW  MONOALFABETYCZNYCH PODSTAWIENIOWYCH--------------------")
        #INPUT
    ciphertext = input("Podaj szyfrogram:\n")
    ciphertext = ciphertext.upper()
    x = 0
    try:
        for l in ciphertext:
            if l not in correctChars:
                print("""W podanym szyfrogramie występują znaki spoza alfabetu angielskiego lub inne niż standardowa 
                interpunkcja. Sprawdź czy podany szyfrogram używa alfabetu angielskiego lub usuń dodatkowe znaki.""")
                print("Przyjmowane znaki: ",correctChars)
                print("Wybierz co chcesz dalej zrobić:")
                print("1 - Wprowadzenie innego szyfrogramu")
                print("2 - Wyjście")
                try:
                    x = int(input())
                except:
                    x = 0
                while x != 1 and x !=2:
                    try:
                        x = int(input())
                    except:
                        x = 0                                   
                if x == 1:
                    raise BreakIt
                else:
                    raise                
    except BreakIt:
        continue
    except:
        quit()
    #-------------------------------clearing, counting frequency-----------------------------------------------------
    
    ciphertext = clear(ciphertext,alphabetEnglish)
    ciphertext = ciphertext.upper()
    frequencyCiphertext = countFrequency(ciphertext,alphabetEnglish)
    frequencyCiphertextLetters = list(map(lambda x: x[0],frequencyCiphertext))
    
    print("Częstość występowania liter w podanym szyfrogramie:")
    for i in range(lenAlphabetEnglish):
        print("%s %d"%(frequencyCiphertext[i]))   
    digramfrequencyCiphertext = countDigramFrequency(ciphertext)
    trigramFrequencyCiphertext = countTrigramFrequency(ciphertext)     
    
   
    #----------------------------------------frequancy - speculation-----------------------------------------------------

    potentialKey = [" " for i in range(lenAlphabetEnglish)]
    
    #top frequent letters
    for j in range(5):
        if frequencyCiphertext[j][0] ==  trigramFrequencyCiphertext[0][0][2]:
            potentialKey[4]  =  frequencyCiphertext[j][0]
    for j in range(5):
        if frequencyCiphertext[j][0] ==  trigramFrequencyCiphertext[0][0][0]:
            potentialKey[19] = frequencyCiphertext[j][0]
    Acandidats = []
    for j in range(5):
        if frequencyCiphertextLetters[j] not in potentialKey:
            Acandidats.append(frequencyCiphertextLetters[j])
    for i in range(len(digramfrequencyCiphertext)):       
            #print("wsolwystepujaca z e: ",frequencyCiphertext[i][0])
            if digramfrequencyCiphertext[i][0][0] ==  potentialKey[4] and digramfrequencyCiphertext[i][0][1] in Acandidats:
                potentialKey[0]  = digramfrequencyCiphertext[i][0][1]
                break
            elif digramfrequencyCiphertext[i][0][1] ==  potentialKey[4] and digramfrequencyCiphertext[i][0][0] in Acandidats:
                potentialKey[0]  = igramfrequencyCiphertext[i][0][0]
                break
            

        
   
    print("Po dopasowaniu częstości występowania liter z uwzględnieniem trigramów uzyskano prawdopodobne litery klucza:")
    print(potentialKey)
    print("Częstość występowania digramów w szyfrogramie:")
    print(digramfrequencyCiphertext)
    print("Częstość występowania trigramów w szygramie:")
    print(trigramFrequencyCiphertext)
    consonants = []
    vowels = []
    
    #consoants and vowels division    
    for i in range(1,11):
        su = 0
        for letter in digramfrequencyCiphertext:
            if letter[0] == frequencyCiphertext[i][0]+potentialKey[4] or letter[0] == potentialKey[4] + frequencyCiphertext[i][0]:
                su = su+letter[1]
        if su > frequencyCiphertext[i][1]/2:
            if frequencyCiphertext[i][0] not in potentialKey:
                consonants.append(frequencyCiphertext[i][0])
        if su < frequencyCiphertext[i][1]/10:
            if frequencyCiphertext[i][0] not in potentialKey:
                vowels.append(frequencyCiphertext[i][0])
    
   
    #double vowels    
    #"oo" - hunting
    if len(vowels)>0:
        for i in range(len(digramfrequencyCiphertext)):       
            if digramfrequencyCiphertext[i][0][0] == digramfrequencyCiphertext[i][0][1] and digramfrequencyCiphertext[i][0][0] in vowels:
                potentialKey[14] = digramfrequencyCiphertext[i][0][1]
                vowels.remove(digramfrequencyCiphertext[i][0][1])
                break
       
    print("Po dokonaniu analizy częstości zdublowanych samogłosek uzyskano następujące prawdopodobne litery klucza:")    
    print(potentialKey) 
    
    #"THE" is the most frequent trigram in english!!!
    if len(trigramFrequencyCiphertext) >0:
        if trigramFrequencyCiphertext[0][0][0]==potentialKey[19] and  trigramFrequencyCiphertext[0][0][2] == potentialKey[4] :
            if trigramFrequencyCiphertext[0][0][1] in consonants and trigramFrequencyCiphertext[0][0][1] not in potentialKey:
                potentialKey[7] = trigramFrequencyCiphertext[0][0][1]
                consonants.remove(trigramFrequencyCiphertext[0][0][1])
    
    print("Po dokonaniu analizy częstości trigramów oraz uwzglednieiu podziału na samogłoski i spółgłoski następujące prawdopodobne litery klucza:")
    print(potentialKey)
    
    #hunting for digram "RE"
    if len(consonants)>0:
        for i in range(len(digramfrequencyCiphertext)):
            if potentialKey[4] == digramfrequencyCiphertext[i][0][0]:
                if digramfrequencyCiphertext[i][0][1] in consonants:               
                        potentialKey[17] = digramfrequencyCiphertext[i][0][1]
                        consonants.remove(digramfrequencyCiphertext[i][0][1])
                        break
                elif digramfrequencyCiphertext[i][0][1] not in potentialKey:
                    break
            if potentialKey[4] == digramfrequencyCiphertext[i][0][1]:
                if digramfrequencyCiphertext[i][0][0] in consonants:                
                        potentialKey[17] = digramfrequencyCiphertext[i][0][0]
                        consonants.remove(digramfrequencyCiphertext[i][0][0])
                        break
                elif digramfrequencyCiphertext[i][0][0] not in potentialKey:
                    break
                    
    print("Po dokonaniu analizy częstośći digramów i występowania spółgłosek z samogłoską 'e' uzyskano następujące prawdopodobne litery klucza:")
    print(potentialKey)
    print("Następujące liery skasyfikowane jako samogłoski pozostały nieumieszczone w kluczu:")
    print(vowels)
    print("Następujące liery skasyfikowane jako spółgłoski pozostały nieumieszczone w kluczu:")
    print(consonants)
    #----------------------------------------lexical - speculation----------------------------------------------------
    
    
    while " " in potentialKey:
        wrongPattern = {}
        flag = True
        maxi = 20
        mini = 6
        while flag and " " in potentialKey:
            flag = False
            plaintext = ""
            for letter in ciphertext:
                if letter in potentialKey:
                    plaintext = plaintext + alphabetEnglish[potentialKey.index(letter)]
                else:
                    plaintext = plaintext+ " "
            #print(plaintext)

            for size in range(maxi,mini,-1):
                dictionaryBig = {}
                with open("dictionary.txt", "r") as fileDictionary:         
                    dictionaryBig = makedictionary(fileDictionary,alphabetEnglish,size,size)        
                for pattern in dictionaryBig: 
                    if pattern in wrongPattern:
                        continue
                    for j in range(len(ciphertext)-size):
                        word =  plaintext[j:j+size]
                        if word.count(" ") == 1:
                            gapIndex = word.find(" ")
                            #print(size,len(word),len(pattern))
                            #print([word[gapIndex-jj] for jj in range(1,size)],[pattern[gapIndex-jj] for jj in range(1,size)])
                            if [word[gapIndex-jj] for jj in range(1,size)] == [pattern[gapIndex-jj] for jj in range(1,size)]:               
                                
                                if potentialKey[alphabetEnglish.find(pattern[gapIndex])] == " ":
                                    print("Program znalazł następującą zbitkę:")
                                    print(word)
                                    print("Sugerującą następujące słowo:")
                                    print(pattern)
                                    #print(j)
                                    print("Odpowiada ono takiemu szyfrogramowi: ")
                                    print(ciphertext[j:j+size])
                                    print("Wpisz 1 aby zatwierdzić aktualizacje klucza, lub 0 aby nie uznać tej sugestii")
                                    steruj = input()
                                    if steruj == "1":
                                        potentialKey[alphabetEnglish.find(pattern[gapIndex])] = ciphertext[j+gapIndex]
                                        flag = True
                                    else:
                                        wrongPattern.update({pattern:len(wrongPattern)})
                                        break
                                        
            if mini < 7:
                mini+=1
            print("Po uwzględnieniu ostatnich pasujacych zbitek uzyskano następujące prawdopodobne litery klucza:")
            print(potentialKey)
        print("Po przeszukaniu wszystkich wzorów słów o długościach od %d do %d usyskano następujący prawdopodobny tekst jawny oraz klucz"%(mini,maxi))
        plaintext = ""
        for letter in ciphertext:
            if letter in potentialKey:
                plaintext = plaintext + alphabetEnglish[potentialKey.index(letter)]
            else:
                plaintext = plaintext+ " "
        print(plaintext)
        print(potentialKey)
        if " " in potentialKey:
            print("Program wyczerpał możliwości kryptoanalizy. Jeżeli odgadujesz dalsze wartości klucza podaj je by ukończyć deszyfracje")
            print("Podaj literę alfabetu którą zdeszyfrowałeś, lub wpisz 1 aby zakończyć działanie programu:")
            letp = input().upper()
            while True:
                if letp == "1":
                    quit()
                if letp in alphabetEnglish:
                    keyIndex = alphabetEnglish.find(letp)
                    if potentialKey[keyIndex] == " ":
                        print("Podaj literę alfabetu będącą szyfrogramem powyższej litery")
                        letc = input().upper()
                        if letc in alphabetEnglish:
                            if letc not in potentialKey:                        
                                potentialKey[keyIndex] = letc
                                break
                            else:
                                print("Ta litera jest już przypisana do klucza, podaj inną literę będącą szyfrogramem, lub wpisz 1 aby zakończyć")
                                letc = input().upper()

                    else:
                        print("Podano już zdeszyfrowaną literę, poddaj inną zdeszyfrowaną literę, lub wpisz 1, aby zakończyć")
                        letp = input().upper()
                else:
                    print("Podano niewłaściwy znak, spróbuj jeszcze raz")
                    letp = input().upper() 
        if potentialKey.count(" ") ==1:
            for letter in alphabetEnglish:
                if letter not in potentialKey:
                    potentialKey[potentialKey.index(" ")] = letter
    plaintext = ""
    for lettr in ciphertext:
        if lettr in potentialKey:
            plaintext = plaintext + alphabetEnglish[potentialKey.index(lettr)]
        else:
            plaintext = plaintext+ " "
      
    print(plaintext)
    print(potentialKey)
    print("Pomyślnie odtworzono cały klucz i odszyfrowano pełen szyfrogram, (patrz powyżej)")  
    print("Po wprowadzeniu dowolnego znaku  program zakończy działanie: ")
    
    a = input()     
    quit()
quit()  


# In[ ]:


def encrypt(plaintext, key, alphabet):
    ciphertext = ""
    c = [key[alphabet.index(l)] for l in plaintext]
    ciphertext = "".join(c)         
    return ciphertext

def decrypt(ciphertext, key, alphabet):
    p = [alphabet[key.index(l)] for l in ciphertext]
    plaintext = "".join(p)    
    return plaintext

def countFrequency(text, alphabet):
    frequency = []
    lenText = len(text)
    for a in alphabet:
        counter = 0
        for l in text:
            if l == a:
                counter+=1
        frequency.append(counter/lenText)        
    return frequency


alphabetEnglish = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "LTUVWXYZIJKABCDEFGHMNOPQRS"
plaintext = "NOCZESCJESTEMPRZYKLADOWYMPLAINTEXTEM"
decrypt(encrypt(plaintext, key, alphabetEnglish),key,alphabetEnglish)


# In[1]:


from random import randint
def clear(text, alphabet):
    i= 0
    while i<len(text):
        if text[i] not in alphabet:
            text = text.replace(text[i], u'')
        else:
            i+=1
    return text
def randKey(alphabet):
    l = len(alphabet)
    pula = alphabet
    key = ''
    for i in range(l):
        ind = randint(0,len(pula)-1)
        key = key + pula[ind]
        pula = pula.replace(pula[ind],"")
    return key                  

def encrypt(plaintext, key, alphabet):
    ciphertext = ""
    plaintext = plaintext.upper()
    plaintext = clear(plaintext,alphabet)    
    c = [key[alphabet.index(l)] for l in plaintext]
    ciphertext = "".join(c)         
    return ciphertext

plaintext = """Frodo woke suddenly. It was still dark in the room. Merry was standing there with a candle in one hand, and banging on the door with the other. ‘All right! What is it?’ said Frodo, still shaken and bewildered.

‘What is it!’ cried Merry. ‘It is time to get up. It is half past four and very foggy. Come on! Sam is already getting breakfast ready. Even Pippin is up. I am just going to saddle the ponies, and fetch the one that is to be the baggage-carrier. Wake that sluggard Fatty! At least he must get up and see us off.’

Soon after six o’clock the five hobbits were ready to start. Fatty Bolger was still yawning. They stole quietly out of the house. Merry went in front leading a laden pony, and took his way along a path that went through a spinney behind the house, and then cut across several fields. The leaves of trees were glistening, and every twig was dripping; the grass was grey with cold dew. Everything was still, and far-away noises seemed near and clear: fowls chattering in a yard, someone closing a door of a distant house.

In their shed they found the ponies; sturdy little beasts of the kind loved by hobbits, not speedy, but good for a long day’s work. They mounted, and soon they were riding off into the mist, which seemed to open reluctantly before them and close forbiddingly behind them. After riding for about an hour, slowly and without talking, they saw the Hedge looming suddenly ahead. It was tall and netted over with silver cobwebs. ‘How are you going to get through this?’ asked Fredegar. ‘Follow me!’ said Merry, ‘and you will see.’ He turned to the left along the Hedge, and soon they came to a point where it bent inwards, running along the lip of a hollow. A cutting had been made, at some distance from the Hedge, and went sloping gently down into the ground. It had walls of brick at the sides, which rose steadily, until suddenly they arched over and formed a tunnel that dived deep under the Hedge and came out in the hollow on the other side.

Here Fatty Bolger halted. ‘Good-bye, Frodo!’ he said. ‘I wish you were not going into the Forest. I only hope you will not need rescuing before the day is out. But good luck to you - today and every day!’

‘If there are no worse things ahead than the Old Forest, I shall be lucky,’ said Frodo. ‘Tell Gandalf to hurry along the East Road: we shall soon be back on it and going as fast as we can.’ ‘Good-bye!’ they cried, and rode down the slope and disappeared from Fredegar’s sight into the tunnel.

It was dark and damp. At the far end it was closed by a gate of thick-set iron bars. Merry got down and unlocked the gate, and when they had all passed through he pushed it to again. It shut with a clang, and the lock clicked. The sound was ominous.

‘There!’ said Merry. ‘You have left the Shire, and are now outside, and on the edge of the Old Forest.’

‘Are the stories about it true?’ asked Pippin.

‘I don’t know what stories you mean,’ Merry answered. ‘If you mean the old bogey-stories Fatty’s nurses used to tell him, about goblins and wolves and things of that sort, I should say no. At any rate I don’t believe them. But the Forest is queer. Everything in it is very much more alive, more aware of what is going on, so to speak, than things are in the Shire. And the trees do not like strangers. They watch you. They are usually content merely to watch you, as long as daylight lasts, and don’t do much. Occasionally the most unfriendly ones may drop a branch, or stick a root out, or grasp at you with a long trailer. But at night things can be most alarming, or so I am told. I have only once or twice been in here after dark, and then only near the hedge. I thought all the trees were whispering to each other, passing news and plots along in an unintelligible language; and the branches swayed and groped without any wind. They do say the trees do actually move, and can surround strangers and hem them in. In fact long ago they attacked the Hedge: they came and planted themselves right by it, and leaned over it. But the hobbits came and cut down hundreds of trees, and made a great bonfire in the Forest, and burned all the ground in a long strip east of the Hedge. After that the trees gave up the attack, but they became very unfriendly. There is still a wide bare space not far inside where the bonfire was made.’

‘Is it only the trees that are dangerous?’ asked Pippin.

‘There are various queer things living deep in the Forest, and on the far side,’ said Merry, ‘or at least I have heard so; but I have never seen any of them. But something makes paths. Whenever one comes inside one finds open tracks; but they seem to shift and change from time to time in a queer fashion. Not far from this tunnel there is, or was for a long time, the beginning of quite a broad path leading to the Bonfire Glade, and then on more or less in our direction, east and a little north. That is the path I am going to try and find.’

The hobbits now left the tunnel-gate and rode across the wide hollow. On the far side was a faint path leading up on to the floor of the Forest, a hundred yards and more beyond the Hedge; but it vanished as soon as it brought them under the trees. Looking back they could see the dark line of the Hedge through the stems of trees that were already thick about them. Looking ahead they could see only tree-trunks of innumerable sizes and shapes: straight or bent, twisted, leaning, squat or slender, smooth or gnarled and branched; and all the stems were green or grey with moss and slimy, shaggy growths.

Merry alone seemed fairly cheerful. ‘You had better lead on and find that path,’ Frodo said to him. ‘Don’t let us lose one another, or forget which way the Hedge lies!’

They picked a way among the trees, and their ponies plodded along, carefully avoiding the many writhing and interlacing roots. There was no undergrowth. The ground was rising steadily, and as they went forward it seemed that the trees became taller, darker, and thicker. There was no sound, except an occasional drip of moisture falling through the still leaves. For the moment there was no whispering or movement among the branches; but they all got an uncomfortable feeling that they were being watched with disapproval, deepening to dislike and even enmity. The feeling steadily grew, until they found themselves looking up quickly, or glancing back over their shoulders, as if they expected a sudden blow.

There was not as yet any sign of a path, and the trees seemed constantly to bar their way. Pippin suddenly felt that he could not bear it any longer, and without warning let out a shout. ‘Oi! Oi!’ he cried. ‘I am not going to do anything. Just let me pass through, will you!’

The others halted startled; but the cry fell as if muffled by a heavy curtain. There was no echo or answer though the wood seemed to become more crowded and more watchful than before.

‘I should not shout, if I were you,’ said Merry. It does more harm than good.’

Frodo began to wonder if it were possible to find a way through, and if he had been right to make the others come into this abominable wood. Merry was looking from side to side, and seemed already uncertain which way to go. Pippin noticed it. ‘It has not taken you long to lose us,’ he said. But at that moment Merry gave a whistle of relief and pointed ahead.

‘Well, well!’ he said. ‘These trees do shift. There is the Bonfire Glade in front of us (or I hope so), but the path to it seems to have moved away!’

The light grew clearer as they went forward. Suddenly they came out of the trees and found themselves in a wide circular space. There was sky above them, blue and clear to their surprise, for down under the Forest-roof they had not been able to see the rising morning and the lifting of the mist. The sun was not, however, high enough yet to shine down into the clearing, though its light was on the tree-tops. The leaves were all thicker and greener about the edges of the glade, enclosing it with an almost solid wall. No tree grew there, only rough grass and many tall plants: stalky and faded hemlocks and wood-parsley, fire-weed seeding into fluffy ashes, and rampant nettles and thistles. A dreary place: but it seemed a charming and cheerful garden after the close Forest.

The hobbits felt encouraged, and looked up hopefully at the broadening daylight in the sky. At the far side of the glade there was a break in the wall of trees, and a clear path beyond it. They could see it running on into the wood, wide in places and open above, though every now and again the trees drew in and overshadowed it with their dark boughs. Up this path they rode. They were still climbing gently, but they now went much quicker, and with better heart; for it seemed to them that the Forest had relented, and was going to let them pass unhindered after all.

But after a while the air began to get hot and stuffy. The trees drew close again on either side, and they could no longer see far ahead. Now stronger than ever they felt again the ill will of the wood pressing on them. So silent was it that the fall of their ponies’ hoofs, rustling on dead leaves and occasionally stumbling on hidden roots, seemed to thud in their ears. Frodo tried to sing a song to encourage them, but his voice sank to a murmur."""
      
plaintext2 = """ The fighting occurred in the precipitous, rocky terrain of the strategically important Galwan Valley, which lies between China's Tibet and India's Ladakh.

Indian media say soldiers engaged in direct hand-to-hand combat, with some "beaten to death". During the fight, one newspaper reported, others fell or were pushed into a river.

The Indian army initially said a colonel and two soldiers had died. It later said that "17 Indian troops who were critically injured in the line of duty" and died from their injuries, taking the "total that were killed in action to 20".

The clash has provoked protests in India, with people burning Chinese flags.

Addressing the issue on Wednesday, Prime Minister Modi said: "India wants peace but when provoked, India is capable of giving a fitting reply, be it any kind of situation.

He said he wanted to "assure the nation" the loss of the soldiers would "not be in vain".

"For us, the unity and sovereignty of the country is the most important," he added.

China did not confirm the number of casualties, but accused India of crossing the border onto the Chinese side.

China's foreign ministry said on Wednesday it wanted to avoid further clashes and reiterated that it was not to blame.

This is not the first time the two nuclear-armed neighbours have fought without conventional firearms on the border. India and China have a history of face-offs and overlapping territorial claims along the more than 3,440km (2,100 mile), poorly drawn Line of Actual Control (LAC) separating the two sides.

Don't expect any more confirmation from China
Analysis by Robin Brant, BBC News, Beijing

The official line from Beijing is that China and India have an agreement to "peacefully resolve" their Himalayan border dispute. The foreign ministry also repeated claims that Indian forces "provoked and attacked" their Chinese counterparts. But that's where the detail ends.

China has not confirmed how many of its personnel died or were injured. The Indian media has reported gruesome details. There are claims that US intelligence agencies think China suffered a loss of life in the dozens. But the closest Beijing has come to any official confirmation is a tweet from the state-run Global Times newspaper saying it has "never reported the exact casualties on the Chinese side'".

The main reason is that China just doesn't do that. Going back decades it's never given contemporaneous confirmation on military deaths outside of peacekeeping duties. Sometimes numbers have emerged, but many, many years later.

On this occasion China's propagandists may not want to fan nationalist flames at home by making much of any loss. Or they may not want to admit to a significant and demoralising loss. Or, as has long been the case, they just don't want to admit if Chinese soldiers have been killed in action.

How tense is the area?
The LAC is poorly demarcated. The presence of rivers, lakes and snowcaps means the line can shift. The soldiers either side - representing two of the world's largest armies - come face-to-face at many points.

Border patrols have often bumped into each other, resulting in occasional scuffles."""   
      #ABCDEFGHIJKLMNOPQRSTUVWXYZ
      #FVBOREZAQWSYUDJHMGCLNITPXK
key = "FVHORBNJDWSYXQGZMACLTIEKUP"
alphabetEnglish = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
print(encrypt(plaintext2,key,alphabetEnglish))


# In[22]:


def clear(text, alphabet):
    i= 0
    while i<len(text):
        if text[i] not in alphabet:
            text = text.replace(text[i], u'')
        else:
            i+=1
    return text

def makedictionary(file,alphabet):
    D = {}
    index = 0   
    for slowo in file:
        slowo = slowo.rstrip()        
        #slowo = slowo.decode('windows-1250')
        slowo = slowo.upper()        
        slowo = clear(slowo,alphabet)        
        D.update({slowo:index})
        index+=1    
    return D

alphabetEnglish = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dictionary = {}
with open("dictionary.txt","r") as f:
    dictionary = makedictionary(f,alphabetEnglish)   
print("ACCOMPANY" in D)
print(type(f))


# In[21]:


def diffCalc(pattern, argument):
    if len(pattern) != len(argument):
        raise Exception("Wrong number of letter. Comparing impossible")
    counter = 0
    for i in range(len(pattern)):
        if argument[i] != pattern[i]:
            counter += 1
    return counter
A ="ALFABET"
B ="ABFTE"
i = 0


# In[6]:


A ="abc"
A.find


# In[16]:


D= "ABCD"
D.find


# In[ ]:




