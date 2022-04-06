class Utility:

    def __init__(self):
        pass

    def get_int(self):
        return int(input(""))


class HashTable:
    def __init__(self):
        pass

    def get_int(self):
        return int(input(""))


def hashing_runner():
    """
    This method acts as runner
    :return: nothing
    """
    utility_obj = Utility()
    hash_obj = HashTable()

    print('These are the Numbers in our File')
    file = open("hash_table.py", "r")
    print(file.readline())

    print('Now enter the Number you are looking for')
    try:
        number = utility_obj.get_int()
    except Exception as e:
        print(e)
        print("Enter Number only")
        hash_obj.insert()
        print(hash_obj.search(number))

        print('Now Updated File Content are as Follows')
        hash_obj.file_update(number)


if __name__ == "__main__":
    hashing_runner()
