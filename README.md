# Python Pipelines

This repository provides a blueprint for building flexible, testable, and extensible data pipelines in Python. It showcases a modern software engineering approach using **Dependency Injection** with Python's `typing.Protocol` to create modular and interchangeable pipeline components.

The core idea is to decouple the main pipeline logic from the concrete implementations of its parts (e.g., data loading, exporting). This makes the system highly configurable and easy to test.

### Key Concepts Demonstrated

*   **Dependency Injection:** Instead of hard-coding dependencies, they are "injected" into the pipeline at runtime.
*   **Protocols as Interfaces:** `typing.Protocol` is used to define contracts (interfaces) that components must adhere to. This allows for type-safe, swappable implementations without relying on class inheritance.
*   **Configurable Execution:** The `triggers` script shows how to dynamically select and run the pipeline with different components, such as choosing between exporting to a file, a database, or not exporting at all.

This structure makes it simple to:
*   **Test Components in Isolation:** You can easily substitute mock objects that conform to a protocol for unit testing.
*   **Extend Functionality:** Adding a new data source or export destination is as simple as creating a new function that matches the required protocol and updating the configuration.
*   **Run in Different Environments:** Effortlessly switch between components for development (e.g., loading local sample data) and production (e.g., loading from a live database).

# UV Commands

```bash
# init repo
uv init

# create env
uv venv

# list packages in env
uv pip list

# install package editable
uv pip install -e .

# install dev dependency
uv add --dev pytest

# create lock file
uv lock
```
