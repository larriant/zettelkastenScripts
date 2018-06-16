import os

for filename in os.listdir('../'):
    if filename.endswith(".md"):
        timestamp = filename[0:12]
        if timestamp.isdigit():
            title = filename[12:-3]
            print('Timestamp', timestamp)
            print('Title:', title)
            
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
            print('Answer:', lines[5:moreLine])
            print(' ')
            print(' ')
