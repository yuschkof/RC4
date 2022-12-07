class RC4:
    def __init__(self, key):
        self.key = key

    def ksa(self):
        key_b = [ord(c) for c in self.key]
        key_length = len(key_b)
        S = list(range(256))
        j = 0
        for i in range(256):
            j = (j + S[i] + key_b[i % key_length]) % 256
            S[i], S[j] = S[j], S[i]
        return S

    def prga(self, S, plaintext_length=0):
        if plaintext_length != 0:
            return prga_return(S, plaintext_length)
        else:
            K = prga_generator(S)
            return K

    def encrypt(self, plaintext, output_format='hex'):
        plaintext_b = [ord(c) for c in plaintext]
        keystroke = self.prga(self.ksa())
        keystroke_list = []
        if not (type(keystroke) is list):
            for i in range(len(plaintext_b)):
                keystroke_list.append(next(keystroke))
            keystroke = keystroke_list
        match output_format:
            case 'hex':
                return xor_bytes(plaintext_b, keystroke).hex()
            case 'bin':
                return xor_bytes(plaintext_b, keystroke)
            case 'unicode':
                ciphertext_b = xor_bytes(plaintext_b, keystroke)
                ciphertext_unicode = ''
                for b in ciphertext_b:
                    ciphertext_unicode += chr(b)
                return ciphertext_unicode
            case _:
                return xor_bytes(plaintext_b, keystroke).hex()

    def decrypt(self, ciphertext, output_format='unicode'):
        keystroke = self.prga(self.ksa())
        ciphertext_b = bytes.fromhex(ciphertext)
        plaintext_b = xor_bytes(ciphertext_b, keystroke)
        match output_format:
            case 'unicode':
                plaintext_unicode = ''
                for b in plaintext_b:
                    plaintext_unicode += chr(b)
                return plaintext_unicode
            case _:
                return [chr(b) for b in xor_bytes(ciphertext_b, keystroke)]


def prga_return(S, plaintext_length):
    i = j = 0
    K = []
    for n in range(plaintext_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K.append(S[(S[i] + S[j]) % 256])
    return K


def prga_generator(S):
    i = j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K


def xor_bytes(bytes1, bytes2):
    return bytes([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])
