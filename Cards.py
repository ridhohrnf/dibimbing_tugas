from random import choice

class Cards:
    def __init__(self):
        self.lst = ["Ace","2","3","4","5","6","7","8","9","Jack","Queen","King"]
# kenapa nomornya dijadikan string? gabisa integer aja?
    def draw(self):
        print(choice(self.lst))


def main():
    card = Cards()
    card.draw()

if __name__ == "__main__":
    main()