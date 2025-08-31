# 🌲 LuxGen – Lightweight Procedural Map Generator

```
        🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲
      🌲🌲      L U X G E N      🌲🌲
     🌲🌲🌲   Procedural Forest   🌲🌲🌲
      🌲🌲     Worlds Await      🌲🌲
        🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲🌲
```

LuxGen is a **lightweight Python-based world/map generator** that builds procedural worlds with materials you define.
It’s designed for **games, simulations, experiments, and creative coding**.

---

## ✨ Features

* 📄 **Config-driven** → Easy to set world size, seed, and object limits via `luxconf.json`.
* 🌍 **1D & 2D Maps** → Fully supports both 1D linear worlds *and* 2D layered maps (already working, see `map = [gen1, gen2]` in code).
* 🧱 **Custom Materials** → Define your own tiles with names, numeric IDs, and symbols.
* 🎲 **Seeded Randomness** → Reproducible maps every time with the same seed.
* 🔢 **Dual Outputs** → Print **visual** maps (`T ~ #`) or **numeric** ones (`4 1 3`).
* 🌿 **Biome System (coming soon)** → Group materials into biomes like forest, cave, desert.
* 💧 **Detection System (coming soon)** → Detect water clusters to form lakes, ponds, rivers.
* 💾 **Map Saving (coming soon)** → Save generated maps to `.map` files for reuse.

---

## ⚙️ Example `luxconf.json`

```json
{
  "world_len": 20,
  "seed": 123456,
  "max_objects": 50
}
```

---

## 🧱 Defining Materials

```python
materials_list.append(material("Moss", 1, "~"))
materials_list.append(material("Tree", 2, "T"))
materials_list.append(material("Water", 3, "#"))
materials_list.append(material("Cave", 4, "^"))
```

---

## 🚀 Example Output

### 1D World:

```
T ~ # * ~ ^ ~ T ~ ~ * # T
```

### Numeric View:

```
2 1 3 5 1 4 1 2 1 1 5 3 2
```

### 2D World (already working in code):

```
T ~ # * ~ ^ ~ T ~ ~
T T # ^ ~ * ~ ~ ~ ~
```

---

## 🔧 Use Cases

* 🎮 **Game Development** → Build maps for roguelikes, survival games, or text adventures.
* 🧪 **Simulations** → Procedural environments for AI/pathfinding experiments.
* 🏗 **Prototyping** → Test terrain generation ideas before building a bigger engine.
* 🎲 **Random Worlds** → Generate endless landscapes with just a few materials.

---

## 🛠 Roadmap

* ✅ **Basic 1D maps**
* ✅ **2D map support** (already in place, just expand `map = [gen1, gen2]`)
* 🔲 **Biome system** (forest, desert, cave, etc.)
* 🔲 **Water/pond detection** → cluster water into lakes & rivers
* 🔲 **.map export** → Save maps for external use
* 🔲 **Noise-based generation** → More natural terrain flow

---

## 📦 Quickstart

```bash
git clone https://github.com/MOHAPY24/luxgen
cd luxgen
python3 luxgen.py
```

---

## 📜 License

This project is licensed under the **GNU GPL 3.0 License**.
You are free to run, study, share, and modify this software, but **derivatives must also be open-sourced** under the same license.

---

🌲 **LuxGen – Build infinite forests, caves, and worlds with just a few lines of Python.**
