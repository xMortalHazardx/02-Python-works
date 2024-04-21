import PySimpleGUI as sg
import functions

label = sg.Text("Digite a To-Do:")

"""tootip é quando o mouse fica sobre o elemento, key ele identifica a chave do diciona
rio"""

input_box = sg.InputText(tooltip="Digite Algo: ", key='todo')
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                    layout=[[label, ], [input_box, add_button]],                    
                    font=('Helvetica', 15))

while True:
    
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            """Nessa variavel new_todo estamos chamando a key do dicionario values
            que é todo e adicionando somente o valor dentro da variavel new_todo"""
            new_todo = values['todo']
            todos.append(new_todo+"\n")
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()