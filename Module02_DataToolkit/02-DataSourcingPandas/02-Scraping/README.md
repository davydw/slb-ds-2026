In this exercise, we will put in practice the Scraping techniques covered in the lecture. The goal will be to automatically extract information from a website with Python.

The website we are scraping is [books.toscrape.com](http://books.toscrape.com/). It's a website which has been created exactly for our purpose -  to learn how to scrape!

The goal will be to automatically retrieve information about sold books, like their name, price, rating, etc. The trick is that the website is **paginated**. Can you see how? Do you foresee it being a difficulty?

## Setup

The goal is to scrape the website **and** then use `pandas` to visualize the extracted information. For this exercise, it still makes sense to work in a Notebook.

```bash
jupyter notebook
```

Go ahead and open the new Python Notebook in the `~/code/<user.github_nickname>/{{local_path_to("02-Data-Toolkit/02-Data-Sourcing/02-Scraping")}}` folder.

In the Python world, an easy-to-use library for scraping is `BeautifulSoup`. We installed it during the setup, so we can import it straightaway.

We'll combine it with the `requests` library: `requests` will help us to fetch the HTML page, and `BeautifulSoup` will help us to extract the information out of the page.

Start your notebook with the following imports in the first code cell:

```python
import requests
from bs4 import BeautifulSoup

import numpy as np
import pandas as pd

%matplotlib inline
import matplotlib.pyplot as plt
```

## First request

Insert a new cell and work on the `TODO`s (the starter code is the same as the one in the lecture's slides!)

```python
url = "http://books.toscrape.com/"

# TODO: Use `requests` to do an HTTP request to fetch data located at that URL
# TODO: Create a `BeautifulSoup` instance with that data
```

<details><summary markdown='span'>View solution
</summary>

This code is quite generic and should be the same as the lecture! If you already have a scraping project, what you usually do, is open it and copy-paste those first lines!

```python
url = "http://books.toscrape.com/"

# This is where we do an HTTP request to get the HTML from the website
response = requests.get(url)

# And this is where we feed that HTML to the parser
soup = BeautifulSoup(response.content, "html.parser")
```

</details>

In a new code cell, inspect your `soup` variable. What is its type? At first sight it looks like a string, but is it? Check it with `type(soup)`.

`soup` is now a BeautifulSoup object containing the parser on which we can run our queries to extract information from the HTML. To know which HTML elements you want to extract, you need to analyze the *Books to Scrape*'s website HTML with the browser inspector.

To use the browser inspector, right click on the element you want to inspect, and in the menu choose the `Inspect` option.

![Screenshot of the website and the inspector](https://res.cloudinary.com/wagon/image/upload/v1562063504/books-to-scrape_hojlqo.png)

Can you spot which HTML contains **one** book? Is it identical for each book?

<details><summary markdown='span'>View solution
</summary>

The `<article />` element with the class `product_pod` is what we are looking for! All the books on the page have exactly the same structure, that's _exactly_ what we need for parsing.

```html
<article class="product_pod">
  <!-- [...] -->
</article>
```

</details>

Now that we have identified the relevant HTML, we can use the `soup` Python variable to query the document. Let's use the [searching by CSS class](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-by-css-class) approach. Insert a new cell and try to select **all** books in the HTML. Store this in a `books_html` variable.

<details><summary markdown='span'>View solution
</summary>

```python
books_html = soup.find_all("article", class_="product_pod")
len(books_html)
```

</details>

Now that we have a `books_html` variable containing all the HTML `<article />`s, let's focus on **one** book (the first!) and try to extract all the information we need from that HTML fragment.

## Parsing _one_ book

It's a good time for you to insert a **Markdown cell** and type in the following:

```markdown
## Parsing _one_ book
```

Of course you can write more text! The goal is to document your train of thoughts in your notebook to eventually have a well documented/structured Notebook.

Let's have a look at the HTML fragment of the first book. Insert a code cell and type in:

```python
books_html[0]
```

Great! We now have a smaller piece of HTML to deal with.

It looks like a string doesn't it? But we know better by now! Check it's `type()`. It seems to be a more advanced object again.

We can **chain** the [`.find()`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find) on this HTML fragment to **extract** 3 pieces of information from it.

### Find the book's title - retrieving text from an attribute

Let's start with the book *title*. Try to retrieve this information from `books_html[0]` and store it in a `book_title` variable.

You can try to find it within the HTML code that you displayed in the notebook. You can also go back to your browser and use the Inspect function again to find the element that contains the title, and from there go up the hierarchy until you're back at the `<article >` level.

<details><summary markdown='span'>View solution (only <strong>after</strong> you tried it yourself!)
</summary>

The title is located in an HTML link tag `<a />` inside the `<h3 />` tag. So we need to first `.find()` the `h3`, then the `a`:

```python
books_html[0].find("h3").find("a")
```

That's almost it. Now we need to select the title in the `<a />` tag's **attributes**:

```python
books_html[0].find("h3").find("a").attrs
```

The line above returns a `dict`. You can now select the right key!

```python
book_title = books_html[0].find("h3").find("a").attrs["title"]
book_title
```

</details>

### Find the book's price - getting a number out of an element

Awesome! Let's now try to retrieve the **price** of that book. Going back to the element inspection in the browser we find that the price is located within a `<p class="price_color"></p>`. Try to put the price in a `book_price` variable, and be careful, we want to get a `float`!


<details><summary markdown='span'>View solution (only <strong>after</strong> you tried it yourself!)
</summary>

Like for the `<article />` before to select books, we are going to use the "Searching by CSS class" approach, combined with using the [`.string`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#string) method:

```python
books_html[0].find("p", class_="price_color").string
```

The thing is that we want to extract the **number** (here that would be a Python `float`) rather than just text. We need to get rid of the first character `£` with the slice method on the `list` and then pass the sliced string to the `float()` method to convert it:

```python
book_price = float(books_html[0].find("p", class_="price_color").string[1:])
book_price
```

</details>

### Find the book's rating

Finally we need to get the **rating** (how many yellow stars does the book have). Back to the browser inspector, we can see that there is a `<p class="star-rating TEXT"></p>` where `TEXT` can take the values `"One"`, `"Two"`, `"Three"`, `"Four"` or `"Five"`. This one is a bit more difficult then, but doable. Insert a cell and copy/paste the following code:

```python
book_stars_html = books_html[0].find("p", class_="star-rating")
book_stars_html
```

```python
book_stars_html.attrs['class']
```

In Python, you can use the `in` keyword to check if an element is contained in a `list`. For instance:

```python
cities = [ 'paris', 'london', 'brussels' ]

if 'berlin' in cities:
    print("Berlin is available")
else:
    print("Sorry, Berlin is not available")
```

:question: Define a method `parse_rating` which takes a list of classes (from the `<p />`) and returns the rating from `1` to `5`:

```python
def parse_rating(rating_classes):
    # TODO: Look at `rating_classes` and return the correct rating
    # e.g. of an argument for `rating_classes`: [ 'star-rating', 'Three' ]
    # "One" => 1
    # "Two" => 2
    # "Three" => 3
    # "Four" => 4
    # "Five" => 5
    return 0
```

<details><summary markdown='span'>View solution (only <strong>after</strong> you tried it yourself!)
</summary>

```python
def parse_rating(rating_classes):
    """
    Parses the rating classes and returns the rating

    Parameters
    ----------
    rating_classes : str
        The rating classes of the book: these are the classes of the stars element in the HTML

    Examples
    --------
    >>> rating_classes = ['star-rating', 'Three']
    >>> parse_rating(rating_classes)
    3
    """
    # Define the ratings: mapping from English to numerical
    ratings = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    # For each of the 5 possible ratings, check if it's in the rating classes
    for rating in ratings:
        if rating in rating_classes:
            return ratings[rating] # Found the rating, return the numerical value
```

</details>

Once you implemented this method, you can use it to read the book's rating! Insert a new code cell and copy/paste the following code:

```python
book_rating = parse_rating(books_html[0].find("p", class_="star-rating").attrs['class'])
```

## Parsing _all_ books

Once again, it's a good time to insert a **Markdown cell** and type in the following:

```markdown
## Parsing _all_ books
```

So far, we wrote the code to parse all the information for **the first** book.

We now need to _glue_ all the code above and put it inside a `for` loop over all the books in the `books_html` variable!

We are going to store the information collected about the books in a **Python `dict`**. This dictionary will have three keys `Title`, `Price` and `Rating`. The **values** stored in that dictionary will be `list`s with the values for all the books:

- `Title` => `["A light in the attic", "Tipping the Velvet", ...]`
- `Price` => `[51.77, 53.74, ...]`
- `Rating` => `[3, 1, ...]`

We store the information this way because we aim to give it to Pandas, and, conveniently enough, giving the data in this format to Pandas allow us to create a Dataframe from it very easily.

Insert a new cell and initialize this dictionary

```python
books_dict = { 'Title': [], 'Price': [], 'Rating': [] }
```

:question: Implement a loop that will iterate over `books_html` to populate the `books_dict` dictionary by reusing all the code from above.

<details><summary markdown='span'>View solution (only <strong>after</strong> you tried it yourself!)
</summary>

In a new cell, we write the `for` loop and copy paste the code

```python
for book in books_html:
    title = book.find("h3").find("a").attrs["title"]
    price = float(book.find("p", class_="price_color").text[1:])
    rating = parse_rating(book.find("p", class_="star-rating").attrs['class'])
    books_dict["Title"].append(title)
    books_dict["Price"].append(price)
    books_dict["Rating"].append(rating)
```

</details>

Have a look at the results with the following cells:

```python
books_dict
```

```python
len(books_dict)          # You should have 3 key:value pairs
```

```python
len(books_dict["Title"]) # Each value should contain 20 elements from the 20 books, as many as on the web page!
```

## Loading data in Pandas

New section! Don't forget to create a new **Markdown cell** to document your process as you go.

The `books_dict` looks good, let's now load that data into Pandas with [`pandas.DataFrame()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html):

```python
books_df = pd.DataFrame(books_dict)
books_df
```

Looks great! Let's generate a small plot to celebrate. The plot will show how many books there are per **Rating**:

```python
books_df.groupby("Rating").count()["Title"].plot(kind="bar")
```

### Test your code!

Add and run the following cell to test your code:

```python
from nbresult import ChallengeResult

result = ChallengeResult('books',
    columns=books_df.columns,
    title=str(books_df.loc[0,'Title']),
    price=books_df.loc[0,'Price'],
    rating=books_df.loc[0,'Rating']
)
result.write()
print(result.check())
```

Then you can `commit` and `push` your code :rocket:

Quite a lot of books have a very poor rating (1). Maybe it's only the books on the first page? What about the **other** pages? Time to look at page 2 and beyond!

## Going through _all_ the pages of the catalogue

New section! Don't forget about the **Markdown cell**.

On [books.toscrape.com](http://books.toscrape.com/), scroll down to the bottom and click on the "Next" button. Do it again. Do you see the **pattern** of the URL for the different pages?

<details><summary markdown='span'>View solution
</summary>

```python
page = 1
url = f"http://books.toscrape.com/catalogue/page-{page}.html"
url
```

</details>

We need another `for` loop! Basically a loop which will iterate from page `1` to `50` and do the scraping. While we are testing, let's just focus on scraping from page 1 to 3:

```python
MAX_PAGE = 3
for page in range(1, MAX_PAGE + 1):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    print(url)
```

Seems like the loop is working! Let's replace the `print` with the actual code to scrape. Then run another `for` loop to scrape **all** the books from the **current** page. All the code is already in your notebook. Time to pick it up and glue everything together!


<details><summary markdown='span'>View solution
</summary>

```python
all_books_dict = { 'Title': [], 'Price': [], 'Rating': [] }

MAX_PAGE = 50
for page in range(1, MAX_PAGE + 1):
    print(f"Parsing page {page}...")
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    for book in soup.find_all("article", class_="product_pod"):
        title = book.find("h3").find("a").attrs["title"]
        price = float(book.find("p", class_="price_color").text[1:])
        rating = parse_rating(book.find("p", class_="star-rating").attrs["class"])
        all_books_dict["Title"].append(title)
        all_books_dict["Price"].append(price)
        all_books_dict["Rating"].append(rating)

print("Done!")
```

</details>

All good? Check that you actually parsed `MAX_PAGE` * 20 books with:

```python
len(all_books_dict["Title"])
```

Time to load the `all_books_dict` into a Pandas `DataFrame`:

```python
all_books_df = pd.DataFrame.from_dict(all_books_dict)
all_books_df.tail()
```

Let's see how expensive the books are:

```python
all_books_df["Price"].hist()
```

And how well rated they are:

```python
all_books_df.groupby("Rating").count()["Title"].plot(kind="bar")
```

## Saving the data for later

Right now, all the scraped data is living **in memory** of the Notebook, and will be lost as soon as we quit our notebook or restart the kernel. That would be a shame, so a good practice is to actually save the results of a successful scraping session into a file.

For that we will use one of the [**writers**](https://pandas.pydata.org/docs/user_guide/io.html) Pandas provide. We can write a `DataFrame` to disk like this:

```python
all_books_df.to_csv("books.csv")
```

If you'd rather have a regular Excel file, it's possible!

```bash
pip install XlsxWriter
```

```python
all_books_df.to_excel('books.xlsx', sheet_name='Books')
```

A good practice is to create a **Data Pipeline** where one process will scrape and dump the Data to CSV, and another one will read back the data from the CSV file and go on to analyze it through a Pandas Dataframe!

:bulb: Don't forget to **push your code to GitHub**

## A word on refactoring

We wrote quite a lot of code that does different things. A good practice would be to **refactor** all this code in smaller, easier to read, functions that we can reuse:

- A function `fetch_page` that fetches one page and turns it into a `soup`
- A function `add_books_to_dict` that takes the `soup` for one page, and extracts all the books' information into a dictionary
- A function `create_books_df` that iterates over a `max_page` number of pages, uses the previous two functions to extract all the data, and stores that into a DataFrame.

If you have time, try to refactor your code like this before you move on to the optional challenges.

If not, do have a look at the solution once it's available and see how this improves the readability of the code!
