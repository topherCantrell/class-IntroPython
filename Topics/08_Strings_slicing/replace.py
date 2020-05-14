a = 'Hello <<NAME>>. How are you <<NAME>>?'

b = a.replace('<<NAME>>','Chris')

print(b)

text = '''
From the "Best of Mad Libs" by Roger Price and Leonard Stern

LITTLE RED RIDING HOOD

One day, Little {color} Riding Hood was going through the forest carrying a
basket of {plural noun} for her grandmother. Suddenly, she met a big {adjective}
wolf. 

"{exclamation}!" said the wolf. "Where are you going, little {silly word}?"

"I\'m going to my grandmother\'s house," she said. 

Then the wolf {verb (past tense)} away. When Miss Riding Hood got to her 
grandmother\'s house, the wolf was in bed dressed like her grandmother. 

"My, Grandmother," she said. "What big {plural noun 1} you have." 

"The better to {verb 1} you with," said the wolf. 

"And, Grandmother," she said, "what big {plural noun 2} you have." 

The wolf said, "The better to {verb 2} you with." 

And then she said, "What big {plural noun 3} you have, Grandmother." 

But the wolf said nothing. He had just died of indigestion from eating Grandmother.'''

print(text)