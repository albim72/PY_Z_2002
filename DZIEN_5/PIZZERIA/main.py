from margaritabulder import MargaritaBuilder
from creamybaconbuilder import CreamyBaconBuilder
from waiter import Waiter




def validate_style(builders):
    try:
        input_msg = 'Jaką Pizzę wyboerasz, [m]argarita czy [c]reamy bacon? '
        pizza_style = input(input_msg)
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError:
        error_msg = 'Sorry, tylko [m]argarita czy [c]reamy bacon są dziś dostępne...'
        print(error_msg)
        return (False,None)
    return (True,builder)


def main():
    builders = dict(m=MargaritaBuilder,c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input,builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print(f'Ciesz się swoją pizzą, Smacznego!')

if __name__ == '__main__':
    main()
