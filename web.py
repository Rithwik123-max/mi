import requests
from bs4 import BeautifulSoup
from tkinter import*
from PIL import Image,ImageTk
root=Tk()
root.geometry("800x600")
root.title("Live Cricket Score")
image=Image.open("cricket.png")
photo=ImageTk.PhotoImage(image)
img=Label(image=photo)
img.pack()

font="comicsans 15 bold"

# while True:
def main():
    url="https://www.cricbuzz.com/cricket-match/live-scores"

    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")
    soup.prettify()
    try:
        date=soup.find('span',class_="text-gray").text
        print(date)
        da=Label(text=date,font=font)
        da.pack()
            
    except AttributeError:
        print('No live cricket matches are detected')
        noMatch=Label(text="No live cricket matches are detected")
        noMatch.pack()
        exit()

    place=soup.find('div',class_="text-gray").text
    print(place)
    p=Label(text=place,font=font)
    p.pack()
        


    t1=soup.find_all('div',class_="cb-ovr-flo cb-hmscg-tm-nm")
    s1=soup.find_all('div',class_="cb-ovr-flo")

    print(t1[0].text,'-->',s1[2].text)
    print(t1[1].text,'-->',s1[4].text)
    team1Name=Label(text=t1[0].text,font=font)
    team1Score=Label(text=s1[2].text,font=font)
    team2Name=Label(text=t1[1].text,font=font)
    team2Score=Label(text=s1[4].text,font=font)

    team1Name.pack()
    team1Score.pack()
    team2Name.pack()
    team2Score.pack()

    try:
        comment=soup.find('div',class_="cb-text-live").text
        print(comment)
        c=Label(text=comment,fg="green",font=font)
        c.pack()

            
    except AttributeError:
        come=soup.find('div',class_="cb-text-complete").text
        print('winner-->',come)
        win=Label(text=come,fg="blue",font=font)
        win.pack()
    root.mainloop()


f1=Frame(root,bg="grey",borderwidth=6)
f1.pack()
btn=Button(f1,fg="red",text="Refresh",command=main,activeforeground="red",cursor="plus")
btn.pack()
main()
