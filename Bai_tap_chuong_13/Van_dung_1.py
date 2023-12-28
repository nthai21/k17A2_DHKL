# Trong xu_ly_tap_tin.py
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "Không tìm thấy tập tin."
    except Exception as e:
        return f"Có lỗi xảy ra: {e}"
