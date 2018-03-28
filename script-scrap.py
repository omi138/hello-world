from tkinter import *
from bs4 import BeautifulSoup as bs
import  requests
def fetchdetail(topicc):
    url='http://10bestquotes.com/'+topicc+'/'
    r = requests.get(url)

    soup = bs(r.content,'html.parser')

    #print(list(soup.children))
    #print(soup.prettify())
    #links = soup.find_all('p')

    #print(list(soup.children))
    htmll = list(soup.children)[2]
    #print(htmll)
    f1 = open("big_bang.txt","w")
    li = soup.find_all('p')

    for line in li:
        textt = line.text
        print(textt)
        quote = re.match(r'([\d]{1,2})(\D)+',textt)
        #if quote:
        if quote == None:
            print("none")
        else:
            yield quote.group()
           # f1.write(quote.group().strip() + "\n")

    f1.close()

def printtext():
    global var
 #   global text
    global e
    global root
    string = e.get()
    print(string)



    textFromWeb = ""
    var.set("")
    for item in fetchdetail(string):
        #text.insert(INSERT,str(item) + '\n')
        textFromWeb = textFromWeb + str(item).strip() + '\n'
        var.set(textFromWeb)
    text.pack()

root = Tk()
var = StringVar()
root.title('Quote It!')
text = Label(root,textvariable=var,font=("Helvetica", 10),justify=LEFT,anchor=W,wraplength=550)

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='Get quotes',command=printtext)
b.pack(side='bottom')



root.mainloop()


#to add image

