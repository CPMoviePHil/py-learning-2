

class MainProgram:
    @staticmethod
    def sum_list(li_1):
        total = 0
        for item in li_1:
            total += item
        return total


list_1 = list(range(1,11))
print(MainProgram.sum_list(list_1))
