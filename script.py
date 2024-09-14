import base64

with open("pac_decoded.txt", "rb") as f:
    file_content = f.read()

encoded_content = base64.b64encode(file_content).decode("utf-8")

lines = [encoded_content[i:i+64] for i in range(0, len(encoded_content), 64)]

with open("pac.txt", "w") as f:
    f.write("\n".join(lines))

