
todo = []

while True:

    user_prompt = input("Entrada de fazer: ")
    user_prompt = user_prompt.strip()

    match user_prompt:
        case "Adicionar":
            fazer = input("Enter a todo: ") + "\n"  

            with open('Files/todos.txt','r') as arquivo:
                todo = arquivo.readlines()          

            todo.append(fazer)

            with open('Files/todos.txt',"w") as arquivo:
                arquivo.writelines(todo)
                
        #Metodo para ler o arquivo de Texto e armazenar em uma variavel.
            #arq_lista = open('Files/todos.txt', 'r')
            #todo = arq_lista.readlines()
            #arq_lista.close()                      
        #Metodo para escrever dentro do arquivo de Texto e atualizar dentro da Variavel
            #arq_lista = open('Files/todos.txt','w')
            #todo = arq_lista.writelines(todo)
            #arq_lista.close()    
        case "Editar":
            posicao = (int(input("Numero que ira editar em Todo: ")))
            posicao = posicao - 1
                      

            with open('Files/todos.txt','r') as arquivo:
                todo = arquivo.readlines()

            print("This is todos list: ", todo)

            

            with open('Files/todos.txt','w') as arquivo:
                todo = arquivo.writelines(todo)
            
            novo = input("Digite a nova todo: ")  
            todo[posicao] = novo


        case "Mostrar":
            with open('Files/todos.txt','r') as arquivo:
                todo = arquivo.readlines()
                        
            for i, item in enumerate(todo):
                item = item.strip() + '\n'
                row = f"{i + 1}-{item}"
                print(row)
            
        case "Excluir":

            posicao = (int(input("Numero que ira remover em Todo: ")))
            posicao = posicao -1

            with open('Files/todos.txt','r') as arquivo:
                todo = arquivo.readlines()
            todo.pop(posicao)

            with open('Files/todos.txt','w') as arquivo:
                todo = arquivo.writelines(todo)

        case "Sair":
            break