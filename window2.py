import PySimpleGUI as sg
import mapgenerator as mpg
import time
import djikstra as dj
import bfs as bfs


def windownum2(source,destination):
    
    sg.theme('DarkTeal9')
    
    layout = [[sg.Text('Route Instructions')],
             [sg.Text('')],
             [sg.Text('Instruction Mode'),sg.Radio('Text Based','group1',key = 'text_opt'),sg.Radio('Graphical','group1',key = 'gui_opt1')],
             [sg.Text('Approach', size=(12,1)),sg.Radio('Djikstra Approach',1,key='dj'),sg.Radio('Breadth First Approach',1,key='bfs')],
             [sg.Text('')],
             [sg.Text('Display: '),sg.Text(size=(100,1), justification='left',key='Display')],
             [sg.Text('Display: '),sg.Text(size=(100,1), justification='left',key='Display1')],
             [sg.Text('')],
             [sg.Text('')],
             [sg.Submit(),sg.Exit()],
             
             ]

    window2 = sg.Window("GIKI NAVIGATOR",layout,size = (900,300)) #(length,height)
    
    while True:
        event, values = window2.read() #read all events and input values on window canva
        option1 = values['text_opt']
        option2 = values['gui_opt1']
        

        if event == sg.WIN_CLOSED or event == 'Exit':  #in case we cross the program or use exit button break
            break
        if event == 'Submit': #in case we use submit button we print event and values

            if (option1 == True):

                if values['dj']:
                    tpl = dj.dijkstra(source,destination)
                    window2['Display'].update(tpl)
                    window2['Display1'].update(' ')

                elif values['bfs']:
                    bbffs,bbff = bfs.bfs(source,destination)
                    bbffs = round(bbffs)
                    window2['Display'].update(bbffs)
                    window2['Display1'].update(bbff)
            
            elif (option2 == True):
                mpg.generate_map(source,destination) #values passing for correct picture to be displayed
                time.sleep(4)
                mpg.open_map()
                break
            else:
                window2['Display'].update('Invalid Input!')
            
    window2.close()