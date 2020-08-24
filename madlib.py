def madlib(name, subject):
    if name == "" or subject == "":
        if name == "" and subject != "":
            name = "Joseph"
        elif name != "" and subject == "":
            subject = "math"
        elif name == "" and subject == "":
            name = "Mary"
            subject = "laziness"
    return(f"{name}'s favorite subject is {subject}.")

input_name = input("Please enter a name: ")
input_subject = input("Please enter a subject: ")
favorite_subject_sentence = madlib(input_name, input_subject)
print(favorite_subject_sentence)
