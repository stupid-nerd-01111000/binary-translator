class Translator:
    def text_to_binary(self, text_str):
        binary_result = ' '.join(format(ord(char), '08b') for char in text_str)
        return binary_result

    def binary_to_text(self, binary_str):
        binary_str = binary_str.replace(' ', '')
        bytes_list = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
        text_result = ''.join(chr(int(byte, 2)) for byte in bytes_list)
        return text_result

    def networker(self):
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

slow = Translator()
slow.networker()
