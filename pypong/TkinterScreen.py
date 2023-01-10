try:  # Python 3
    from tkinter import *  
except ImportError:
    try:  # Python 2
        from Tkinter import *  
    except ImportError:  # Tkinter not installed...
        raise ImportError("This program requires Tkinter, please make sure you have it installed.")


from GameConstants import *


TK_KEY_ID_GENERIC_KEY = '<Key>'
TK_KEY_ID_SPACE = '<space>'
TK_KEY_ID_ESCAPE = '<Escape>'


class TkinterScreen:

    def __init__(self, gameloop_fn, field, paddle_height, paddle_width, player_one_color, player_two_color):
        self._root_element = self._build_root_element()

        self._gameloop_callback = gameloop_fn

        self._field = field 
        self._width = field.width()
        self._height = field.height()
        self._paddle_heigth = paddle_height
        self._paddle_width = paddle_width
        self._player_one_color = player_one_color
        self._player_two_color = player_two_color

        self._canvas = Canvas(self._root_element, width=self._width, height=self._height, bg=field.color())
        self._canvas.pack()

        self._ball = None 
        self._paddle_left = None
        self._paddle_right = None
        self._instructions_display = self._create_instructions_message_display()
        self._score_left = self._create_score_left_display()
        self._score_right = self._create_score_right_display() 

        self._draw_field_lines()

    def bind_key(self, key_id, callback_fun):
        self._root_element.bind(key_id, callback_fun)

    def start_game(self):
        self._gameloop()
        self._root_element.mainloop()

    def quit_game(self):
        self._root_element.destroy()

    def set_instructions_message(self, message):
        self._canvas.itemconfigure(self._instructions_display, text=message)

    def draw_score_left(self, score, color):
        self._canvas.itemconfigure(self._score_left, text=str(score), fill=color)

    def draw_score_right(self, score, color):
        self._canvas.itemconfigure(self._score_right, text=str(score), fill=color)

    def create_ball_object(self, ball, ball_color):
        self._ball = self._canvas.create_oval(ball.leftmost(), ball.topmost(), ball.rightmost(), ball.bottommost(), fill=ball_color)

    def create_left_paddle_object(self, paddle):
        half_pad_width = self._paddle_width / 2 
        half_pad_height = self._paddle_heigth / 2
        pos = paddle.pos()
        self._paddle_left = self._canvas.create_line(half_pad_width, pos - half_pad_height, half_pad_width, pos + half_pad_height, fill=self._player_one_color, width=self._paddle_width)

    def create_right_paddle_object(self, paddle):
        half_pad_width = self._paddle_width / 2 
        half_pad_height = self._paddle_heigth / 2
        pos = paddle.pos()
        self._paddle_right = self._canvas.create_line(self._width - half_pad_width, pos - half_pad_height, self._width - half_pad_width, pos + half_pad_height, fill=self._player_two_color, width=self._paddle_width)

    def draw_ball(self, ball):
        self._canvas.coords(self._ball, ball.leftmost(), ball.topmost(), ball.rightmost(), ball.bottommost())

    def draw_left_paddle(self, paddle):
        half_pad_width = self._paddle_width / 2
        self._canvas.coords(self._paddle_left, half_pad_width, paddle.topmost(), half_pad_width, paddle.bottommost())

    def draw_right_paddle(self, paddle):
        half_pad_width = self._paddle_width / 2
        self._canvas.coords(self._paddle_right, self._width - half_pad_width, paddle.topmost(), self._width - half_pad_width, paddle.bottommost())

    def _build_root_element(self):
        root = Tk()
        root.title(GAME_TITLE)

        # place game window in a nice position on screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry("+" + str(screen_width // 4) + "+" + str(screen_height // 4))  # using only offsets from left and top

        return root

    def _gameloop(self):
        self._root_element.after(1000 // 60, self._gameloop)
        self._gameloop_callback()

    def _draw_field_lines(self):
        width = self._width
        height = self._height
        color_lines = self._field.color_lines()
        goal_line_offset = self._field.goal_line_offset()
        self._canvas.create_line(width / 2, 0, width / 2, height, fill=color_lines)
        self._canvas.create_line(goal_line_offset, 0, goal_line_offset, height, fill=color_lines)
        self._canvas.create_line(width - goal_line_offset, 0, width - goal_line_offset, height, fill=color_lines)

    def _create_instructions_message_display(self):
        # TODO: Refactor font definition to centralized place
        return self._canvas.create_text(self._width / 4, self._height - 25, text="", fill="white", font=('Helvetica', '10'))

    def _create_score_display(self, x, y):
        # TODO: Refactor font definition to centralized place
        return self._canvas.create_text(x, y, text="0", font=('Helvetica', '30'))

    def _create_score_left_display(self):
        return self._create_score_display(self._width / 4, self._height / 4)

    def _create_score_right_display(self):
        return self._create_score_display(self._width * 3 / 4, self._height / 4)

