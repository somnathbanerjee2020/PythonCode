import os.path
import urllib.request

links = open('urls.txt', 'r')
for link in links:

    #Get one line of text (e.g. http://server/files/grades.doc),
    # then get the filename from the end of the URL
    link = link.strip()
    filename = link.rsplit('/', 1)[-1]

    #Does this file exist in this folder? If not, download it
    if not (os.path.isfile(filename)):
        print('Downloading: ' + filename )
        try:
            urllib.request.urlretrieve(link, filename)
            print("File size was", os.path.getsize(filename))
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error. Continuing.')
    
    #File exists; don't download
    else:
        print("This file exists already.")

#End of program
print("Finished downloading.")