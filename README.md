## 🚀 Key Concepts Covered

### 🧩 1. LangGraph Workflows

- **Sequential Workflow:**  
  Tasks executed one after another (e.g., blog generation, BMI calculator).

- **Parallel Workflow:**  
  Multiple nodes running simultaneously (e.g., cricket data aggregation, essay generation).

- **Conditional Workflow:**  
  Branching logic based on runtime decisions (e.g., customer support bot).

- **Persistent Workflow:**  
  Demonstrates saving and restoring workflow state.

---

## 🧠 Core LangGraph Concepts

### 🔹 State  
The **state** is the memory of the workflow.  
It stores variables, inputs, and intermediate results shared among nodes.  
LangGraph automatically updates and passes this state between nodes, enabling smooth data flow and context retention.

### 🔹 Graph 
A **graph** defines the structure of the workflow — the nodes (tasks) and edges (connections) between them.
Each node represents a step (function, model call, or logic unit).
Edges define the order of execution (sequential, parallel, or conditional).

### 🔹 HITL (Human-in-the-Loop)

LangGraph supports HITL integration, where humans can intervene at any node in the workflow.
-This is useful when:
-AI output needs human validation.
-Sensitive or high-impact decisions are involved.
-You want interactive control during workflow execution.

### 🔹 Fault Tolerance

**LangGraph** is fault-tolerant, meaning if a node fails (due to a network error or model timeout),
it can automatically retry, skip, or continue from the last successful checkpoint instead of restarting the entire process.
This ensures reliability and robustness in large-scale workflows.

###🔹 Checkpoints

Checkpoints are saved states of the workflow that allow you to:
Resume from the last successful node after a crash.
Track workflow history.
Debug or analyze intermediate steps.

## 🧰 Tech Stack

- **Python 3.11+**
- **LangGraph**
- **LangChain**
- **Streamlit**
- **Groq API / LLMs**
- **Pydantic**
- **Dotenv**

---

## 📘 Learning Outcomes

By exploring this repository, you’ll learn how to:

- Build custom AI workflows with LangGraph.  
- Use parallelism and branching in LLM pipelines.  
- Implement persistent conversational memory.  
- Compare **LangGraph** and **LangChain** practically.  
