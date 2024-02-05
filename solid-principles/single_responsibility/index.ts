// A class should have a single responsibilty
import * as fs from "fs";

class Journal {
  private entries: string[];
  public count: number;

  constructor() {
    this.entries = [];
    this.count = 0;
  }

  addEntry(entry: string): void {
    this.count++;
    this.entries.push(entry);
  }

  removeEntry(index: number): void {
    this.count--;
    delete this.entries[index];
  }

  toString(): string {
    return this.entries.join("\n");
  }

  // Adding extra responsibility
  //   saveFileToDisk() {}
}

/*
Above we are adding extra responsibility to the Journal class.
We can create a extra class called PersistenceManager for handing
saving the journal to disk
*/

class PersistenceManager {
  static saveToDisk(journal: Journal, filename: string): void {
    fs.writeFileSync(filename, journal.toString(), "utf-8");
  }
}

const j = new Journal();
j.addEntry("I learned solid principles today.");
j.addEntry("I ate burger.");
console.log(j.count);
j.removeEntry(1);
console.log(j.count);

PersistenceManager.saveToDisk(j, "myjouralts.txt");
