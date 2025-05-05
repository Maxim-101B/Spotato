import math

class Utilities():
    @staticmethod    
    def seconds_to_mm_ss(seconds):
        seconds = int(seconds)
        min = int(seconds // 60)
        sec = int(seconds % 60)
        return f"{min:02}:{sec:02}"
    
    @staticmethod 
    def round_up_to_thousand(x):
        # Проверяем, кратно ли число 1000 (с учётом погрешности для float)
        remainder = abs(x) % 1000
        if math.isclose(remainder, 0, abs_tol=1e-9) or math.isclose(remainder, 1000, abs_tol=1e-9):
            return x
        # Округляем вверх до следующей тысячи

        return math.ceil(x / 1000) * 1000
    
    
    #@staticmethod 
    #def get_file_extension(file_path):
    #    return os.path.splitext(file_path)[1]


