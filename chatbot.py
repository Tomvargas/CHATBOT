from chatterbot import ChatBot
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
	database = "./database.accdb"
)

while True:
	print ('bot: ',bot.get_response(None))
