import PySimpleGUI as sg

layout = [
    [
        sg.Input(key = '-INPUT-'),
        sg.Spin(['km ne milje', 'kg ne pound', 'sec ne min'], key = '-UNITS-'),
        sg.Button('Konverto', key = '-CONVERT-')
    ],
    [sg.Text('Rezultati', key = '-OUTPUT-')]
]
window = sg.Window('Konvertuesi', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km ne milje':
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f'{input_value} Km jane {output} Milje'
                case 'kg ne pound':
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f'{input_value} Kg jane {output} Pound'
                case 'sec ne min':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} sec jane {output} Minuta'

            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Futni nje numer')

window.close()