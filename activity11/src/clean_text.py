def clean_text(text: str) -> str:
    new_text = [""]
    for c in text:
        if c.isalpha() or c.isspace():
            new_text[-1] = new_text[-1] + c.lower()
    return " ".join(new_text)


if __name__ == "__main__":
    print(clean_text("Hello, world! How are you doing? Really?! So, what are you doing?"))
