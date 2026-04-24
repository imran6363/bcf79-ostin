def save_result(data):
    with open("result.txt", "a") as f:
        f.write(data + "\n\n")
