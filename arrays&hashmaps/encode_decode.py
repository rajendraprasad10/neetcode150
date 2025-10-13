class Codec:
    # Encodes a list of strings to a single string.
    def encode(self, strs):
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s   # length#string
        return encoded

    # Decodes a single string to a list of strings.
    def decode(self, s):
        res = []
        i = 0

        while i < len(s):
            # 1️⃣ Find the position of '#'
            j = i
            while s[j] != '#':
                j += 1

            # 2️⃣ Extract length
            length = int(s[i:j])

            # 3️⃣ Extract the actual string using the length
            string = s[j+1 : j+1+length]
            res.append(string)

            # 4️⃣ Move i to the next encoded block
            i = j + 1 + length

        return res


# Example test
codec = Codec()
data = ["neet","code","","you"]
encoded = codec.encode(data)
print("Encoded:", encoded)
decoded = codec.decode(encoded)
print("Decoded:", decoded)
