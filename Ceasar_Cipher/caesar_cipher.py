""""Keep your secrets as a Roman"""

def ceasar(origina_text, positions_shift, enconde_decode):
    """"Keep your secrets as a Roman"""

    alphabet = ['a','b','c','d','e',
                'f','g','h','i','j',
                'k','l','m','n','o',
                'p','q','r','s','t',
                'u','v','w','x','y','z']
    secret = list(origina_text)
    result = []
    if enconde_decode == 1:
        # Encrypting
        for i, secret in enumerate(secret):
            if secret not in alphabet:
                result.append(secret)
            else:
                result.append(alphabet[(alphabet.index(secret) + positions_shift) % len(alphabet)])
    if enconde_decode == -1:
        # Decrypting
        for i, secret in enumerate(secret):
            if secret not in alphabet:
                result.append(secret)
            else:
                result.append(alphabet[(alphabet.index(secret) - positions_shift) % len(alphabet)])
    return "".join(result)

if __name__ == '__main__':
 
    import art
    print(art.logo)

    while True:
        answer = input("What do you want to do?\n1- Encrypt text\n2- Decrypt text\nN - Exit\n")

        if answer == '1':
            txt = input("Text: ")
            try:
                shift = int(input("Key: "))
            except ValueError:
                print("Key must be a number.")
                continue
            print("Your secret is safe: ", ceasar(txt, shift, 1))

        elif answer == '2':
            txt = input("Text: ")
            try:
                shift = int(input("Key: "))
            except ValueError:
                print("Key must be a number.")
                continue
            print("Secret recovered: ", ceasar(txt, shift, -1))

        else:
            break

    print("\nMay Jupiter bless you!")
