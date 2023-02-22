CS1440 - Friday, February 24 - Lecture 19 - Module 3

# Topics:
* [Action Items](#action-items)
* [UML Class Diagrams](#uml-class-diagrams)
* [What is the point of a UML Class Diagram?](#what-is-the-point-of-a-uml-class-diagram)
* [UML: Multiplicity Constraints](#uml-multiplicity-constraints)
* [Real-world UML class diagrams](#real-world-uml-class-diagrams)


------------------------------------------------------------
# Action Items

*   Complete phases **4. Deployment** and **5. Maintenance** *today* 
    *   Make your final push to GitLab early so you have plenty of time to **verify** your submission
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# [UML Class Diagrams](../UML.md)

The Unified Modeling Language is an important design-phase tool that helps you
capture the essence of an object-oriented system.  Creating a UML class diagram
early on will support your work in the later phases of the project, especially
the Implementation phase.



# [What is the point of a UML Class Diagram?](../UML.md#what-am-i-trying-to-accomplish-with-a-uml-class-diagram)


What sorts of things can I say in the Unified Modeling Language?

*   High-level structure of a system
*   Ways in which classes/objects in a system are related to each other
*   How many objects participate in a relationship

What do I expect you to accomplish with UML?

*   Explain *what* classes exist in your solution
    *   Describe the starter code so as to help you understand it
    *   Show me how the starter code classes have changed in your implementation
    *   Show me any new classes that you created

The goal of Assignment #4 is to ensure that, for at least once in your career, you have the experience of designing an object-oriented system *before* you sit down to code it, as opposed to documenting it after the fact.



# [UML: Multiplicity Constraints](../UML.md#multiplicity-constraints)

In some systems it is important to document the number of objects that participate in relationships.

A multiplicity constraint indicates how many times an object from one class can be associated with objects of another class



# [Real-world UML class diagrams](https://www.uml-diagrams.org/class-diagrams-examples.html)

I show these examples of UML class diagrams to give you an idea of what a UML class diagram that describes part of a real-world program looks like.  Your diagrams do not need to be this complex or detailed!  Our Bingo Card Generator is far more simple than these systems.

It takes *many* UML class diagrams to fully describe a real-world system.  

The Unified Modeling Language defines other kinds of diagrams besides class diagrams.  A class diagram describes only one aspect of a system.  Other diagrams are used to explain how various parts of the system interact with each other while the program is running, and some are used to describe all of the ways a user might use a system, etc.


## Diagrams of interest:

*   Illustration of dependencies, public/private access modifiers, data types
    *   [Sentinel HASP Classes of Aladdin Package](https://www.uml-diagrams.org/software-licensing-class-diagram-example.html)
*   Illustration of associations, multiplicity constraints
    *   [Online Shopping](https://www.uml-diagrams.org/examples/online-shopping-domain-uml-diagram-example.html)
        *   This diagram uses the *composition* symbol for some of its associations; we won't be that strict in Bingo!
*   Illustration of associations, multiplicity constraints, relationship descriptions
    *   [DICOM Model of the Real World](https://www.uml-diagrams.org/dicom-real-world-uml-class-diagram-example.html)


### Symbology Glossary

*   `+` indicates *public* accessibility
*   `-` indicates *private* accessibility
*   `#` indicates *protected* accessibility
*   `^` denotes an *inherited* member
    *   This data member belongs to this class because it inherits from an ancestor class
*   `/` denotes a *derived* member
    *   This member's value is computed from other members
*   Open (white) diamond indicates an "Aggregation" association
    *   The diamond is attached to the "parent" class
    *   Instances of the child class may exist independently of its parent, and may be attached to other parents/aggregates
        *   For example Cars & Wheels
        *   Wheels can be removed from one car and attached to another, or may be kept in the garage until the weather improves
*   Closed (black) diamond indicates an "Composition" association
    *   The diamond is attached to the "parent" class
    *   Instances of the child class may **not** exist independently of its parent 
        *   For example, you and your brain
        *   You cannot live without your brain, and vice-versa



