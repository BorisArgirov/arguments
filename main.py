# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting_template = "Hello, <name>!"):
    return greeting_template.replace('<name>', name)
print(greet('Bob'))
print(greet('Bob', "What's up, <name>!"))


def force(mass, body='earth'):
    gravity_factors = {
        'sun': 274.0,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6,
    }
    
    if body not in gravity_factors:
        raise ValueError(f"Unknown celestial body '{body}'")
    
    g = round(gravity_factors[body], 1)
    f = round(mass * g, 1)
    return f
print(force(75.0, 'mars'))

def pull(m1, m2, d):
    f = (6.674 * 10**-11) * (m1 * m2 / d**2)
    return f
print(pull(500, 600, 5)) 
