# 1. dengan menggunakan kurung kurawal {}
import sys
kataSambung = {"semangka", "pisang", "apel"}
print(kataSambung)  
print(type(kataSambung))
print("ukuran memori:", sys.getsizeof(kataSambung))

# 2. dengan menggunakan fungsi set()
tokenword: set[str] = set(["semangka", "pisang", "apel"])
print(tokenword)
print(type(tokenword))
print("ukuran memori:", sys.getsizeof(tokenword))

#membuktikan tidak menganut konsep indeks
# print(tokenword[0])

#menambahkan anggota set
# 1. dengan menggunakan fungsi add()
kataSambung.add("mangga")
print(kataSambung)
# 2. dengan menggunakan fungsi update()
tokenword.update(["mangga", "jeruk"])


#menghapus anggota set
# 1. remove
kataSambung.remove("semangka")
#print(kataSambung)
# 2. discard
kataSambung.discard("apel")
#print(kataSambung)
# 3. pop
#kataSambung.pop()
print(kataSambung)
print(tokenword)

#mengubah anggota set

#implementasi operasi pada set
# 1. union
setA = {1, 2, 3}
setB = {3, 4, 5}
print(setA | setB) # hasilnya {1, 2, 3, 4, 5}
print(setA.union(setB)) # hasilnya {1, 2, 3, 4, 5}
# 2. intersection
print(setA & setB) # hasilnya {3}
print(setA.intersection(setB)) # hasilnya {3}
# 3. difference
print(setA - setB) # hasilnya {1, 2}
print(setB.difference(setA)) # hasilnya {4, 5}
# 4. symmetric difference
print(setA ^ setB) # hasilnya {1, 2, 4,}
print(setA.symmetric_difference(setB)) # hasilnya {1, 2, 4, 5}