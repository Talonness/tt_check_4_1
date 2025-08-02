# 📚 Abstract Base Classes (ABC) and Type Hints Tutorial for SQA Students

## 🎯 Learning Objectives
By the end of this tutorial, you will understand:
- What Abstract Base Classes (ABC) are and why they're important for testing
- How `@abstractmethod` enforces contracts in code
- How type hints with `List` improve code quality and testing
- Real-world applications in software quality assurance

---

## 🔍 What is an Abstract Base Class (ABC)?

An **Abstract Base Class** is like a blueprint or contract that defines what methods a class MUST have, but doesn't implement them. Think of it like a job description - it tells you what skills you need, but you have to actually learn those skills yourself.

### 🏗️ Why Use ABC in Testing?

In software testing, we often need to test different implementations of the same interface. ABC helps us ensure:
- **Consistency**: All implementations have the same methods
- **Testability**: We can write tests that work with any implementation
- **Quality**: Missing methods are caught early, not in production

---

## 🛠️ Basic ABC Example

```python
from abc import ABC, abstractmethod

# This is our "contract" or "interface"
class DataStorage(ABC):
    """Abstract class defining how data storage should work"""
    
    @abstractmethod
    def save_data(self, data):
        """Every storage class MUST implement this method"""
        pass
    
    @abstractmethod
    def load_data(self):
        """Every storage class MUST implement this method"""
        pass
```

---

## ⚠️ What Happens If You Don't Follow the Contract?

Let's see what happens when someone tries to create an incomplete implementation:

```python
# ❌ This class is INCOMPLETE - missing load_data()
class BrokenStorage(DataStorage):
    def save_data(self, data):
        print(f"Saving: {data}")
    # Missing load_data() method!

# This will FAIL:
try:
    storage = BrokenStorage()  # TypeError!
except TypeError as e:
    print(f"Error: {e}")
    # Output: Can't instantiate abstract class BrokenStorage 
    # without an implementation for abstract methods 'load_data'
```

**🎓 Key Learning**: Python prevents you from creating broken objects!

---

## ✅ Correct Implementation

```python
# ✅ This class is COMPLETE - implements all required methods
class FileStorage(DataStorage):
    def save_data(self, data):
        with open("data.txt", "w") as f:
            f.write(data)
    
    def load_data(self):
        with open("data.txt", "r") as f:
            return f.read()

class DatabaseStorage(DataStorage):
    def save_data(self, data):
        # Save to database
        print(f"Saving to DB: {data}")
    
    def load_data(self):
        # Load from database
        return "data from database"

# ✅ Both work because they implement the contract:
file_storage = FileStorage()      # Works!
db_storage = DatabaseStorage()    # Works!
```

---

## 🔢 Understanding Type Hints with `List`

Type hints tell other developers (and testing tools) what types of data your functions expect and return.

### 📝 Basic Type Hints

```python
from typing import List

def process_numbers(numbers: List[int]) -> int:
    """
    Args:
        numbers: A list of integers
    Returns:
        The sum of all numbers
    """
    return sum(numbers)

# Usage examples:
result = process_numbers([1, 2, 3, 4])  # ✅ Correct: List of int
# process_numbers("hello")               # ❌ Wrong: String, not List[int]
```

### 🧪 Why Type Hints Matter in Testing

```python
from typing import List, Optional

class TaskRepository(ABC):
    @abstractmethod
    def get_all_tasks(self) -> List[dict]:
        """Returns a list of task dictionaries"""
        pass
    
    @abstractmethod
    def get_task_by_id(self, task_id: int) -> Optional[dict]:
        """Returns a task dict or None if not found"""
        pass
```

**Benefits for Testing:**
- **Clear Expectations**: Testers know exactly what data to expect
- **Better Test Data**: You know to create `List[dict]` for test inputs
- **IDE Support**: Your editor can catch type errors before running tests
- **Documentation**: Type hints serve as living documentation

---

## 🎯 Real-World Example: Task Repository Pattern

Let's look at a real example from your codebase:

```python
from abc import ABC, abstractmethod
from typing import List, Optional

class TaskRepository(ABC):
    """Contract for all task storage implementations"""
    
    @abstractmethod
    def load_tasks(self) -> List[dict]:
        """Load all tasks as dictionaries"""
        pass
    
    @abstractmethod
    def save_tasks(self, tasks: List[dict]) -> None:
        """Save a list of task dictionaries"""
        pass
    
    @abstractmethod
    def get_task_by_id(self, task_id: int) -> Optional[dict]:
        """Get one task by ID, or None if not found"""
        pass

# Implementation 1: File-based storage
class FileTaskRepository(TaskRepository):
    def load_tasks(self) -> List[dict]:
        # Read from JSON file
        return [{"id": 1, "title": "Learn Python"}]
    
    def save_tasks(self, tasks: List[dict]) -> None:
        # Write to JSON file
        pass
    
    def get_task_by_id(self, task_id: int) -> Optional[dict]:
        # Search in file
        return {"id": task_id, "title": "Found task"}

# Implementation 2: Database storage
class DatabaseTaskRepository(TaskRepository):
    def load_tasks(self) -> List[dict]:
        # Query database
        return [{"id": 1, "title": "Learn SQL"}]
    
    def save_tasks(self, tasks: List[dict]) -> None:
        # Insert into database
        pass
    
    def get_task_by_id(self, task_id: int) -> Optional[dict]:
        # Database query
        return {"id": task_id, "title": "DB task"}
```

---

## 🧪 How This Helps in Testing

### 1. **Consistent Test Interface**
```python
def test_repository_loads_tasks(repository: TaskRepository):
    """This test works with ANY repository implementation!"""
    tasks = repository.load_tasks()
    assert isinstance(tasks, list)  # Type hint tells us it's a List
    
    if tasks:  # If not empty
        assert isinstance(tasks[0], dict)  # Type hint tells us it's List[dict]

# Run the same test with different implementations:
test_repository_loads_tasks(FileTaskRepository())
test_repository_loads_tasks(DatabaseTaskRepository())
```

### 2. **Better Test Data Creation**
```python
def create_test_tasks() -> List[dict]:
    """Type hint tells us exactly what this function returns"""
    return [
        {"id": 1, "title": "Test task 1", "completed": False},
        {"id": 2, "title": "Test task 2", "completed": True}
    ]

def test_save_tasks():
    repo = FileTaskRepository()
    test_data = create_test_tasks()  # We know this returns List[dict]
    repo.save_tasks(test_data)       # Perfect match for the type hint!
```

### 3. **Early Error Detection**
```python
# ❌ Type checker will warn you about this:
def broken_test():
    repo = FileTaskRepository()
    repo.save_tasks("not a list")  # Expected List[dict], got str
    
# ✅ Type checker approves this:
def good_test():
    repo = FileTaskRepository()
    repo.save_tasks([{"id": 1, "title": "Valid"}])  # Correct type!
```

---

## 📊 Common Type Hints for Testing

| Type Hint | What It Means | Example |
|-----------|---------------|---------|
| `List[int]` | List of integers | `[1, 2, 3, 4]` |
| `List[str]` | List of strings | `["apple", "banana"]` |
| `List[dict]` | List of dictionaries | `[{"name": "John"}, {"name": "Jane"}]` |
| `Optional[str]` | String or None | `"hello"` or `None` |
| `bool` | True or False | `True` or `False` |
| `None` | Returns nothing | Function that doesn't return a value |

---

## 🎓 Best Practices for SQA Students

### ✅ Do This:
```python
from abc import ABC, abstractmethod
from typing import List, Optional

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Clear method signature with types"""
        pass
    
    @abstractmethod
    def get_transaction_history(self) -> List[dict]:
        """Returns list of transaction dictionaries"""
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        # Implement credit card logic
        return True
    
    def get_transaction_history(self) -> List[dict]:
        return [{"id": 1, "amount": 100.0, "status": "completed"}]
```

### ❌ Avoid This:
```python
# No ABC - no contract enforcement
class PaymentProcessor:
    def process_payment(self, amount):  # No type hints
        pass

# Incomplete implementation
class BrokenProcessor(PaymentProcessor):
    pass  # Missing methods, but Python won't catch it!
```

---

## 🔬 Testing Strategy with ABC

```python
import pytest
from typing import List

class TestAnyTaskRepository:
    """Tests that work with ANY TaskRepository implementation"""
    
    @pytest.fixture(params=[FileTaskRepository, DatabaseTaskRepository])
    def repository(self, request):
        """Test with all repository types"""
        return request.param()
    
    def test_load_tasks_returns_list(self, repository: TaskRepository):
        """Verify the contract is followed"""
        tasks = repository.load_tasks()
        assert isinstance(tasks, list)
    
    def test_save_and_load_tasks(self, repository: TaskRepository):
        """Test the full cycle"""
        test_tasks: List[dict] = [
            {"id": 1, "title": "Test", "completed": False}
        ]
        repository.save_tasks(test_tasks)
        loaded_tasks = repository.load_tasks()
        assert len(loaded_tasks) > 0
```

---

## 🎯 Key Takeaways for SQA Students

1. **ABC = Contract Enforcement**: Ensures all implementations have required methods
2. **Type Hints = Clear Expectations**: Makes testing requirements obvious
3. **Better Test Design**: You can write tests that work with multiple implementations
4. **Early Bug Detection**: Type errors caught before runtime
5. **Living Documentation**: Code tells you exactly what it expects

---

## 💡 Practice Exercises

### Exercise 1: Create a Logger ABC
```python
from abc import ABC, abstractmethod
from typing import List

class Logger(ABC):
    @abstractmethod
    def log_message(self, message: str) -> None:
        pass
    
    @abstractmethod
    def get_logs(self) -> List[str]:
        pass

# TODO: Implement FileLogger and ConsoleLogger
```

### Exercise 2: Test the Logger
```python
def test_logger_interface(logger: Logger):
    # TODO: Write a test that works with any Logger implementation
    pass
```

---

## 🔗 Additional Resources

- [Python ABC Documentation](https://docs.python.org/3/library/abc.html)
- [Python Typing Module](https://docs.python.org/3/library/typing.html)
- [Real Python: Type Checking](https://realpython.com/python-type-checking/)

---

**Remember**: ABC and type hints make your code more reliable, testable, and maintainable - exactly what we want in quality software! 🚀
