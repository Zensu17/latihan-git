number = 5
second_number = 10
first_array = [number] * 5
second_array = [second_number] * 5
combined_array = first_array + second_array

if number > second_number:
    print("number lebih besar dari second_number")

if first_array.count(number) == 5:
    print("first_array hanya berisi number")

if len(second_array) == 5:
    print("second_array memiliki panjang 5")

if len(first_array) + len(second_array) == len(combined_array):
    print("combined_array adalah gabungan dari first_array dan second_array")

