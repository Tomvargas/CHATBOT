from chatterbot import ChatBot
from tkinter import *
bot=ChatBot(
	"AI",
	storage_adapter = "chatterbot.storage.SQLStorageAdapter",
	logic_adapter = [
		"chatterbot.logic.TimeLogicAdapter",
		"chatterbot.logic.MathematicalEvaluation"
	],
	database_uri = "sqlite:///chatbot.sqlite3")

def main():
	root=Tk()
	root.geometry("400x600")	
	root.resizable(False, False)
	root.title("BOT")
	bg=PhotoImage(file="graphics/bg.png")
	Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

	usr=StringVar() #distancia de surcos
	usr.set("")
	r=StringVar()
	r.set(" ")
    

	def res():
		r.set(bot.get_response(usr.get()))
		usr.set("")

	Label(root,text="CHAT-BOT",bg="#18a1d3",fg="white",font=(40)).place(x=24,y=15)
	"""Label(root,text="Message").pack()
				Label(root,text="").pack()"""
	avtr=PhotoImage(file="graphics/avtr.png")
	Label(root, image=avtr,bg="#282923").place(x=98,y=136)
	ent=Entry(root,textvariable=usr,bg="#46483d",fg="white",relief=FLAT, width=30,font=(20))
	ent.place(x=50, y=538)
	
	
	Label(root,textvariable=r,bg="#282923",fg="white",font=(25)).place(x=100,y=350)
	but=Button(root,text="►", command=res,relief=FLAT,bg="#18a1d3",fg="white",font=(25))
	but.place(x=320,y=534) 
	root.mainloop()

main()
