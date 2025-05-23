from faker import Faker

if __name__ == '__main__':
    f = Faker()
    for i in range(5):

        print(f"-----------------FAKE DETAIL # {i+1}-----------------------")
        fake_name = f.name()
        fake_address = f.address()
        fake_text = f.text()
        print(f"Name: {fake_name}")
        print(f"Address: {fake_address}")
        print(f"Text: {fake_text}")