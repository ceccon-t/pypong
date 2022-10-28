try:  # Python 3
    from Strategy.Strategy import Strategy, PLAYER_ONE, PLAYER_TWO
except ImportError:  # Python 2
    from Strategy import Strategy, PLAYER_ONE, PLAYER_TWO


SIMPLE_COMPUTER_PLAYER_SPEED = 0.6

class StrategySimpleComputerPlayer(Strategy):

    def decide_acceleration_factor(self, game_state):
        paddle = self._get_player_paddle(game_state)
        paddle_pos = paddle.pos()
        decision = 0
        ball_pos = [game_state.ball.pos(game_state.coord_x_universal_id), game_state.ball.pos(game_state.coord_y_universal_id)]
        ball_vel = [game_state.ball.vel(game_state.coord_x_universal_id), game_state.ball.vel(game_state.coord_y_universal_id)]
        X = 0
        Y = 1

        if self._ball_is_coming(ball_vel[X]):

            if self._ball_is_escaping_from_center(paddle_pos, ball_pos[Y], ball_vel[Y]):
                decision = self._move_down()
                if ball_vel[Y] < 0:  # factor must match direction of ball movement
                    decision = self._move_up()
            
            # panic mode (when ball is close enough always attempt to match it)
            elif self._ball_is_really_close(ball_pos[X], game_state):
                if self._ball_is_down(ball_pos[Y], paddle_pos, game_state):
                    decision = self._move_down()
                elif self._ball_is_up(ball_pos[Y], paddle_pos, game_state):
                    decision = self._move_up()
        
        return decision

    def _move_up(self):
        return -SIMPLE_COMPUTER_PLAYER_SPEED
    
    def _move_down(self):
        return SIMPLE_COMPUTER_PLAYER_SPEED

    def _get_player_paddle(self, game_state):
        paddle = None 
        if self.player_number == PLAYER_ONE:
            paddle = game_state.player_one.paddle()
        else:
            paddle = game_state.player_two.paddle()
        return paddle

    def _ball_is_coming(self, ball_x_vel):
        if self.player_number == PLAYER_ONE:
            return ball_x_vel < 0  # ball moving to the left
        else:
            return ball_x_vel > 0  # ball moving to the right

    def _ball_is_up(self, ball_y_pos, paddle_pos, game_state):
        paddle_half_height = game_state.paddle_height / 2
        return ball_y_pos < (paddle_pos - paddle_half_height)

    def _ball_is_down(self, ball_y_pos, paddle_pos, game_state):
        paddle_half_height = game_state.paddle_height / 2
        return ball_y_pos > (paddle_pos + paddle_half_height)

    def _ball_is_escaping_from_center(self, paddle_pos, ball_y_pos, ball_y_vel):
        is_up_and_upward = ball_y_pos < paddle_pos and ball_y_vel < 0
        is_down_and_downward = ball_y_pos > paddle_pos and ball_y_vel > 0
        return is_up_and_upward or is_down_and_downward

    def _ball_is_really_close(self, ball_x_pos, game_state):
        is_it = False
        if self.player_number == PLAYER_ONE:
            threshold = game_state.field_width * 1 / 4  # a quarter of the field away
            if ball_x_pos < threshold:
                is_it = True
        else:
            threshold = game_state.field_width * 3 / 4  # a quarter of the field away
            if ball_x_pos > threshold:
                is_it = True
        return is_it
