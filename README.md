# 🧩 Two Sum Problem — Clean & Efficient Python Solutions  

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Tests](https://img.shields.io/badge/Tests-Pytest-green?logo=pytest)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A concise yet powerful demonstration of **algorithmic problem-solving** in Python.  
This project showcases both the **naive O(n²)** and **optimized O(n)** solutions to the classic *Two Sum* problem, built with professional code structure, clarity, and full automated testing.

---

## 🚀 Project Overview  

The **Two Sum** problem asks:  
> Given an array of integers and a target value, return the indices of the two numbers that add up to that target.

This repository implements two distinct approaches:

| Approach | Description | Time Complexity |
|-----------|--------------|------------------|
| 🔁 **Naive Algorithm** | Checks all possible pairs using nested loops. | O(n²) |
| ⚡ **Hash Map Algorithm** | Stores complements in a dictionary for O(1) lookups. | O(n) |

Each version is fully typed, documented, and covered by unit tests written with `pytest`.

---

## 🧠 What This Project Demonstrates  

- Deep understanding of **algorithm optimization** and computational efficiency.  
- Clean, maintainable Python code following **PEP 8** and good naming practices.  
- Experience with **unit testing**, modularization, and reproducible structure.  
- A data-driven, problem-solving mindset — from exploration to refinement.  

---

## 📁 Project Structure  

two_sum_problem/
├── init.py
├── naive_algorithm.py # O(n²) nested-loop approach
├── hash_map_approach.py # O(n) optimized hash-map solution
└── tests/
├── test_naive_algorithm.py # Tests for naive solution
└── test_hash_map_two_sum.py# Tests for optimized solution



---

## 💡 Example Usage  


from hash_map_approach import hash_map_two_sum
from naive_algorithm import naive_algorithm_two_sum

print(hash_map_two_sum([2, 7, 11, 15], 9))   # ➜ [0, 1]
print(naive_algorithm_two_sum([3, 3], 6))    # ➜ [0, 1]


---
## 🧪 Running Tests
```python
pip install pytest
cd two_sum_problem
pytest -q
```
---
## ✅ Example Output:
....
4 passed in 0.01s

---

## ⚙️ Technologies Used

Language: Python 3.12

Testing: pytest

Typing: Python typing (List, Dict)

Style: PEP 8 with meaningful variable names and docstrings

---
## 📘 Learning Journey

When I began this project, I started with the naive approach a straightforward double loop that checks every pair of numbers. It worked fine for small arrays but quickly became inefficient as the list grew.

Curiosity led me to analyze its time complexity (O(n²)), and I challenged myself to optimize it.
By introducing a hash map (dictionary), I learned to track complements in real-time, cutting the complexity down to O(n) while maintaining clarity and correctness.

Through iterative testing and refactoring, I gained hands-on experience with:

- Algorithmic thinking, recognizing patterns and trade-offs.

- Optimization techniques, using data structures to reduce runtime.

- Test-driven development,  verifying correctness through every iteration.

This journey reflects my growth as a developer: not just solving problems, but improving how I solve them.

---
## 💼 Why This Project Matters

This small project captures what I value in software engineering:

- Writing elegant, efficient solutions to complex problems.

- Building maintainable, testable, and reusable code.

- Thinking like a problem-solver, not just a coder.

---
## 👨‍💻 About the Developer

Lina Chioma Anaso
Software Engineering Student • Future Full-Stack Developer

I’m passionate about writing clean, efficient, and purposeful code.
This project is part of my continuous journey to master algorithms, data structures, and modern development practices.


## 📫 **Connect with me:**
[LinkedIn](https://linkedin.com/in/lina-chiom-anaso)
**linkedin.com/in/lina-chioma-anaso**

**github.com/Chiomalina**

---
## 🧾 License

MIT License — free to use, learn from, and build upon.