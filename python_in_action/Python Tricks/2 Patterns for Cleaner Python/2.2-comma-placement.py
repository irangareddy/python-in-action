"""2.2 Complacent Comma Placement"""

"""
Bad Practice
voice_assistants = ['Alexa', 'Siri', 'Bixby']

Good Practice - can easily identify changes in Git Diff
voice_assistants = [
    'Alexa',
    'Siri',
    'Bixby'
]
"""

# Adding name without comma placement
voice_assistants = [
    'Alexa',
    'Siri',
    'Bixby'
    'Ranga'
]
print(voice_assistants)

"""
Reason: String literal Concatenation
Multiple adjacent string or bytes literals (delimited by whitespace), 
possibly using different quoting conventions, are allowed, 
and their meaning is the same as their concatenation
"""

long_message = ('This is a super long string constant '
                'spread out across multiple lines. '
                'And look, no backslash characters needed!')

print(long_message)

# Fix for String literal Concatenation issue
voice_assistants = [
    'Alexa',
    'Siri',
    'Bixby',
    'Ranga'
]
print(voice_assistants)

# In Python, you can place a comma after every item in a list, dict, or set constant, including the last item.
# That way, you can just remember to always end your lines with a comma and thus avoid the comma placement
# juggling that would otherwise be required.
voice_assistants = [
    'Alexa',
    'Siri',
    'Bixby',
    'Ranga',
]
print(voice_assistants)

"""
Key Takeaways

* Smart formatting and comma placement can make your list, dict, or set constants easier to maintain.
* Python’s string literal concatenation feature can work to your benefit, or introduce hard-to-catch bugs.
"""
