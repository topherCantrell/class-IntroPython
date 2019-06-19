class French:

    def __init__(self, target):
        self._target = target

    def say_hi(self):
        print('Le ', end='')
        self._target.say_hi()


class Canadian:

    def __init__(self, target):
        self._target = target

    def say_hi(self):
        self._target.say_hi()
        print('Eh?')

# Use inheritance sparingly. Instead of making FrenchDog and FrenchHuman
# and CanadianDog and FrenchCanadianDog ... just one decorator to apply
# to any animal.


import animals

# This is the DECORATOR design pattern. Decorating an object with another.
# Pass the "target" into the constructor. The book talks about this
# pattern and the terminology. Makes it easier for you to discuss as a
# team ... "we'll use the decorator pattern here and blah blah blah"

dog = French(animals.Dog())
human = French(Canadian(animals.Human()))

print('---')

dog.say_hi()
human.say_hi()