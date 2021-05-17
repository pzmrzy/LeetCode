from collections import deque
class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.snake = deque([(0, 0)])
        self.food = deque(food)
        self.width = width
        self.height = height
        self.dir = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        new = [self.snake[0][0] + self.dir[direction][0], self.snake[0][1] + self.dir[direction][1]]
        if new[0] < 0 or new[0] >= self.height or new[1] < 0 or new[1] >= self.width or (new in self.snake and new != self.snake[-1]):
            return -1
        if self.food and new == self.food[0]:
            self.snake.appendleft(new)
            self.food.popleft()
        else:
            self.snake.appendleft(new)
            self.snake.pop()
        return len(self.snake) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
