# CSC-665-01-SchedgAssist
This project is a simple AI-based scheduling assistant for CSC 665.

Given:
- A weekly schedule (7 days × 48 half-hour blocks)
- A new event to schedule (duration, deadline, priority, etc.)

The system:
- Uses a heuristic "oracle" to choose an optimal time slot
- Generates synthetic training data from the oracle
- Trains ML models (e.g., Logistic Regression, Decision Tree, small NN)
- Compares a simple baseline rule vs learned models