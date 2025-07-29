# Python Learning Repository

This repository contains various Python topics and examples for learning purposes.

## Topics Covered

### Tuples
- **[tuples_example.py](Tuples/tuples_example.py)**: Demonstrates tuple creation, accessing elements, immutability, unpacking, and other tuple operations.

### Duck Typing
- **[birds_v1.py](Duck_Typing/birds_v1.py)**: Basic implementation of duck typing.
- **[birds_v2.py](Duck_Typing/birds_v2.py)**: Advanced implementation of duck typing.
- **[birds_v3.py](Duck_Typing/birds_v3.py)**: Using Abstract Base Classes
- **[main.py](Duck_Typing/main.py)**: Example usage of duck typing.

### Structural Pattern Matching
- **[pattern_matching_v1.py](structural_pattern_matching/pattern_matching_v1.py)**: Basic pattern matching examples.
- **[repl_v1.py](structural_pattern_matching/repl_v1.py)**: REPL implementation with pattern matching (version 1).
- **[repl_v2.py](structural_pattern_matching/repl_v2.py)**: REPL implementation with pattern matching (version 2).
- **[constant_value_patterns_enums.py](structural_pattern_matching/constant_value_patterns_enums.py)**: Pattern matching with enums.
- **[ConstantValuePatterns.jsh](structural_pattern_matching/ConstantValuePatterns.jsh)**: Java shell script for constant value patterns.

### LEGB Rule (Scope Resolution)
- **[legb_rule_basics.py](legb_rule/legb_rule_basics.py)**: Explains the LEGB (Local, Enclosing, Global, Built-in) rule with examples.
- **[global_keyword.py](legb_rule/global_keyword.py)**: Demonstrates the use of the `global` keyword.
- **[nonlocal_keyword.py](legb_rule/nonlocal_keyword.py)**: Demonstrates the use of the `nonlocal` keyword.
- **[pitfalls_and_best_practices.py](legb_rule/pitfalls_and_best_practices.py)**: Common pitfalls and best practices related to variable scope.

### Thread Safety
- **[race_conditions.py](thread_safety/race_conditions.py)**: Demonstrates how threads work and how race conditions can occur when multiple threads access shared data without proper synchronization.
- **[solving_with_locks.py](thread_safety/solving_with_locks.py)**: Shows how to use threading.Lock to protect shared resources and prevent race conditions, with a comparison of results with and without locks.
- **[avoiding_deadlocks_with_rlock.py](thread_safety/avoiding_deadlocks_with_rlock.py)**: Demonstrates how deadlocks can occur with regular locks and how to use threading.RLock (reentrant lock) to avoid them, with practical examples comparing Lock vs RLock.
