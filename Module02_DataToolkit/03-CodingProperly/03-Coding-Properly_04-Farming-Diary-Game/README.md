## 🎯 Background and Objectives
Back to our Farm diary. After all the great work you did building the classes, let's reward our efforts by building a game on top of it! Let's build an interface where the player is a farmer who manages his/her crops and animals, and see the farm evolve thanks to an illustration we provide.

You will learn how to build an interface using an infinite loop!

## 🏗️ Setup

Let's start by importing your animals and crops classes in this challenge:

```bash
cp ../data-farming-diary-crops/farm/{crop.py,corn.py,rice.py} farm
cp ../data-farming-diary-animals/farm/{animal.py,cow.py,chicken.py} farm
```

In `farm/interface.py`, we already added the right `import` at the top of the file to load your classes 👌

## 📝 Specs

The player can choose between a set of actions: plant corn, plant rice, water the crops, add animals, etc.
When the player picks one action, we translate it in code using our classes and move on to the next choice. It's a loop. Let's build it step by step.

![Loop](https://raw.githubusercontent.com/lewagon/fullstack-images/master/ruby/farming-diary/loop.svg?sanitize=true)


There is no `make` on this challenge.

### 🖥️ Start with a basic UI

Open `farm/interface.py` and code a very basic user interface, running only once:
- Invite the player to pick a word from a list.
- Display a simple sentence for each word.

Running `python farm/interface.py`, you should display something along:

```bash
Pick an action: [corn | rice | quit]
> corn
Let's plant corn crops!
```

or

```bash
Pick an action: [corn | rice | quit]
> rice
Rice crops today!
```

or

```bash
Pick an action: [corn | rice | quit]
> quit
See you next time
```

When the player types a random word:

```bash
Pick an action: [corn | rice | quit]
> lalala
I don't know what you mean...
```


### 🔁 Make it loop

The game will not be very funny to play if it quits after one action. Make it loop until the `quit` action is typed the player. Running `python/interface.py`, should give the following output:

```bash
Pick an action: [corn | rice | quit]
> corn
Let's plant corn crops!

Pick an action: [corn | rice | quit]
> rice
Rice crops today!

Pick an action: [corn | rice | quit]
> corn
Let's plant corn crops!

Pick an action: [corn | rice | quit]
> quit
See you next time
```

### 🧑‍🌾 Planting crops

Now that you have the infinite loop in place, let's introduce our farm classes in the game. When the player picks `corn` or `rice`, instantiate objects of the appropriate class and store them in a `crops` list.

To give you an illustrated feedback of the state of the farm after each action, add a line with `Board().display()` inside the loop. If your code works as expected, the farm will live 😀

> No need to go and try to understand the `helpers/board.py` and `helpers/ref.py`. It's complicated code using some advanced Python concepts that you won't need in everyday Data Science & AI coding.

### 🚰 Watering crops

Add a new action to the user interface: `water`:

```bash
Pick an action: [corn | rice | water | quit]
```

In this action, the player waters all the crops (corn and rice) already planted. Remember they both inherit the `water` method from `Crop`.

### 🐄 Animals

Congratulations on building the crops part. Do you want to give a try to build the animals part all by yourself?

The UI has three new entries (cow, chicken and feed):

```bash
Pick an action: [corn | rice | water | cow | chicken | feed | quit]
```

**Hints and clues:**
- `cow` and `chicken` actions create new instances of the corresponding classes and stores them in an `animals` array
- Chickens have a gender, picked randomly by the game
  <details>
  <summary markdown='span'>Hint</summary>

  Check the use of `random.choice`

  </details>

Good luck! 🚀
