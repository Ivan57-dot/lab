import PySimpleGUI as sg
from snake import Game, GameOver

CELL, SIZE = 25, 20
W = CELL * SIZE

layout = [
    [sg.Graph((W, W), (0, W), (W, 0), background_color='black', key='-G-',
              enable_events=True, drag_submits=False)],
    [sg.Text('Score: 0', key='-S-')],
    [sg.Button('Exit')]
]

window = sg.Window('Snake', layout, finalize=True)
graph = window['-G-']
game = Game()

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
    
    if event == 'Up' or event == 'w':
        game.change_dir(0, -1)
    elif event == 'Down' or event == 's':
        game.change_dir(0, 1)
    elif event == 'Left' or event == 'a':
        game.change_dir(-1, 0)
    elif event == 'Right' or event == 'd':
        game.change_dir(1, 0)
    
    try:
        game.update()
        draw()
    except GameOver:
        graph.draw_text(f'Game Over!\nScore: {game.score}', (W//2, W//2), color='white')
        window.read()
        break

window.close()