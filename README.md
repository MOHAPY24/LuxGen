 # LuxGen 🌌

LuxGen is a lightweight, procedural **map and world generator** written in Python.  
It’s designed to be simple, configurable, and flexible, letting you generate endless ASCII or symbolic maps with your own set of materials.

---

## ✨ Key Features
- **Customizable Materials**: Define your own objects (stone, water, grass, etc.) with symbolic and numeric representations.
- **Deterministic Worlds**: Generation is based on a configurable seed, so worlds are reproducible.
- **Dynamic World Rules**: Special conditions (like alternating water, rare caves, etc.) can be programmed directly in the generator.
- **Export Option**: Save generated maps into `.map` files for sharing or post-processing.
- **Numeric + Symbol Worlds**: Access both symbolic (`⬜`, `🌿`, `~`) and numeric representations of the same map.

---

## ⚙️ Installation


Simply copy `luxgen.py` into your project.  
Make sure you also create a `luxconf.json` file in the same directory (see below).

---

## 🔧 Configuration

The generator reads configuration values from `luxconf.json`:

```json
{
  "world_len": 50,
  "seed": 12345,
  "max_objects": 20,
  "map_save": true
}
````

* `world_len` → Size of the world (number of tiles/slots to generate).
* `seed` → Random seed (controls reproducibility).
* `max_objects` → Maximum allowed unique materials. Prevents overpopulation of object types.
* `map_save` → If true, the generated world is saved to a `map.map` file.

---

## 🧱 Defining Materials

Materials are declared using the `material` class:

```python
from luxgen import material

stone = material("Stone", 1, "⬜")
water = material("Water", 2, "~")
grass = material("Grass", 3, "🌿")
```

* `material_name`: Name of the object.
* `material_numeric_value`: Numeric identifier (useful for algorithms).
* `material_repr`: Symbol or character representing it in the world.

---

## 🌍 Generating a World

```python
from luxgen import generator, material

stone = material("Stone", 1, "⬜")
water = material("Water", 2, "~")
grass = material("Grass", 3, "🌿")

world = []
gen = generator(materials=[stone, water, grass], world=world)

print(gen.generate())
```

This produces a procedurally generated map, e.g.:

```
🌿 ⬜ ~ ~ 🌿 ~ ⬜ ⬜ 🌿 ⬜ 🌿 🌿 ⬜ ⬜ ~ 🌿 ~ 🌿 ⬜
```

---

## 🛠 Adding Dynamic Materials

LuxGen already includes **basic rules** for special materials inside `generator.generate()`:

* **Water (`#`)**: Toggles between appearing and disappearing each time it is encountered.
* **Caves (`^`)**: Appear only occasionally (1 in 5 chance).

If you add new materials with **dynamic behavior** (like lava that spreads, forests that cluster, etc.),
you’ll need to **edit the main `luxgen.py` file** inside the `generator.generate()` method.

Example (inside `generate` function):

```python
if random_repr == "~":  # your symbol for water
    if water is True:
        water = False
    else:
        water = True

if random_repr == "^":  # your symbol for caves
    choice = random.randint(1, 5)
    if choice != 5:
        random_material = random.choices(self.valid_materials)
        random_repr = str(random_material)[1]
```

To add your own rules:

1. Assign a **unique symbol** for the material (e.g., `"🔥"` for lava).
2. Add a condition inside `generate()` checking for that symbol.
3. Define the behavior (e.g., skip, duplicate, cluster, toggle).

---

## 💡 Use Cases

### 1. **Game Prototyping**

Use LuxGen to rapidly prototype 2D maps for roguelikes, exploration games, or text-based adventures.

Example:

```python
for row in range(10):  # print 10 rows of 50 tiles
    print("".join(gen.generate()))
```

### 2. **Simulation / Modeling**

Model resource distribution (water, trees, stone, etc.) for simple ecology or survival simulations.

### 3. **Teaching Procedural Generation**

LuxGen is simple enough for students to study how **seeds, randomness, and object placement rules** create complex worlds.

### 4. **ASCII Art Worlds**

Generate aesthetically pleasing ASCII landscapes for creative projects.

---

## 📦 Files in Project

* **`luxgen.py`** → Core generator logic.
* **`luxconf.json`** → Config file with world parameters.
* **`map.map`** → Output file (if saving enabled).

---

## 📚 Guide: Adding New Dynamic Materials

Here’s how you can extend LuxGen with custom world rules.

### Step 1: Define your material

```python
lava = material("Lava", 4, "🔥")
```

### Step 2: Add it to your generator

```python
gen = generator(materials=[stone, water, grass, lava], world=[])
```

### Step 3: Edit `luxgen.py` inside `generator.generate()`

Add custom behavior:

```python
if random_repr == "🔥":  # lava behavior
    # Lava spreads: if the previous tile was also lava, force this tile to lava too
    if len(self.world) > 0 and self.world[-1] == "🔥":
        random_repr = "🔥"
```

This ensures lava “flows” in clusters instead of being totally random.

---

## 🧪 Examples

### Example 1: Water that expands

```python
if random_repr == "~":
    if len(self.world) > 0 and self.world[-1] == "~":
        # 70% chance the next tile is also water
        if random.randint(1, 10) <= 7:
            random_repr = "~"
```

### Example 2: Forests that clump

```python
if random_repr == "🌲":
    # Trees have a 50% chance to appear next to other trees
    if len(self.world) > 0 and self.world[-1] == "🌲":
        if random.randint(0, 1) == 1:
            random_repr = "🌲"
```

### Example 3: Rare treasure

```python
if random_repr == "💎":
    # Treasure only appears once every 100 tiles
    if random.randint(1, 100) != 1:
        random_repr = str(random.choice(self.valid_materials))[1]
```

---

## 📜 License

Licensed under **GPL-3.0**.
You are free to use, modify, and distribute LuxGen — just keep it open source.

---

> “Every world begins with a seed… what will yours grow into?”

```
