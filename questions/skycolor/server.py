import random
import prairielearn as pl

class SkyColorQuestion:
    def generate(self):
        question = pl.Question()
        question.prompt = "What is the color of the sky?"
        
        choices = ["Blue", "Green", "Orange"]
        correct_answer = random.choice(choices)
        
        question.add_choice(correct_answer, True)
        choices.remove(correct_answer)
        
        for choice in choices:
            question.add_choice(choice, False)
        
        question.shuffle_choices()
        question.correct_answer = correct_answer
        
        return question
