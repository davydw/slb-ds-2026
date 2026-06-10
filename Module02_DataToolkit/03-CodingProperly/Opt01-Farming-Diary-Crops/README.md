## 🎯 Background and Objectives

Here is a little farming scenario you will code step by step to discover the benefits of inheritance.

You'll also see how to only run a subset of tests, only the ones for the code you already wrote.

## 📝 Specs

The farm has two kinds of **crops** (rice and corn).

![Crops](https://raw.githubusercontent.com/lewagon/fullstack-images/master/ruby/farming-diary/crops.svg?sanitize=true)

Discuss with your buddy: how many classes do you think you need, and how would you structure them?

**IMPORTANT:** In this challenge, do not directly use `make` to code your classes! Code the interface in `farm/farming_diary.py` and let the program guide you into designing the classes! At the end each chapter, when the interface prints the expected output, check your classes code with the `make` 👌

### 🌽 The `Corn` class

To start, code a `Corn` class in `farm/corn.py` with the following specifications:
- Initialize the instance variable `grains` to zero.
- A `water` method adds 10 grains anytime it is called.
- A `ripe` method returns `True` if there are at least 15 grains, otherwise `False`.

Open `farm/farming_diary.py` and complete the **Day One** section. Adapt the code to make it print the following output:

```bash
📝 Day One: Corn
The corn crop produced 10 grains
The corn crop is not ripe
```

Run your diary with:

```bash
python -m farm.farming_diary
```

You can run the test for the `Corn` class by running this:
```bash
pytest -v tests/test_corn.py
```

If you passed all the tests, you can run `make`. You should have 12 failed and 6 passed tests at this point.

This is a good point to commit and push:

```bash
git add farm/corn.py farm/farming_diary.py
git commit -m "Completed Corn"
git push origin master
```

### 🌾 The `Rice` class

Create a `Rice` class in `farm/rice.py` and copy/paste all the methods from the `Corn` class.
- Adjust the grains production in `water`: it adds only 5 grains.
- The `ripe` method has the same behavior as in `Corn`.
- `Rice` has a specific method called `transplant` which produces 10 more grains.

Continue your farming diary by planting some rice on **Day Two**.

When your program works, you can run the tests for the `Rice` class by running this:
```bash
pytest -v tests/test_rice.py
```

If you passed all the tests, you can run `make`. You should now have 6 failed and 12 passed tests at this point.

This is a good point to commit and push the two files you just changed. For the commands: get some inspiration from the previous step.

### 🔀 Refactoring

If you felt uncomfortable copy/pasting code, you were right! Duplicating code means more maintenance and is a source of errors. That's where inheritance comes to the rescue to keep the code DRY (Don't Repeat Yourself).

The crops share many similarities, so refactor them:
- Introduce a parent class named `Crop` in `farm/crop.py` and move the shared methods into it.
- Make `Corn` and `Rice` classes **inherit** from `Crop`.
- Don't forget to import the `Crop` class in `farm/corn.py` and `farm/rice.py`.

## ✅ Checks and takeaways

Now let's run `make` to run all the provided tests! Take the time to make all the tests pass to validate your architecture and the interfaces of your classes.

When all the tests pass, run `git status` to check which files were changed. Commit and push them.

Now that you committed your working code, make sure you also get 10/10 for style! Then commit and push again.

Congratulations on taking the time to let _the program_ guide your class design before running the tests. It's an important step in your learning journey as a developer gaining autonomy.
