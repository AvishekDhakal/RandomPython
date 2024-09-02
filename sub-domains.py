import requests
from bs4 import BeautifulSoup


r = requests.get("https://crt.sh/?q=note.shiril.com.np")
# The line `soup = BeautifulSoup(r.content, 'html5lib')` is creating a BeautifulSoup object from the
# content of the HTTP response obtained from the URL "https://crt.sh/?q=google.com".
soup = BeautifulSoup(r.content, 'html5lib')  #so what is did first was created an object bs4.BeautifulSoup. just think of it like creating a list but for html contents. 
print(type(soup))

tables = soup.find_all('table') #this is where i am finding all the table elements in the contents. 
print("all tables class", type(tables))
table_we_want = tables[2] #this is me selecting the 2nd table tag which is where the sub domains were located.
print("After selecting second",type(table_we_want))
t_body_want = (table_we_want.find('tbody')) #further getting inside and selecting first tag.
print(type(t_body_want))
tag_we_want = (t_body_want.find_all('tr')[1:]) #the first list returned empty for tr so thats why silce it after 1st. 
print("sliced",type(tag_we_want))
# print(tag_we_want) # One whole list 

i = 1
for tags in tag_we_want:  #so the tag_we_want may be list but inside it is still <class 'bs4.element.Tag'> this class. That is why we were able to apply below method.
    # print(tags)
    c = (tags.find_all('td')) #finding all td tags in individual <tr> tags.
    print(i,c[4].get_text())  #the fourth column contained the link i wanted. 
    i = i + 1 

# print("looped element:", type(tags)) # this is tag element only but when we again use find_all() here the result c is converted in to Result.set()

# print(type(c)) 


# A major mistake I made was considering after type conversion the elements inside list would not act as bs4 elements but it did. cause afer line 13 the table_we_want is a list type and i thought the the elemts would be too but no.



#Notes

# <class 'bs4.element.ResultSet'> vs <class 'bs4.element.Tag'>

# so one is like lists and another is like individual elements like int or str 

# you will typically end up with ResultSet after you use methods like find_all() or select
# and to use individual elements insidde ResultSet you index them and get Tag class which is basically individual elements.
