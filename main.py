from src.doubly_linked_list import DoublyLinkedList
from src.array_list import ArrayList

print()
print("__________Demonstration for DoublyLinkedList__________")

dll = DoublyLinkedList()
dll.append('A')
dll.append('B')
dll.append('C')


print("Initial list:")
print([dll.get(i) for i in range(dll.length())])
print()


print("Added 6 to the end:")
dll.append('6')
print([dll.get(i) for i in range(dll.length())])
print()


dll.insert('X', 1)
print("After inserting 'X' at position 1:")
print([dll.get(i) for i in range(dll.length())])
print()


dll.delete(2)
print("After deleting the element at position 2:")
print([dll.get(i) for i in range(dll.length())])
print()


print("First entry 'X':", dll.findFirst('X'))
print()


dll.reverse()
print("After reverse:")
print([dll.get(i) for i in range(dll.length())])
print()


cloned = dll.clone()
print("Cloned list:")
print([cloned.get(i) for i in range(cloned.length())])
print()


new_list = DoublyLinkedList()
new_list.append('X')
new_list.append('Y')
new_list.append('Z')
print("The list we are adding:", new_list)
print()

dll.extend(new_list)
print("The list after extend():", dll)
print()


dll.clear()
print("After cleaning, the length of ddl = ", dll.length())
print()

print("__________Demonstration for ArrayList__________")
print()

arr = ArrayList()
arr.append('A')
arr.append('B')
arr.append('C')

print("Initial list:")
print([arr.get(i) for i in range(arr.length())])
print()

arr.append('6')
print("Added 6 to the end:")
print([arr.get(i) for i in range(arr.length())])
print()

arr.insert('X', 1)
print("After inserting 'X' at position 1:")
print([arr.get(i) for i in range(arr.length())])
print()

arr.delete(2)
print("After deleting the element at position 2:")
print([arr.get(i) for i in range(arr.length())])
print()

print("First entry 'X':", arr.findFirst('X'))
print()

arr.reverse()
print("After reverse:")
print([arr.get(i) for i in range(arr.length())])
print()

cloned_arr = arr.clone()
print("Cloned ArrayList:")
print([cloned_arr.get(i) for i in range(cloned_arr.length())])
print()

new_arr = ArrayList()
new_arr.append('X')
new_arr.append('Y')
new_arr.append('Z')
print("The list we are adding:", [new_arr.get(i) for i in range(new_arr.length())])
print()

arr.extend(new_arr)
print("The list after extend():")
print([arr.get(i) for i in range(arr.length())])
print()

arr.clear()
print("After clearing, the length of arr = ", arr.length())
print()
