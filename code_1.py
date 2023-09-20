
def generate_random_data():
    random_string = 'Wonder election throw police doctor exist.'
    random_number = 59

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Wonder election throw police doctor exist.")
        print(f"Random Number: 59")

if __name__ == "__main__":
    main()
