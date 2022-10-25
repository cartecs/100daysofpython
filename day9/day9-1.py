kv={"Bug": "An error", "Function": "code you can call"}
print(kv["Bug"])
kv["loop"] = "doing something over and over"
print(kv)

kv["Bug"] = "different value"
print(kv["Bug"])

for item in kv:
    print(kv[item])