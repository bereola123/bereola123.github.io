def answer_Question():
    import random
    import math
    answers = ["It is certain", "It is decidedly so",
               "Without a doubt", "Yes definitely",
               "You may rely on it", "As I see it, yes",
               "Most likely", "Outlook good", "Yes",
               "Signs point to yes",
               "Reply hazy try again", "Ask again later",
               "Better not tell you now",
               "Cannot predict now",
               "Concentrate and ask again",
               "Don't count on it",
               "My reply is no", "My sources say no",
               "Outlook not so good", "Very doubtful"]
    question = raw_input('Ask me a Question!')
    if(question[len(question) -1] == "?"):
        i = random.randint(0, len(answers))
        print answers[i]
        print question
    else:
        print("I don't understand the question, please try again")

answer_Question()
