import argparse
import random

def main():
    parser = argparse.ArgumentParser(description='Generate a joke.')
    parser.add_argument('--type', choices=['pun', 'knock-knock', 'one-liner'], default='pun',
                        help='Type of joke (default: pun)')
    parser.add_argument('--length', choices=['short', 'medium', 'long'], default='short',
                        help='Length of the joke (default: short)')
    parser.add_argument('--audience', choices=['kids', 'adults', 'tech-savvy'], default='adults',
                        help='Intended audience (default: adults)')

    args = parser.parse_args()

    # Predefined jokes database
    jokes = {
        'pun': {
            'short': {
                'kids': [
                    'Why did the teddy bear say no to dessert? Because she was stuffed.',
                ],
                'adults': [
                    'I used to play piano by ear, now I use my hands.',
                ],
                'tech-savvy': [
                    'Why do programmers prefer dark mode? Because light attracts bugs.',
                ],
            },
            'medium': {
                'kids': [
                    'I would tell you a construction pun, but I\'m still working on it.',
                ],
                'adults': [
                    'The future, the present, and the past walked into a bar. Things got a little tense.',
                ],
                'tech-savvy': [
                    'Debugging: Removing the needles from the haystack.',
                ],
            },
            'long': {
                'kids': [
                    'Did you hear about the mathematician who’s afraid of negative numbers? He will stop at nothing to avoid them.',
                ],
                'adults': [
                    'I have a joke about time travel, but I’m not gonna share it. You guys didn’t like it.',
                ],
                'tech-savvy': [
                    'There are only 10 types of people in the world: those who understand binary and those who don\'t.',
                ],
            },
        },
        'knock-knock': {
            'short': {
                'kids': [
                    'Knock knock.\nWho’s there?\nBoo.\nBoo who?\nDon’t cry, it’s just a joke.',
                ],
                'adults': [
                    'Knock knock.\nWho’s there?\nCanoe.\nCanoe who?\nCanoe come out tonight?',
                ],
                'tech-savvy': [
                    'Knock knock.\nWho’s there?\nCache.\nCache who?\nBless you!',
                ],
            },
            'medium': { ... },  # Additional jokes can be added here
            'long': { ... },
        },
        'one-liner': {
            'short': {
                'kids': [
                    'Why did the computer go to the doctor? Because it had a virus!',
                ],
                'adults': [
                    'I’m reading a book on anti-gravity. It’s impossible to put down.',
                ],
                'tech-savvy': [
                    'I would tell you a UDP joke, but you might not get it.',
                ],
            },
            'medium': { ... },
            'long': { ... },
        },
    }

    # Retrieve jokes based on user input
    selected_jokes = jokes.get(args.type, {}).get(args.length, {}).get(args.audience, [])
    if selected_jokes:
        print(random.choice(selected_jokes))
    else:
        print('No joke found for the given criteria.')

if __name__ == '__main__':
    main()
