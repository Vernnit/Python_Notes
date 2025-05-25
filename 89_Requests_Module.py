# Requests module is used to make HTTP requests.


# In the easiest words, data parsing is converting data from one format to another. For example, if a text is in HTML format, data parsing can help you convert the file into a more readable format, such as normal text.

# Beautiful soup is used  to parse the data   -bs4

import requests
response = requests.get('http://www.google.com')
print(response.text)  
# print(help(response))

print(response.status_code)     #200 means success , 300 redirect , 400 client error no permission etc , 500 server error. 
print(response.ok)              # prints True if source code is 200s and 300s. False if there is any client or server error.



# TO DOWNLOAD IMAGE-

r = requests.get('https://365datascience.com/resources/blog/2020-02-python-requests-package-how-to-download-web-files-python.jpg')        #image adress or image url.
# print(r.content)
with open('python.jpg' , 'wb') as f:                                          #write bytes
    f.write(r.content)                                                        #.content to download.
print(r.content)                                                              #prints the bytes of the image.

# for headings in r.find_all('h2'):
#     print(headings)


# print(r.headers)                                                            #prints all the headers with response.




# HTTPBIN.org is a site to test different requests made by the same person who wrote requests module.

# x = requests.get('https://httpbin.org/get?page=2&count=25')         #parameters given with url itself.


import requests
# giving params as a dictionary.
payload = {'page':2, 'count':25} 
x=requests.get('https://httpbin.org/get' , params=payload)
print(x.status_code)
print(x.text)
print(x.url)                                                          #gives the same url we gave Above.


# TO POST REQUEST. give a form which is relevant by looking at the html source code.

payload ={'username':'vernnitverma' ,'password':'vermavernnit'} 
x=requests.post('https://httpbin.org/post' , data=payload) 
print(x.text)

# to read a json response use (.json) - you get a dictionary.