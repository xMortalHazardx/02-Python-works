

def get_todos():
    with open('/home/machine/Documents/Python/Files/todos.txt','r') as arquivo:
        todo = arquivo.readlines()
    return todo 

while True:

    user_prompt = input("Entrada de fazer: ")
    user_prompt = user_prompt.strip()

    if user_prompt.startswith('Adicionar'):
        fazer = input("Enter a todo: ") + "\n"  

        todo = get_todos()
        todo.append(fazer)
    # Comando WITH mais resumido para abrir arquivos e salvar em uma variavel.
        #with open('Files/todos.txt','r') as arquivo:
        #    todo = arquivo.readlines()        

        with open('Files/todos.txt',"w") as arquivo:
            arquivo.writelines(todo)                
         
    elif user_prompt.startswith("Editar"):
        try: 
            posicao = (int(input("Numero que ira editar em Todo: ")))
            posicao = posicao - 1
                      
            todo = get_todos()
        # Comando WITH mais resumido para abrir arquivos e salvar em uma variavel.
        # with open('Files/todos.txt','r') as arquivo:
        # todo = arquivo.readlines() 

            print("This is todos list: ", todo)        
                      
            novo = input("Digite a nova todo: ")  
            todo[posicao] = novo + '\n'

            with open('Files/todos.txt','w') as arquivo:
                todo = arquivo.writelines(todo)
        except ValueError:
            print("Comando inválido.")
        # A função que recarrega o codigo ao representar um erro na tela do usuário 
            continue

    elif user_prompt.startswith("Mostrar"):
        # Comando WITH mais resumido para abrir arquivos e salvar em uma variavel.
        # with open('Files/todos.txt','r') as arquivo:
        # todo = arquivo.readlines() 
        todo = get_todos()   

        for i, item in enumerate(todo):
            item = item.strip() + '\n'
            row = f"{i + 1}-{item}"
            print(row)
            
    elif user_prompt.startswith("Remover"):
    
        posicao = (int(input("Numero que ira remover em Todo: ")))
        posicao = posicao -1
        todo = get_todos()
        # Comando WITH mais resumido para abrir arquivos e salvar em uma variavel.
        # with open('Files/todos.txt','r') as arquivo:
        # todo = arquivo.readlines() 
        todo.pop(posicao)

        with open('Files/todos.txt','w') as arquivo:
            todo = arquivo.writelines(todo)

    elif user_prompt.startswith("Sair"):
        break
    else:
         print("Comando inválido.")

print("Adeus!")