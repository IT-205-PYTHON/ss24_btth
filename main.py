from models.drink import Drink
from features import view_menu, add_drink, toggle_status

menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000),
]

while True:
    print("\n=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===\n")
    print("1. Xem danh sách đồ uống")
    print("2. Thêm đồ uống mới")
    print("3. Cập nhật trạng thái kinh doanh")
    print("4. Thoát chương trình")
    print("\n==============================================")
    choice = input("Chọn chức năng (1-4): ").strip()

    match choice:
        case "1":
            view_menu(menu)
        case "2":
            add_drink(menu)
        case "3":
            toggle_status(menu)
        case "4":
            print("\nCảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
            break
        case _:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4!")