import random

class Game:
    def __init__(self, difficulty=100):
        self.difficulty = difficulty
        self.number = random.randint(1, self.difficulty)
        self.attempts = 0
        self.max_attempts = self.set_max_attempts()

    def set_max_attempts(self):
        return {50: 7, 100: 10, 1000: 15}.get(self.difficulty, 10)
    
    def check_guess(self, guess):
        self.attempts += 1
        if guess < self.number:
            return 'Слишком мало!'
        elif guess > self.number:
            return 'Слишком много!'
        else:
            return 'Поздравляю! Вы угадали число!'

class Player:
    @staticmethod
    def get_guess():
        while True:
            try:
                return int(input('Введите число: '))
            except ValueError:
                print('Пожалуйста, введите целое число.')


def play_game():
    while True:
        difficulty = int(input('Выберите уровень сложности (10, 50, 100): '))
        game = Game(difficulty)
        print(f'Я загадал число от 1 до {difficulty}. Попробeйте угадать!')

        while game.attempts < game.max_attempts:
            guess = Player.get_guess()
            result = game.check_guess(guess)
            print(result)

            if result == 'Поздравляю! Вы угадали число!':
                print(f'Вы справились за {game.attempts} попыток.')
                break
        else:
            print(f'Вы исчерпали попытки. Загаданное число было {game.number}.')
        
        again = input('Хотите сыграть снова? (да/нет): ').lower()
        if again != 'да':
            break

if __name__ == '__main__':
    play_game()
