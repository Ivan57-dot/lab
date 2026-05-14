import PySimpleGUI as sg
from snake import Game, GameOver

CELL, SIZE = 25, 20
W = CELL * SIZE

layout = [
    [sg.Graph((W, W), (0, W), (W, 0), background_color='black', key='-G-')],
    [sg.Text('Score: 0', key='-S-')],
    [sg.Button('Exit')]
]

window = sg.Window('Snake', layout, finalize=True)
graph = window['-G-']

# ВАЖНО: Устанавливаем фокус на окно
window.force_focus()

game = Game()

# Привязываем клавиши напрямую через tkinter
tk_window = window.TKroot
tk_window.bind('<Up>', lambda e: game.change_dir(0, -1))
tk_window.bind('<Down>', lambda e: game.change_dir(0, 1))
tk_window.bind('<Left>', lambda e: game.change_dir(-1, 0))
tk_window.bind('<Right>', lambda e: game.change_dir(1, 0))
# Добавляем WASD
tk_window.bind('<w>', lambda e: game.change_dir(0, -1))
tk_window.bind('<s>', lambda e: game.change_dir(0, 1))
tk_window.bind('<a>', lambda e: game.change_dir(-1, 0))
tk_window.bind('<d>', lambda e: game.change_dir(1, 0))

def draw():
    graph.erase()
    for i, (x, y) in enumerate(game.snake.body):
        graph.draw_rectangle((x*CELL, y*CELL), ((x+1)*CELL, (y+1)*CELL), 
                            fill_color='green' if i else 'darkgreen')
    f = game.food
    graph.draw_rectangle((f.x*CELL, f.y*CELL), ((f.x+1)*CELL, (f.y+1)*CELL), fill_color='red')
    window['-S-'].update(f'Score: {game.score}')

while True:
    event, _ = window.read(timeout=100)
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    try:
        game.update()
        draw()
    except GameOver:
        graph.draw_text(f'Game Over!\nScore: {game.score}', (W//2, W//2), color='white')
        window.read()
        break

window.close()