from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from wa_query import get_imgs

def solve(inp, wa, container):
    if inp == '':
        ui.notify('Input cannot be empty!')

    else :
        container.clear()

        #
        #TODO: MODEL PIPELINE GOES HERE
        #

        if not wa:
            with container:
                ui.separator()
                ui.label('Input: ' + inp)
                ui.separator()
            ui.notify('Show result from model')            

        else:
            with container:
                ui.separator()
                ui.label('Input: ' + inp)
                for images in get_imgs(inp) :
                    ui.image(images).classes('w-96')
                    #ui.image('https://www6b3.wolframalpha.com/Calculate/MSP/MSP30001h9ec521i502gd2800002b7f23ag77g3d859?MSPStoreType=image/gif&s=9').classes('w-96')

                ui.separator()

    return

def main():
    ui.markdown('''# Math Sage
                
    Mathematical Word Problem Solving with NLP''')
    
    #ANSWERS GO HERE
    #ui.image('https://www6b3.wolframalpha.com/Calculate/MSP/MSP30001h9ec521i502gd2800002b7f23ag77g3d859?MSPStoreType=image/gif&s=9')

    with ui.row():
        input = ui.input('Text input')
        use_wa = ui.switch('Wolfram Alpha Computation')
    
    ui.button('Solve', on_click=lambda: solve(input.value, use_wa.value, res_container))

    res_container = ui.column()

    ui.markdown('Connor Dunlop, Jin-sol Jung, Jackson Livanec, Lemara Williams')
    ui.link('Source Code', 'https://github.com/jinzzasol/Mathsage').classes('mt-8')
    ui.run()


main()