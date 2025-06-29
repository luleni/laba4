arr = [1,7,5,1,23,4]
unique_elements = list(set(arr))
unique_elements.sort()

second_largest = unique_elements[-2]
print("Второй наибольший элемент:", second_largest)
