/*
1. High-level modules should not depend on low-level modules.
Both should depend on abstractions.

2. Abstractions should not depend on details. 
Details should depend on abstractions.
*/

enum Relationship {
  CHILD = 0,
  PARENT = 1,
  SIBLING = 2,
}

class Person {
  name: string;

  constructor(name: string) {
    this.name = name;
  }
}

type SingleRelationship = {
  person1: Person;
  relationship: Relationship;
  person2: Person;
};

class Relationships {
  relations: SingleRelationship[];

  constructor() {
    this.relations = [];
  }

  addChildToParent(child: Person, parent: Person): void {
    this.relations.push({
      person1: parent,
      relationship: Relationship.CHILD,
      person2: child,
    });
  }
}

class Research {
  constructor(r: Relationships) {
    const relations = r.relations;
    for (const item of relations) {
      if (
        item.person1.name === "John" &&
        item.relationship === Relationship.CHILD
      ) {
        console.log("John has a child ", item.person2.name);
      }
    }
  }
}

/*
The problem above is that the high level module Research depends on the 
implementation of relations inside Relationships. If we change it from a list
to any other data structure, the code will break.

The solution is to move the implementation of finding child to an abstraction.
*/

interface RelationshipBrowser {
  getChildrenOfPerson(name: string): Person[];
}

class RelationshipsNew implements RelationshipBrowser {
  relations: SingleRelationship[];

  constructor() {
    this.relations = [];
  }

  addChildToParent(child: Person, parent: Person): void {
    this.relations.push({
      person1: parent,
      relationship: Relationship.CHILD,
      person2: child,
    });
  }

  getChildrenOfPerson(name: string): Person[] {
    const result: Person[] = [];
    for (const item of this.relations) {
      if (
        item.person1.name === name &&
        item.relationship === Relationship.CHILD
      ) {
        result.push(item.person2);
      }
    }
    return result;
  }
}

class ResearchNew {
  constructor(r: RelationshipsNew) {
    const children = r.getChildrenOfPerson("John");
    for (const child of children) {
      console.log("John has a child ", child.name);
    }
  }
}
