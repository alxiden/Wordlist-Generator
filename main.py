import itertools
import bs4
import requests

class WordlistGenerator:
    def __init__(self, words, numbers, url, output_file="wordlist.txt"):
        self.words = [word.strip() for word in words.split(",")]
        self.url = url.strip() if url else None
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

    def url_to_word(self, url):
        try:
            response = requests.get(url)
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            soup = soup.get_text()
            words = set()
            for word in soup.split():
                if len(word.strip()) > 4:
                    words.add(word.strip())
            return list(words)
        except requests.RequestException as e:
            print(f"Error fetching URL: {e}")
            return []


    def apply_replacements(self, word):
        replaced_words = []
        for letter, symbol in self.replacements.items():
            if letter in word or letter.upper() in word:
                replaced_word = word.replace(letter, symbol).replace(letter.upper(), symbol)
                replaced_words.append(replaced_word)
        return replaced_words

    def generate_wordlist(self):
        combinations = []
        # Generate combinations of words and numbers
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

        # Generate combinations of two words capitalized
        for word1, word2 in itertools.permutations(self.words, 2):
            combined_variation = f"{word1.capitalize()}{word2.capitalize()}"
            combinations.append(combined_variation)
            combinations.extend(self.apply_replacements(combined_variation))

            # Add numbers to the end of the combined words
            for number in self.numbers:
                combined_with_number = f"{combined_variation}{number}"
                combinations.append(combined_with_number)
                combinations.extend(self.apply_replacements(combined_with_number))



        # Write all combinations to the output file
        with open(self.output_file, "w", encoding="utf-8") as file:
            file.write("\n".join(combinations))
    
    def main(self):
        if self.url:
            words_from_url = self.url_to_word(url)
            if words_from_url:
                self.words.extend(words_from_url)
        self.generate_wordlist()
        print(f"Wordlist generated and saved to {self.output_file}.")


if __name__ == "__main__":
    words = input("Enter words separated by commas: ")
    numbers = input("Enter numbers separated by commas: ")
    url = input("Enter URL (optional): ")
    output_file = input("Enter output file name (default: wordlist.txt): ") or "wordlist.txt"
    generator = WordlistGenerator(words, numbers, url, output_file)
    generator.main()