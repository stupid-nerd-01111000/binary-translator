# Binary Translator

This is a Python project that provides functionality to convert text to binary and binary to text. It includes a simple user interface via the command line, making it easy to use for basic translation tasks.

## Features
- **Text to Binary Conversion:** Input a text string, and get its binary representation.
- **Binary to Text Conversion:** Input a binary string, and get its corresponding text.
- Supports binary strings with or without spaces between 8-bit blocks.

## Requirements
- Python 3.6 or higher

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/binary-translator.git
   cd binary-translator
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. Follow the prompts:
   - Select an option (1 for Text to Binary, 2 for Binary to Text).
   - Enter the value to be converted.

### Example
#### Text to Binary:
```plaintext
1. text to binary
2. binary to text

Enter your choice (1 or 2): 1
Enter value: Hello
Binary: 01001000 01100101 01101100 01101100 01101111
```

#### Binary to Text:
```plaintext
1. text to binary
2. binary to text

Enter your choice (1 or 2): 2
Enter value: 01001000 01100101 01101100 01101100 01101111
Text: Hello
```

## Code
Here is the main script for the translator:
```python
class Translator:
    def text_to_binary(self, text_str):
        # Convert text to binary
        binary_result = ' '.join(format(ord(char), '08b') for char in text_str)
        return binary_result

    def binary_to_text(self, binary_str):
        # Remove spaces and convert binary to text
        binary_str = binary_str.replace(' ', '')  # Remove spaces
        bytes_list = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
        text_result = ''.join(chr(int(byte, 2)) for byte in bytes_list)
        return text_result

    def networker(self):
        # Prompt user for choice
        print('''
1. text to binary
2. binary to text
''')
        self.order = input('Enter your choice (1 or 2): ')
        self.value = input('Enter value: ')

        if self.order == '1':
            print("Binary:", self.text_to_binary(self.value))
        elif self.order == '2':
            try:
                print("Text:", self.binary_to_text(self.value))
            except ValueError:
                print("Invalid binary input. Please ensure the input is a valid binary string.")
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Create an instance and run the program
slow = Translator()
slow.networker()
```

## Contribution
Feel free to fork the repository and submit pull requests. Suggestions and bug reports are welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

