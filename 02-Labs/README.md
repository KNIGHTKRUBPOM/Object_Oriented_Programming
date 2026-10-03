# 🧪 Coursework Laboratory Assignments

This directory contains laboratory assignments designed to reinforce core Object-Oriented Programming (OOP) concepts in Python.

---

## 📑 Labs Overview

### ⚔️ [Lab 01: RPG Character & Equipment System](Lab01-RPG-Character/)
- **Core Concepts**: Object Composition, Aggregation, Class Attributes, and Behavioral Methods.
- **Scenario**: Modeling an RPG character with dynamic stats (Level, HP), equipped items (`Weapon`, `Armor`), and clan affiliations (`Guild`).
- **Key Classes**:
  - `Player`: Manages player state, actions (attack, walk, jump), and equipment associations.
  - `Weapon` & `Armor`: Items with durability, damage/defense ratings, and upgrade mechanisms.
  - `Guild`: Clan association linking players with a guild leader.

---

### 🎓 [Lab 02: University Course Registration System](Lab02-Course-Registration/)
- **Core Concepts**: Data Encapsulation, Python Properties (`@property`, `@setter`), Type Checking, and Many-to-Many Associations.
- **Scenario**: A university portal managing students, course enrollments, teachers, prerequisites, and grade assignments.
- **Key Features**:
  - Strict input validation on student IDs and names.
  - Subject credit tracking and enrollment capacity.
  - Calculation of GPAs and academic standing.

---

### 🏧 [Lab 03: ATM Banking Simulation & UML Design](Lab03-ATM-Banking-System/)
- **Core Concepts**: System Architecture, UML Class Diagram Modeling, State Management, and Secure Financial Transactions.
- **Scenario**: A complete ATM banking network handling card verification, accounts, transactions, and machine cash balances.
- **Key Highlights**:
  - **UML Class Diagram**: Fully documented in Mermaid (`diagram_ATM.md`) and Draw.io (`diagram_ATM.drawio`).
  - **Classes**: `User`, `Account`, `ATMCard`, `ATMMachine`, `Bank`, `Transaction`.
  - **Operations**: PIN verification, cash deposits, cash withdrawals, transfers between accounts, daily withdrawal limits, and transaction statement logging.

---

## 🛠️ Running the Labs

Each lab can be run directly using Python:
```bash
# Run Lab 1
python 02-Labs/Lab01-RPG-Character/Lab1.py

# Run Lab 2
python 02-Labs/Lab02-Course-Registration/Lab2.py

# Run Lab 3
python 02-Labs/Lab03-ATM-Banking-System/Lab3.py
```
