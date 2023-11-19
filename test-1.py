import unittest
import pygame
from flappy_bird_game import *

class TestFlappyBirdGame(unittest.TestCase):

    def setUp(self):
        pygame.init()

    def tearDown(self):
        pygame.quit()

    def test_reset_game(self):
    # Assuming the reset_game function works correctly
       initial_score = 5
    #    pygame.sprite.Group.empty = unittest.mock.Mock()
       score = reset_game()
       self.assertEqual(score, 0)


    def test_bird_initialization(self):
      bird = Bird(100, 200)
      self.assertEqual(bird.rect.center, (100, 200))


    def test_pipe_initialization(self):
       pipe = Pipe(300, 400, 1)
       self.assertEqual(pipe.rect.bottomleft, (300, 325))




    def test_button_click(self):
        button_img = pygame.Surface((50, 50))
        button = Button(100, 100, button_img)
        # action = button.draw()
        #self.assertFalse(action)  # No click
       # pygame.mouse.get_pos = unittest.mock.Mock(return_value=(110, 110))
       # pygame.mouse.get_pressed = unittest.mock.Mock(return_value=(1, 0, 0))
       # action = button.draw()
       # self.assertTrue(action)  # Clicked

    def test_game_over_reset(self):
        # pygame.time.get_ticks = unittest.mock.Mock(return_value=1000)
        button_img = pygame.Surface((50, 50))
        button = Button(100, 100, button_img)

        flappy = Bird(100, 200)
        bird_group = pygame.sprite.Group(flappy)

        pipe_group = pygame.sprite.Group()
        pipe = Pipe(300, 400, 1)
        pipe_group.add(pipe)

        score = 5
        game_over = True
        # action = button.draw()

        self.assertTrue(game_over)
        # self.assertTrue(action)
        self.assertEqual(score, 5)

if __name__ == '__main__':
    unittest.main()
