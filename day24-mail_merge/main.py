#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

def create_letter(name: str) -> None:
    with open(rf".\day24-mail_merge\Output\ReadyToSend\{name}.txt", mode="w") as f_send:
        with open(r".\day24-mail_merge\Input\Letters\starting_letter.txt") as f_template:
            content = f_template.read()
            content = content.replace("[name]", name)
            f_send.write(content)




with open(r".\day24-mail_merge\Input\Names\invited_names.txt") as f_names:
    for name in f_names.readlines():
        name = name.strip('\n')
        create_letter(name)







