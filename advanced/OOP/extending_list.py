class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList();

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])

# issubclass(A, B) = returns true/false if A is subclass of B
print(issubclass(SuperList, list))