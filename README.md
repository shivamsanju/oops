# Object-Oriented Programming (OOP) and Design Patterns

## Object-Oriented Programming (OOP)

Object-Oriented Programming is a paradigm that structures software design around real-world entities, encapsulating data and behavior within objects. OOP principles include:

- **Encapsulation:** Bundling data and methods that operate on that data into a single unit, known as a class.

- **Inheritance:** Creating new classes by inheriting properties and behaviors from existing classes.

- **Polymorphism:** Allowing objects of different types to be treated as objects of a common type, enabling flexibility and extensibility.

- **Abstraction:** Representing essential features while hiding unnecessary details.

## Design Patterns

Design Patterns are reusable solutions to common problems encountered in software design. They provide a template for solving issues and help in creating maintainable and scalable software. The Gang of Four (GoF) design patterns are categorized into three groups: Creational, Structural, and Behavioral.

### Creational Patterns

#### Singleton Pattern

Ensures that a class has only one instance and provides a global point of access to it.

#### Factory Method Pattern

Defines an interface for creating an object, but leaves the choice of its type to the subclasses, creating an instance of one of the multiple classes.

#### Abstract Factory Pattern

Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

#### Builder Pattern

Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

#### Prototype Pattern

Creates new objects by copying an existing object, known as the prototype.

### Structural Patterns

#### Adapter Pattern

Allows the interface of an existing class to be used as another interface, making it compatible with clients that expect a different interface.

#### Bridge Pattern

Decouples an abstraction from its implementation so that the two can vary independently.

#### Composite Pattern

Composes objects into tree structures to represent part-whole hierarchies, allowing clients to treat individual objects and compositions of objects uniformly.

#### Decorator Pattern

Attaches additional responsibilities to an object dynamically, providing a flexible alternative to subclassing for extending functionality.

#### Facade Pattern

Provides a simplified interface to a set of interfaces in a subsystem, making it easier to use.

#### Flyweight Pattern

Minimizes memory usage or computational expenses by sharing as much as possible with related objects, allowing the reuse of existing similar objects.

#### Proxy Pattern

Controls access to an object by acting as an intermediary, typically to add functionality or restrict access.

### Behavioral Patterns

#### Chain of Responsibility Pattern

Passes a request along a chain of handlers, each processing the request or passing it along to the next handler in the chain.

#### Command Pattern

Encapsulates a request as an object, thereby parameterizing clients with queues, requests, and operations.

#### Interpreter Pattern

Defines a grammar for interpreting the sentences in a language and provides an interpreter to interpret those sentences.

#### Iterator Pattern

Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

#### Mediator Pattern

Defines an object that centralizes communication between a set of objects, promoting loose coupling.

#### Memento Pattern

Captures and externalizes an object's internal state so that the object can be restored to this state later.

#### Observer Pattern

Defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically.

#### State Pattern

Allows an object to alter its behavior when its internal state changes, treating state transitions as explicit objects.

#### Strategy Pattern

Defines a family of algorithms, encapsulates each algorithm, and makes them interchangeable. It allows the client to choose the appropriate algorithm at runtime.

#### Template Method Pattern

Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

#### Visitor Pattern

Represents an operation to be performed on the elements of an object structure, allowing the definition of new operations without changing the classes of the elements.

These design patterns contribute to building maintainable, scalable, and flexible software systems.
