
# Confidential Employee Salary Benchmarking System  
### Using Multi-Party Computation and Functional Encryption  

---

## Project Overview

This project is a software engineering prototype that demonstrates how multiple companies can collaboratively benchmark employee salaries without revealing any individual salary data.

The system computes global statistics (average, median, minimum, maximum ....) while preserving confidentiality at every stage of the computation.

The prototype combines two cryptographic concepts:

- Multi-Party Computation (MPC) for secure computation  
- Functional Encryption (FE) for restricted access to results  

Cryptographic mechanisms are simulated for educational purposes, but the architecture and security guarantees follow real-world designs.

---

## Objectives

- Prevent disclosure of individual salaries  
- Allow collaborative statistical analysis  
- Separate trust between multiple entities  
- Demonstrate end-to-end data confidentiality  

---

## System Architecture

The system is composed of three main actors:

### 1️⃣ Enterprise Client

- Holds raw salary data locally  
- Splits data using MPC secret sharing  
- Encrypts data before transmission  
- Never sends plaintext salaries  

### 2️⃣ MPC Node (Intermediate)

- Receives secret shares only  
- Performs aggregation directly on shared data  
- Cannot reconstruct individual salaries  
- Outputs encrypted aggregated results  

### 3️⃣ Result Server

- Manages Functional Encryption keys  
- Decrypts only authorized statistics  
- Generates the final benchmarking report  

---

## Data Flow

Raw Salaries
↓
MPC Secret Sharing (Enterprise)
↓
Secure Aggregation (MPC Node)
↓
Encrypted Statistical Result
↓
Functional Decryption (Authorized Only)
↓
Benchmarking Report




---

## Security Design

### Multi-Party Computation (MPC)

- Protects sensitive data during computation  
- No single entity has access to full data  
- Intermediate nodes operate on fragments only  

### Functional Encryption (FE)

- Protects sensitive data after computation  
- Decryption keys are limited to specific functions  
- Prevents unauthorized access to raw or derived data  

**MPC secures the computation, FE secures the output.**

---

## Project Structure



enterprise_client/
Handles salary input, MPC fragmentation, and encryption

intermediate_part/
Performs secure aggregation on secret shares

server_part/
Applies Functional Encryption and generates reports

utils/
Shared utility functions

website/
Show data analysis


---

## Limitations

....................

....................

....................

---

## Conclusion

This prototype demonstrates that confidential salary benchmarking is feasible using modern cryptographic paradigms. By combining MPC and Functional Encryption, the system ensures data privacy throughout the entire lifecycle of computation and result disclosure.


