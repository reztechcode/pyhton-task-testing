import PySimpleGUI as tampilan

# Fungsi untuk menghitung operasi matematika
def Hitung(isi):
    try:
        hasil = eval(isi['input'])
        window['input'].update(hasil)
    except Exception as e:
        window['output'].update("Error")
        
if __name__ =='__main__':
    
    # Layout dari aplikasi kalkulator
    tampilan.theme('Pink')
    layout = [
        [tampilan.InputText('', size=(21, 1), key='input', disabled=True, disabled_readonly_text_color='Black',justification='right')],
        [tampilan.Button('/', size=(2, 1), font='Consolas'), tampilan.Button('1', size=(2, 1), font='Consolas'),
         tampilan.Button('2', size=(2, 1), font='Consolas'), tampilan.Button('3', size=(2, 1), font='Consolas')],
        [tampilan.Button('*', size=(2, 1), font='Consolas'), tampilan.Button('4', size=(2, 1), font='Consolas'),
         tampilan.Button('5', size=(2, 1), font='Consolas'), tampilan.Button('6', size=(2, 1), font='Consolas')],
        [tampilan.Button('-', size=(2, 1), font='Consolas'), tampilan.Button('7', size=(2, 1), font='Consolas'),
         tampilan.Button('8', size=(2, 1), font='Consolas'), tampilan.Button('9', size=(2, 1), font='Consolas')],
        [tampilan.Button('.', size=(2, 1), font='Consolas'), tampilan.Button('+', size=(2, 1), font='Consolas'),
         tampilan.Button('0', size=(2, 1), font='Consolas'), tampilan.Button('C', size=(2, 1), font='Consolas')],
        [tampilan.Button('=', size=(18, 1), bind_return_key=True)]
    ]
    
    # Membuat window dari Input
    window = tampilan.Window('', layout)
    
    # Tombol loop untuk membaca input dari luar
    while True:
        tombol, isi = window.read()
        
        if tombol == tampilan.WIN_CLOSED:
            break
        if tombol in '1234567890.+-*/C':
            if tombol == 'C':
                window['input'].update('')
            else:
                window['input'].update(isi['input'] + tombol)
        if tombol == '=':
            Hitung(isi)
            
    window.close()
