## APP 3 – Display Products Using Flask

### Step 1: Create the Project Structure

* Create a project folder.
* Create a `templates` folder.
* Inside the `templates` folder, create an `index.html` file.
* Create an `app.py` file in the project root.

---

### Step 2: Design the Product Page

* Use AI (or any template source) to generate the HTML and CSS for a product listing page.
* Paste the generated code into `templates/index.html`.

---

### Step 3: Create the Flask Application

* Import Flask and `render_template`.
* Create a Flask application.
* Add the home (`/`) route.
* Render the `index.html` template.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

---

## Fetch Product Data from FakeStore API

### Step 4: Visit the FakeStore API

1. Search **FakeStore API** on Google.
2. Open the first result.
3. Click on **Docs**.
4. Find the **/products** endpoint.
5. Copy the API URL.
6. Paste the URL into your browser.
7. Copy the JSON data displayed.

---

## Display Products in Flask

### Step 5: Store the Data

* Open `app.py`.
* Create a variable named `products`.
* Paste the copied JSON data into the variable.

```python
products = [
    # Paste the copied JSON data here
]
```

---

### Step 6: Pass Data to the Template

```python
@app.route("/")
def home():
    return render_template("index.html", products=products)
```

---

### Step 7: Display Products Using a Jinja Loop

Add the following code inside `index.html` where you want the products to appear:

```html
{% for prod in products %}
<article class="card">
    <img src="{{ prod.get('image') }}" alt="{{ prod.get('title') }}" class="card-image">

    <div class="card-content">
        <h2 class="card-title">{{ prod.get("title") }}</h2>

        <p class="card-description">
            {{ prod.get("description") }}
        </p>

        <div class="card-footer">
            <span class="card-price">₹{{ prod.get("price") }}</span>
            <button class="btn">Add to Cart</button>
        </div>
    </div>
</article>
{% endfor %}
```

---

### Result

* The `products` variable is sent from **app.py** to **index.html**.
* The Jinja `for` loop iterates through each product.
* Each product is displayed as a separate card automatically.
* If you add or remove products from the `products` list, the page updates automatically without changing the HTML. 🚀
