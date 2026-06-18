def view_menu(menu):
    print("\n--- DANH SÁCH ĐỒ UỐNG ---\n")
    print(f"{'Mã món':<8}| {'Tên món':<20}| {'Giá bán':<10}| Trạng thái")
    print("-" * 55)
    for drink in menu:
        print(f"{drink.code:<8}| {drink.name:<20}| {drink.price:<10}| {drink.get_status()}")
    print()