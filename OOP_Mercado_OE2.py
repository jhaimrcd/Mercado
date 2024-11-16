class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}"

phone_list = []

def create_phone():
    brand = input("Enter phone brand: ")
    model = input("Enter phone model: ")
    price = input("Enter phone price: ")
    phone = Phone(brand, model, price)
    phone_list.append(phone)
    print("Phone created successfully!")

def modify_phone():
    display_all_phones()
    index = int(input("Enter the index of the phone to modify: ")) - 1
    if 0 <= index < len(phone_list):
        phone = phone_list[index]
        phone.brand = input(f"Enter new brand (current: {phone.brand}): ") or phone.brand
        phone.model = input(f"Enter new model (current: {phone.model}): ") or phone.model
        phone.price = input(f"Enter new price (current: {phone.price}): ") or phone.price
        print("Phone modified successfully!")
    else:
        print("Invalid index.")

def delete_phone_attribute():
    display_all_phones()
    index = int(input("Enter the index of the phone to modify: ")) - 1
    if 0 <= index < len(phone_list):
        phone = phone_list[index]
        attr = input("Enter the attribute to delete (brand, model, price): ").lower()
        if hasattr(phone, attr):
            delattr(phone, attr)
            print(f"{attr} deleted successfully!")
        else:
            print("Invalid attribute.")
    else:
        print("Invalid index.")

def delete_phone():
    display_all_phones()
    index = int(input("Enter the index of the phone to delete: ")) - 1
    if 0 <= index < len(phone_list):
        del phone_list[index]
        print("Phone deleted successfully!")
    else:
        print("Invalid index.")

def display_all_phones():
    if phone_list:
        print("\nList of Phones:")
        for idx, phone in enumerate(phone_list, start=1):
            print(f"{idx}. {phone.display_info()}")
    else:
        print("\nNo phones available.")

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Add Phone")
        print("2. Modify Phone")
        print("3. Delete Phone Attribute")
        print("4. Delete Phone")
        print("5. Display All Phones")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            create_phone()
        elif choice == "2":
            modify_phone()
        elif choice == "3":
            delete_phone_attribute()
        elif choice == "4":
            delete_phone()
        elif choice == "5":
            display_all_phones()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()