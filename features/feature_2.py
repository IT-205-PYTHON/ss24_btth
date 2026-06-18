from models.drink import Drink


def add_drink(menu):
    print()
    code = input("Nhập mã món: ").strip().upper()

    for drink in menu:
        if drink.code == code:
            print("Mã món đã tồn tại trong hệ thống!")
            return

    name = input("Nhập tên món: ").strip()

    price_input = input("Nhập giá bán: ").strip()

    if not price_input.isdigit() or int(price_input) <= 0:
        print("Giá bán không hợp lệ!")
        return

    new_drink = Drink(code, name, int(price_input))
    menu.append(new_drink)
    print(f"\nThành công: Đã thêm món {name} vào thực đơn!")