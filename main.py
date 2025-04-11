import itertools

class WordlistGenerator:
    def __init__(self, words, numbers, output_file="wordlist.txt"):
        self.words = [word.strip() for word in words.split(",")]
        self.numbers = [number.strip() for number in numbers.split(",")]
        self.output_file = output_file

    def generate_wordlist(self):
        combinations = []
        for word, number in itertools.product(self.words, self.numbers):
            combinations.append(f"{word.capitalize()}{number}")
            combinations.append(f"{word}{number}")
            combinations.append(f"{word.upper()}{number}")
            combinations.append(f"{word.lower()}{number}")

        with open(self.output_file, "w") as file:
            file.write("\n".join(combinations))

        print(f"Wordlist generated and saved to {self.output_file}")


if __name__ == "__main__":
    words = input("Enter words separated by commas: ")
    numbers = input("Enter numbers separated by commas: ")
    generator = WordlistGenerator(words, numbers)
    generator.generate_wordlist()