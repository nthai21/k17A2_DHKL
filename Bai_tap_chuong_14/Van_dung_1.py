def is_triangle(a, b, c):
    """
    Kiểm tra xem ba số a, b, c có thể tạo thành một tam giác hay không.
    """
    return a + b > c and a + c > b and b + c > a

try:
    # Nhập độ dài các cạnh từ người dùng
    a = float(input("Nhập độ dài cạnh a: "))
    b = float(input("Nhập độ dài cạnh b: "))
    c = float(input("Nhập độ dài cạnh c: "))
    
    # Kiểm tra ngoại lệ
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Độ dài các cạnh phải là số dương.")
    
    if not is_triangle(a, b, c):
        raise ValueError("Không thỏa mãn điều kiện tồn tại tam giác.")
    
    # In kết quả nếu không có ngoại lệ
    print("Ba số", a, b, c, "có thể tạo thành một tam giác.")
except ValueError as ve:
    print("Đã xảy ra lỗi:", ve)
except Exception as e:
    print("Đã xảy ra lỗi không xác định:", e)
