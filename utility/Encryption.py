
def xor_encrypt_file(input_path, output_path, password):
    """
    Copy the file located at input_path and encrypt it at the adress
    output_path, based on the password.

    To use:

    xor_encrypt_file(input_path, output_path, password)




    To decrypt it, you just need to run it again
    """

    password_bytes = password.encode()

    with open(input_path, "rb") as f:
        data = f.read()

    encrypted = bytearray()

    for i, byte in enumerate(data):
        key_byte = password_bytes[i % len(password_bytes)]
        encrypted.append(byte ^ key_byte)

    with open(output_path, "wb") as f:
        f.write(encrypted)

    print("Done encrypting")


def encrypt_local( path, password):
    """
    This function takes a path to file and encrypt the file.

    TO USE:
    encruypt_local(path, password)
    """
    xor_encrypt_file(path, path, password)



def decrypt_local(path, password):
    """
    This function takes a path to a encrypted file and decrypt it.

    To USE:
    decrypt_local(path, password)  
    """
    xor_encrypt_file(path,path,password)



    
    

