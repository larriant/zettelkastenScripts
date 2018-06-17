import os
import itertools

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)

def getZettels():
    zettels = []
    for filename in os.listdir('../'):
        if filename.endswith(".md"):
            timestamp = filename[0:12]
            if timestamp.isdigit():
                title = filename[12:-3]
                print('Timestamp', timestamp)
                file_object = open('../' + filename, 'r')
                lines = file_object.readlines()
                numLines = len(lines)
                # print(numLines)
                more = False
                checkLine = 5
                moreLine = 0
                # print(lines[checkLine])

                while more is False and checkLine < numLines:
                    line = lines[checkLine].strip()
                    # print(checkLine)
                    # print('1',line,'2')
                    # print(len(line))
                    if line == '# More':
                        # print('FOUND AN ALSO LINE')
                        more = True
                        moreLine = checkLine
                    else:
                        checkLine += 1
                answer = lines[5:moreLine]
                zettels.append((title, answer))
                print(' ')
                print(' ')
    return zettels

def getQuestions(zettels, numZettels):
    body = ''
    for x in range(0, 8):
        question = ''
        if zettels[x] != None:
            question = zettels[x][0]
        body += f'\t<div class="box"><p>{question}<p></div>'
        if x != 7:
          body += '\n'
    return body;

def getAnswers(zettels, numZettels):
    body = ''
    for x in range(0, 8):
        answer = ''
        if zettels[x] != None:
            answer = ''.join(zettels[x][1]).replace('\n', '</p><p>')
        body += f'\t<div class="box"><p>{answer}</p></div>'
        if x != 7:
          body += '\n'
    return body;

def dictionaryToHTML(zettels):
    file= open("zettelkasten.html","w")
    body = ''
    eight_zettels_list = list(grouper(8, zettels))
    for eight_zettels in eight_zettels_list:
        numZettels = len(eight_zettels)
        body += getQuestions(eight_zettels, numZettels)
        body += getAnswers(eight_zettels, numZettels)

    #write then close file
    html = """
      <html>
        <head>
          <title>Zettelkasten</title>
          <style>
          html,body{
            height:297mm;
            width:210mm;
            /* to centre page on screen*/
            margin: 0;
            margin-left: auto;
            margin-right: auto;
          }
          body {
            display: flex;
            flex-wrap: wrap;
          }
          p {
            left: 0;
            right: 0;
            margin-top: 10px; 
            padding: 0 5px;
          }
          .box {
            position: relative;
            display: inline-block;
            height: calc(74.25mm - 2px);
            width: calc(105mm - 2px);
            border: 1px solid blue;
            text-align: center;
          }
          </style>
        </head>
        <body>
        %s
        </body>
      </html>
    """ %(body)
    file.write(html)
    file.close()

zettels = getZettels()
print(zettels)
dictionaryToHTML(zettels)
