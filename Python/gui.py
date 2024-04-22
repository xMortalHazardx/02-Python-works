import PySimpleGUI as sg
import functions

label = sg.Text("Digite a To-Do:")

"""tootip é quando o mouse fica sobre o elemento, key ele identifica a chave do diciona
rio"""

input_box = sg.InputText(tooltip="Digite Algo: ", key='todo')
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=[40, 15])

edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                    layout=[[label, ], [input_box, add_button],
                             [list_box, edit_button]],                    
                    font=('Helvetica', 15))

while True:
    
    event, values = window.read()
    print(1,event)
    print(2,values)
    print(3,values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            """Nessa variavel new_todo estamos chamando a key do dicionario values
            que é todo e adicionando somente o valor dentro da variavel new_todo"""
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_editar = values['todos'][0]
            novo_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_editar)
            todos[index] = novo_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()