import requests
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


STATE1 = 1
STATE2 = 2

def welcome(update, context):
    try:
        username = update.message.from_user.username
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = 'Olá, ' + firstName + '!'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except Exception as e:
        print(str(e))


def sofriviolencia(update, context):
    try:
        message = '''Você está machucada fisicamente?\n
                1 - Sim \n
                2 - Não \n'''
        update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
        return STATE1
    except Exception as e:
        print(str(e))


def inputRespSF(update, context):
    respSF = lower(update.message.text)
    print(respsf)
    if respSF == '1' or respSF == 'sim' or respSF == 's':
        message = """Você sofreu uma das categorias de Violências físicas contra a Mulher... 
                        \nNos ajude a saber em qual respondendo a proxima questão."""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
        #vai mudando o STATE a cada nova pergunta ou estado
    else:
        if respSF == '2' or respSF == 'não' or respSF == 'n':
        message = """Você pode ter sofrido um tipo de Assédio ou(RevengePorn, Ciberbullyng...) 
                        \nNos ajude a saber respondendo a proxima questão."""
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    
def inputMinhaVoz(update, context):
    #feedback = update.message.text  aqui não vamos ler nada do usuário
    message = '''Visite o nosso site www.minhavoz.com e saiba como pedir ajuda.\n
               Se quiser também pode desabafar sobre o seu problema, \n
               além de ler experiências de quem já passou por isso.'''
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def cancel(update, context):
    return ConversationHandler.END


def main():
    try:
        # token = os.getenv('TELEGRAM_BOT_TOKEN', None)
        #token = 'cole_aqui_o_token_de_acesso_do_seu_bot'
        token = 'cole_aqui_o_token_de_acesso_do_seu_bot'
        updater = Updater(token=token, use_context=True)

        updater.dispatcher.add_handler(CommandHandler('start', welcome))
    
        conversation_handler = ConversationHandler(
            entry_points=[CommandHandler('sofriviolencia', sofriviolencia)],
            states={
                STATE1: [MessageHandler(Filters.text, inputRespSF)],
                STATE2: [MessageHandler(Filters.text, inputMinhaVoz)]
            },
            fallbacks=[CommandHandler('cancel', cancel)])
        updater.dispatcher.add_handler(conversation_handler)

        print("Updater no ar1: " + str(updater))
        updater.start_polling()
        updater.idle()
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
