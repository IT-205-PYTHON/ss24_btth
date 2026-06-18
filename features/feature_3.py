def toggle_status(menu):
    print()
    code = input("Nhập mã món cần cập nhật: ").strip().upper()

    for drink in menu:
        if drink.code == code:
            drink.toggle_available()
            print(f"\nĐã cập nhật trạng thái món {drink.code}.")
            print(f"Trạng thái hiện tại: {drink.get_status()}")
            return

    print("Không tìm thấy món có mã này!")