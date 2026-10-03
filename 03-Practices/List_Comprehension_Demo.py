lst = ["red","green","blue"]
# result1 = "Yes" if "yellow" in lst else "No"
result2 = [color for color in lst if color == "red"]
print(result2)