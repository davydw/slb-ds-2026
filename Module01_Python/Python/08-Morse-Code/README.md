## Morse challenge 📻

### Objectives 🎯

In this challenge, we'll learn:
- How to **break down large problems** into small problems.
- How to create different **modules**, and use functions from another module.
- How to **run tests efficiently**.
- Get familiar with the concept of **encoding and decoding**: we will encounter this again in the Deep Learning module.

### ❔ Background

(From [Wikipedia](https://en.wikipedia.org/wiki/Morse_code)) Beginning in 1836, the American artist Samuel F. B. Morse, the American physicist Joseph Henry, and Alfred Vail developed an electrical telegraph system. This system sent pulses of electric current along wires which controlled an electromagnet that was located at the receiving end of the telegraph system. A code was needed to transmit natural language using only these pulses, and the silence between them. Around 1837, Morse, therefore, developed an early forerunner to the modern **International Morse code**.

In this exercise, we'll write a morse code **encoder** and **decoder**. We'll just consider the 26 letters of the English alphabet, ("A" -> "Z") and ignore all other characters (numbers, punctuation, etc.).

### ⚙️ Setup

For this challenge, make sure you open the challenge from the root of this challenge folder, and open VS Code from that place:

```bash
cd ~/code/<user.github_nickname>/{{ local_path_to("01-Python/01-Programming-Basics/06-Morse-Code") }}
code .
```

We will be working with multiple files in this challenge, so it's important you always work from this location.

### 🏗️ Workflow

We'll break down the code in multiple smaller modules that we can reuse. We will then have to import them. Start by looking at the files in the `morse` directory. In the `mapping.py` file we already gave you a dictionary with the Morse code for the letters of the alphabet.

### ➡️ Code the encoder

First, implement the `encode` method in `morse/encoder.py` which will take text as a parameter and return the Morse sequence for it. Letters of the same word will be separated by a space and words will be separated by a pipe character `|`.

For example, the sentence `"Hi Guys"` should be encoded into `".... ..|--. ..- -.-- ..."`

Break down the complexity by creating two functions: first code a function to encode one word. Then you can call the `encode_word` function from the `encode` function to encode a complete sentence.

### 🧪 Running and testing your code

Before you run the tests, make sure your code works without errors. We added an `if __name__ == "__main__"` block for you to try out your code with `python morse/encoder.py`.

<details>
  <summary markdown='span'>
  ⛓️‍💥 Getting an error <code>No module named 'morse'</code>?
  </summary>

Your terminal is probably not based in the root folder of the challenge. Maybe you moved into the `morse` folder? In that case, move one level up in your terminal.

Or did you open VS Code from inside the `morse` folder? In that case, close VS Code, and open it again from the main folder of this challenge.

The location from where you run your code is important when you use multiple files. We'll see ways to make this a bit less tricky later during the bootcamp.

</details>


Once that works, you can run the tests for your encoder. You could run `make`, but that would run all the tests, including those for the encoder, that we haven't coded yet. So instead run this:

```bash
pytest -v -k encoder
```

> **Why do we use `-v` and `-k`?**
>
> With the `-v` we tell pytest to report on the individual tests within a test class. Try it out without the `-v` and see the difference.
>
> With the `-k encoder` at the end, we ask pytest to only run tests that contain "encoder" in their name.
>
> You can combine conditions like this too: `pytest -v -k "encoder and not pipe"` to run all tests with "encoder" in their name, but excluding those with "pipe" in their name.

Before we move on to the decoder, don't forget to:

```bash
git add morse/encoder.py
git commit -m "Finished the encoder"
git push
```

### ⬅️ Code the decoder

Once the encoder is working, you can start working on the `decode` method in `morse/decoder.py` which will do the opposite!

Again, first run the code (`python morse/decoder.py`), then run the tests for the decoder only.

How can you try out your code without having to write Morse code yourself? In the `if __name__ == "__main__"`, you can first use your **en**coder functions to encode text into Morse code. Then use your **de**coder functions to decode back into text. The result should be your original input (in uppercase).

Before you move on to the last part, commit and push your changes!

### ✅ Testing everything

With your encoder and decoder finished, it's time to run all the tests. This time you can just run `make`.

All your tests should pass green. Now the only thing that's left is to get good coding style. Make sure to get 10/10. If you don't understand why you're not getting good coding style, ask a TA.

Once you're done with this part, commit and push again.

### 💡 A final word on encoding and decoding

Encoding and decoding as we applied it here is the process of converting data into a specific format for transmission or storage, and then reversing it to retrieve the original information.

So if you encode a message and then decode the result of the encoding, you should get the original input back, right?

But did we? Not completely: Morse code is case-insensitive. So both `a` and `A` are encoded into the same code. So when we decode the result, we'll see that we lost a bit of information: wether the text was capitalized or not.

In Deep Learning we'll see similar things happening. Stay tuned for that!
