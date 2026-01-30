phonebook = {
    "Eko" : "08123456789",
    "Jhon" : "08987654321",
    "Marcel" : "08234567890",
    "Zaki" : "08345678901"
  }

for name, number in phonebook.items():
    print("Nama: %s, Nomor: %s" % (name, number))

del phonebook["Marcel"]
print("Setelah menghapus Marcel:")
for name, number in phonebook.items():
    print("Nama: %s, Nomor: %s" % (name, number))

if "Eko" in phonebook:
    print("Nomor Eko adalah %s" % phonebook["Eko"])

if "Marcel" not in phonebook:
    print("Marcel tidak ditemukan dalam phonebook")
