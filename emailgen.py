import email
import random
import string
import time
import os
output = []
randomLeghnt = 5

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def prefixgen(exportAmount, Email):
    for i in range(exportAmount):
        ranID = get_random_string(5)
        Emailcore = Email.replace("@gmail.com", "")
        final = "{}+{}@gmail.com".format(Emailcore, ranID)
        output.append(final)
    print(output)
    input("Aperte enter para continuar...")
    mainmenu()

def exportprefix(exportdir):
    try:
        Directory = r'{}\Output.txt'.format(exportdir)
        print("file location: " + Directory)
        with open(Directory, 'w') as fp:
            for item in output:
                fp.write("%s\n" % item)
            
            print('\033[32m' + "E-mail's gerados e exportados para diretório" + '\033[0m')
            input("Aperte enter para continuar...")
            mainmenu()
    except:
        print('\033[31m' + "Diretório não encontrado ou email's não gerados" + '\033[0m')
        input("Aperte enter para continuar...")
        mainmenu()


def mainmenu():
    os.system('cls')
    print('\033[35m' + """  
                                                                                                                                                                                                     

""" + '\033[0m')
    print('\033[35m' + """ 

    [1] Gerar e-mail's
    [2] Exportar e-mail's
    [3] Fechar programa                                                                                                  

""" + '\033[0m')
    answer = input()
    if answer == "1" :
        email
        genAmount = int(input("Quantas contas você pretende gerar?         "))
        emailinput = input("Digite o g-mail base                         ")
        prefixgen(genAmount, emailinput)
        

    elif answer == "2":
        exportpath = input("Onde você quer salvar o arquivo? ")
        exportprefix(exportpath)


    elif answer == "3":
        print("")
    else:
        print('\033[31m' + "Isso não é um caminho válido" + '\033[0m')

mainmenu()
