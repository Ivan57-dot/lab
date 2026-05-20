import PySimpleGUI as sg
from snake import Game, GameOver, save_score

CELL, SIZE = 25, 20
W = CELL * SIZE

layout = [
    [sg.Graph(canvas_size=(W, W), graph_bottom_left=(0, W), graph_top_right=(W, 0), 
              background_color='black', key='-G-')],
    [sg.Text('Score: 0', key='-S-', text_color='white', background_color='black')],
    [sg.Button('Up'), sg.Button('Down'), sg.Button('Left'), sg.Button('Right')],
    [sg.Button('Exit')]
]

window = sg.Window('Snake', layout, finalize=True)
graph = window['-G-']
game = Game()

def draw():
    graph.erase()
    for i, (x, y) in enumerate(game.snake.body):
        color = '#2ecc71' if i == 0 else '#27ae60'
        graph.draw_rectangle((x*CELL, y*CELL), ((x+1)*CELL, (y+1)*CELL), fill_color=color)
    f = game.food
    graph.draw_rectangle((f.x*CELL, f.y*CELL), ((f.x+1)*CELL, (f.y+1)*CELL), fill_color='red')
    window['-S-'].update(f'Score: {game.score}')

while True:
    event, _ = window.read(timeout=100)
    
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    
    if event == 'Up':
        game.change_dir(0, -1)
    elif event == 'Down':
        game.change_dir(0, 1)
    elif event == 'Left':
        game.change_dir(-1, 0)
    elif event == 'Right':
        game.change_dir(1, 0)
    
    try:
        game.update()
        draw()
    except GameOver:
        save_score(game.score)
        graph.draw_text(f'Game Over!\nScore: {game.score}', 
                       (W//2, W//2), color='white', font=('Arial', 16))
        window.read(timeout=2000)
        break

window.close()