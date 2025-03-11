from cipher.caesar import alphabet

class caesarcipher:
    def __init__(self):
        self.alphabet1 = alphabet
        
    def encrypt_text(self, text:str,key:int )->str:
        alphabet_len=len(self.alphabet1)
        text=text.upper()
        encrypted_text=[]
        for letter in text:
            letter_index=self.alphabet1.index(letter)
            output_index =(letter_index+key)%alphabet_len
            output_letter=self.alphabet1[output_index]
            encrypted_text.append(output_letter)
        return "".join(encrypted_text)
    
    def decrypt_text(self, text:str,key:int )->str:
        alphabet_len=len(self.alphabet1)
        text=text.upper()
        dencrypted_text=[]
        for letter in text:
            letter_index=self.alphabet1.index(letter)
            output_index =(letter_index-key)%alphabet_len
            output_letter=self.alphabet1[output_index]
            dencrypted_text.append(output_letter)
        return "".join(dencrypted_text)