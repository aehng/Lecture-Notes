CS1440 - Friday, March 17 - Lecture 25 - Module 4

# Topics:
* [Announcements](#announcements)
* [Discuss Brooks' Essay "The Other Face", Ch15 of TMMM](#discuss-brooks-essay-the-other-face-ch15-of-tmmm)
* [How & when to comment](#how-when-to-comment)
* [What Is Refactoring?](#what-is-refactoring)
* [Non-functional Attributes](#non-functional-attributes)


------------------------------------------------------------
# Announcements

## [HackUSU - Utah's Premiere Collegiate Hackathon](https://www.hackusu.com/)

*   **What**  24-hr Hackathon
    *   Build a software or hardware project to compete against other teams. All college students and high school seniors are invited!
*   **When**  4:00pm Friday, March 24 - Saturday, March 25
*   **Where** Huntsman Hall
*   **Workshops**
    *   We'll have many great workshops and tech talks on a variety of topics. Check back closer to the event for a complete list!
*   **Networking**
    *   Come network with our sponsors and potential employers. There will be many industry experts to learn from and learn more about their companies!
*   **Free Food**
    *   We'll provide dinner on Friday, and breakfast, lunch, and dinner on Saturday. There will also be plenty of snacks available the entire event!


# Action Items

*   Complete phases **4. Deployment** and **5. Maintenance** *today* 
    *   Make your final push to GitLab early so you have plenty of time to **verify** your submission
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team

## Questions about the assignment:

How do I write a unit test to check if the is not a 300th card in a Deck of 30?

```python
def setUp(self):
    self.d = Deck(30)

def test_draw_any_card(self):
    self.assertRaises(IndexError, self.d.__getitem__, 300)
```



# Discuss Brooks' Essay "The Other Face", Ch15 of TMMM

Take a few moments to write on your mud card what you felt the **big idea** of this essay was.



# [How & when to comment](../How_and_When_to_Comment.md)

Comments can be a controversial subject.  Strongly-held opinions run the gamut from "always comment everything" to "comments are a code smell".  Here I offer some advice to help you decide what comments belong in your source code.



# [What Is Refactoring?](../Refactoring.md)

> The process of restructuring existing computer code without changing its external behavior.



# [Non-functional Attributes](../Refactoring.md#non-functional-attributes)

*Non-functional requirements* are aspects of a program which are difficult to measure, or which aren't spelled out in the specification.



