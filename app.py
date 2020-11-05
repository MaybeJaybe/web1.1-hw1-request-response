
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():

    return 'Are you there, world? It\'s me, Ducky!'
# first example
@app.route('/penguin')
def penguin():

    return 'Penguins are cute!'
# favourite animal
@app.route('/animal/<users_animal>')
def favourite_animal(users_animal):

    return f'Wow, {users_animal} is my favourite animal, too!'
# favourite dessert
@app.route('/dessert/<users_dessert>')
def favourite_dessert(users_dessert):
    
    return f'How did you know I liked {users_dessert}?'
# super duper mad lib
@app.route('/madlibs/<adjective>/<noun>')
def madlib(adjective, noun):
    
    return f'I tried to make this {adjective} soup once using {noun}, because its the best thing ever and i wanted to eat it. {noun} soup isnt as {adjective} as i thought, after all.' 
# multiplication
@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() == True and number2.isdigit() == True:
        num1 = int(number1)
        num2 = int(number2)
        result = num1 * num2
        return f'{num1} multiplied by {num2} is {result}.'
    else:
        return 'Invalid inputs. Try again by entering two numbers.'


if __name__ == '__main__':
    app.run(debug=True)