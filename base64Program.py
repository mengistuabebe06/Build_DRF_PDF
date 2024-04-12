import base64


class SaltedEncoder:
    def __init__(self, salt_key, salt_index):
        self.salt_key = salt_key
        self.salt_index = salt_index

    def encode(self, payload):
        salted_payload = f"{self.salt_key}{payload}{self.salt_index}"
        encoded_payload = base64.b64encode(salted_payload.encode()).decode()
        return encoded_payload

    def decode(self, encoded_payload):
        try:
            decoded_payload = base64.b64decode(encoded_payload).decode()
            if f"{self.salt_key}{self.salt_index}" in decoded_payload:
                original_payload = decoded_payload.replace(
                    f"{self.salt_key}{self.salt_index}", ""
                )
                return original_payload
            else:
                return None
        except Exception as e:
            print(f"Decoding error: {e}")
            return None


# Example usage
salt_key = "mysaltkey"
salt_index = 123
encoder = SaltedEncoder(salt_key, salt_index)

payload = "Hello, world!"
encoded_value = encoder.encode(payload)
print("Encoded value:", encoded_value)

decoded_value = encoder.decode(encoded_value)
if decoded_value:
    print("Decoded value:", decoded_value)
else:
    print("Decoding failed: Incorrect salt key or salt index.")
