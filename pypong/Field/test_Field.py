from Field.Field import Field 

DEFAULT_WIDTH = 100
DEFAULT_HEIGHT = 100 
DEFAULT_COLOR = "black"
DEFAULT_PAD_WIDTH = 4


def _build_default_field():
    return Field(DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_COLOR, DEFAULT_PAD_WIDTH)


def test_get_width():
    field = _build_default_field()
    assert field.width() == DEFAULT_WIDTH

def test_get_height():
    field = _build_default_field()
    assert field.height() == DEFAULT_HEIGHT

def test_get_color():
    field = _build_default_field()
    assert field.color() == DEFAULT_COLOR

def test_hits_top():
    field = _build_default_field()
    assert field.hits_top(-1) == True 
    assert field.hits_top(0) == True
    assert field.hits_top(1) == False

def test_hits_bottom():
    field = _build_default_field()
    assert field.hits_bottom(DEFAULT_HEIGHT-1) == False
    assert field.hits_bottom(DEFAULT_HEIGHT) == True
    assert field.hits_bottom(DEFAULT_HEIGHT+1) == True

def test_hits_left_goal_area():
    field = _build_default_field()
    assert field.hits_left_goal_area(DEFAULT_PAD_WIDTH-1) == True
    assert field.hits_left_goal_area(DEFAULT_PAD_WIDTH) == True
    assert field.hits_left_goal_area(DEFAULT_PAD_WIDTH+1) == False

def test_hits_right_goal_area():
    field = _build_default_field()
    assert field.hits_right_goal_area(DEFAULT_WIDTH-DEFAULT_PAD_WIDTH+1) == True
    assert field.hits_right_goal_area(DEFAULT_WIDTH-DEFAULT_PAD_WIDTH) == True
    assert field.hits_right_goal_area(DEFAULT_WIDTH-DEFAULT_PAD_WIDTH-1) == False
