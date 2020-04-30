from chatterbot import ChatBot
from tkinter import *
bot=ChatBot(
	"AI",
	storage_adapter = "chatterbot.storage.SQLStorageAdapter",
	logic_adapter = [
		"chatterbot.logic.BestMatch",
		"chatterbot.logic.TimeLogicAdapter",
		"chatterbot.logic.MathematicalEvaluation"
	],
	input_adapter = "chatterbot.input.TerminalAdapter",
	output_adapter = "chatterbot.output.TerminalAdapter",
	database = "./database.accdb")

def main():
	root=Tk()
	root.geometry("400x300")	
	root.resizable(False, False)
	root.title("BOT")

	usr=StringVar() #distancia de surcos
	usr.set(0)
	r=StringVar()
	r.set(0)
    

	def res():
		Us=usr.get()
		re=bot.get_response("holaaa")
		r.set(re)

		
	Label(root,text="CHAT-BOT").pack()
	Label(root,text="").pack()
	Label(root,text="Message").pack()
	Label(root,text="").pack()
	Entry(root,textvariable=usr).pack()
	Label(root,text="").pack()
	Entry(root,textvariable=r,state="disabled").pack()
	Label(root,text="").pack()
	Button(root,text="Enviar", command=res).pack()





	root.mainloop()

main()
