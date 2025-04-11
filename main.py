import itertools

class WordlistGenerator:
    def __init__(self, words, numbers, output_file="wordlist.txt"):
        self.words = [word.strip() for word in words.split(",")]
        self.numbers = [number.strip() for number in numbers.split(",")]
        self.output_file = output_file
        self.replacements = {
            "a": "@",
            "e": "3",
            "i": "1",
            "o": "0",
            "s": "$",
            "l": "1",
            "t": "7"
        }

    def apply_replacements(self, word):
        replaced_words = []
        for letter, symbol in self.replacements.items():
            if letter in word or letter.upper() in word:
                # Replace only the first occurrence of the letter
                replaced_word = word.replace(letter, symbol).replace(letter.upper(), symbol)
                replaced_words.append(replaced_word)
        return replaced_words

    def generate_wordlist(self):
        combinations = []
        for word, number in itertools.product(self.words, self.numbers):
            variations = [
                f"{word.capitalize()}{number}",
                f"{word}{number}",
                f"{word.upper()}{number}",
                f"{word.lower()}{number}",
                f"{number}{word.capitalize()}",
                f"{number}{word}",
                f"{number}{word.upper()}",
                f"{number}{word.lower()}",
                f"{word.capitalize()}{number}!",
                f"{word}{number}!",
                f"{word.upper()}{number}!",
                f"{word.lower()}{number}!",
                f"{number}{word.capitalize()}!",
                f"{number}{word}!",
                f"{number}{word.upper()}!",
                f"{number}{word.lower()}!",
                f"{word.capitalize()}-{number}",
                f"{word}-{number}",
                f"{word.upper()}-{number}",
                f"{word.lower()}-{number}",
                f"{number}-{word.capitalize()}",
                f"{number}-{word}",
                f"{number}-{word.upper()}",
                f"{number}-{word.lower()}"
            ]
            combinations.extend(variations)
            for variation in variations:
                combinations.extend(self.apply_replacements(variation)) 

        with open(self.output_file, "w") as file:
            file.write("\n".join(combinations))


if __name__ == "__main__":
    words = input("Enter words separated by commas: ")
    numbers = input("Enter numbers separated by commas: ")
    generator = WordlistGenerator(words, numbers)
    generator.generate_wordlist()