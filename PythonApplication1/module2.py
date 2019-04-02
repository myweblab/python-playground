import re
import optparse

def Main2():
    parser = optparse.OptionParser("Usage wrong -w <word> -f <fiile>")
    parser.add_option("-w", dest='word', type='string',help="h")
    parser.add_option('-f', dest='fname',type='string',help='t')
    (options, args) = parser.parse_args()
    if(options.word == None) | (options.fname == None):
        print(parser.usage)
        exit(0)
    else:
        word = options.word
        fname = options.fname
    searchfile = open(fname)
    linenum = 0
    for line in searchfile.readline():
        line = line.strip('\n\r')
        linenum +=1
        searchresult = re.search(word,line,re.M|re.I)
        searchResult = re.search(r'think',line, re.M|re.I)
        if searchResult:
            print("Match Found " + str(linenum) +':'+ line)

def Main():
    line = "I think I Understand regular expressions"
    matchResult = re.match(r'think',line,re.M|re.I)
    if matchResult:
        print("Match Found " + matchResult.group())
    else:
        print("Not found")
    
    searchResult = re.search(r'think',line, re.M|re.I)
    if searchResult:
        print("Match Found " + searchResult.group())
    else:
        print("Not found")

Main2()


