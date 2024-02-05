# A class should have a single responsibilty

class Journal:
    def __init__(self) -> None:
        self.entries: list[str] = []
        self.count = 0

    def add_entry(self, entry: str) -> None:
        self.count += 1
        self.entries.append(entry)
    
    def remove_entry(self, index: int) -> None:
        self.count -= 1
        del self.entries[index]

    def __str__(self) -> str:
        return '\n'.join(self.entries)

    ## Adding extra responsbility
    # def save_to_disk(self, filename) -> None:
    #     pass

'''
Above we are adding extra responsibility to the Journal class.
We can create a extra class called PersistenceManager for handing
saving the journal to disk
'''

class PersistenceManager:
    @staticmethod
    def save_to_disk(journal: Journal, filename: str) -> None:
        with open(filename, 'w') as fh:
            fh.write(str(journal))


if __name__ == '__main__':
    j = Journal()
    j.add_entry("I learned solid principles today.")
    j.add_entry("I ate burger.")
    print(j.count)
    
    PersistenceManager.save_to_disk(j, "myjoural.txt")

