def main():
    #input from user
    message = input()
    result = convert(message)
    print(result)

def convert(message):
        #Replace :) for happy
        message1= message.replace(":)" ,"🙂")
        #Replace :( for sad
        message2= message1.replace(":(" ,"🙁")

        #returning string
        return message2
main()