def is_palidrome(string: str) -> bool:
    string = string.replace(" ","").lower()
    return string == string[::-1]

def run():
    print(is_palidrome("ana"))    

if __name__ == '__main__':
    run()
