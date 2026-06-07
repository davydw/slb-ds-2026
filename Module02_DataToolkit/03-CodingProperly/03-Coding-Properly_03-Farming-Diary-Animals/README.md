## 🎯 Background and Objectives

This challenge is an extension of the previous one: the farm welcomes its first animals!

You'll start coding your classes from scratch, just by interpreting how your code uses them. Oh, and we'll learn a bit more about writing tests too.

## 📝 Specs

![Animals](https://raw.githubusercontent.com/lewagon/fullstack-images/master/ruby/farming-diary/animals.svg?sanitize=true)

Discuss with your buddy: how many classes do you think you need, and how would you structure them?

Don't `make`! Wait until the very end of the challenge, follow the guidelines and let the farming diary guide you into coding the classes!

### 🐄 Parent and children

We are now familiar with the benefits of inheritance, let's go ahead and:
- Create the three empty classes
- Set the proper inheritance relationship between the children and the parent classes

Unlike in the previous challenge, let's start by coding the common behaviour in the parent class:
- An animal is initialized with zero **energy**
- You can **feed** an animal: it will increase its **energy** by 1

### 🐔 Animals Talk

To figure out the classes, let's start with the **program** we want to run:
- Open the `farm/farming_diary.py`, read _Day Three_ and gather information to code the classes.
- Run the file with `python farm/farming_diary.py`. Solve one error at a time by coding the missing `talk` methods in `Cow` and `Chicken`.

Expected output:

```bash
📝 Day Three: Animals Talk
The cow says moo
The female chicken says cluck cluck
The male chicken says cock-a-doodle-doo
```

### 🍽️ Feed The Animals

Let's move on to the Day Four and feed all the animals at once with an iteration. Remember your animals have a shared `feed` method? You can call the same method on two objects of different types! This concept is called [polymorphism](https://realpython.com/ref/glossary/polymorphism/) 🤓

Here is what you need to know about `feed`:
- `Cow`: beyond gaining energy, cows produce 2 liters of **milk**
- `Chicken`: beyond gaining energy, females produce 2 **eggs** (and males none 🤷‍♂️)

**Hint**: the children method **extend** the parent one. Don't forget to use `super` to call the parent's part!

Expected output:

```bash
📝 Day Four: Feed The Animals
The cow produced 2 liters of milk
The female chicken produced 2 eggs
The male chicken produced 0 eggs
```

### ✅ Time to test

When you're program works, run `make` to test if you coded it properly.

Wait a minute, is something missing in the tests?

<details>
  <summary markdown='span'>💡 Hints</summary>

  Yes, there are no tests for the `Cow` class.

  Your task: write the tests.

</details>


Go ahead and:
- Create a new `tests/test_cow.py` file.
- Code the necessary classes and methods. You can get your inspiration from the `Chicken` class.
- In total you should have 6 tests.

<details>
  <summary markdown='span'>💡 Hints if you don't get to 6</summary>

  - `test_initialize_sets_milk_to_zero`
  - `test_initialize_sets_energy_to_zero`
  - `test_feed_extends_method`
  - `test_feed_adds_milk`
  - `test_feed_adds_energy`
  - `test_talk_returns_moo`

</details>

When you're ready, run `make` again and see how the additional tests get executed.

Writing tests can take quite some time. Fortunately you can take a lot of inspiration from previously written tests. No need to start from scratch: nothing wrong with copying some boilerplate code. Once you know how to write and interpret tests yourself (and only then!), tools like GitHub Copilot can  be very helpful for repetitive tasks like writing tests.


## 🏁 Take away

Congratulations! You can run the `make` now to check that your code is properly organized.

In children classes, there are 4 kinds of methods:
- methods that **inherit** from the parent class: the method is only defined in the parent class
- methods that **extend** the parent's method definition: the method is slightly different in the children classes
- methods that **override** the parent's method: definition is completely different than in the parent class
- methods that are specific to the child class: they are not defined in the parent class _at all_

Extending a method requires the `super` keyword: it acts as if you copied the body from the parent method and pasted it where `super` is invoked.

You also learned how to write your own tests. Even if you don't do it a lot, it's very useful to know how tests are written!
