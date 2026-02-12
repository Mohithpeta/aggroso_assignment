# AI_NOTES.md

## Use of AI Assistance

AI was used as a **support tool during development**, not to generate the final solution end-to-end.

### What AI Was Used For
- Clarifying requirements and edge cases around text-file ingestion and parsing.
- Suggestions for structuring the input-processing pipeline (validation → parsing → transformation).
- Drafting initial utility functions for text handling and cleanup.
- Prompt-level experimentation to understand how parsed text should be formatted before being sent to the model.
- General guidance on error handling and defensive checks for malformed input files.

### What Was Done and Verified Manually
- Final design of the file-input flow and processing logic.
- Validation rules for uploaded / provided text files.
- Parsing, chunking, and preprocessing logic.
- Integration of the parsed text with the backend flow.
- Manual testing with different file sizes, encodings, and malformed inputs.
- Verification of outputs for correctness, consistency, and edge cases.

All core logic and final behavior were implemented and validated manually.

---

## LLM and Provider

- **LLM Used:** GPT-4–class model  
- **Provider:** OpenAI  

### Why This LLM Was Chosen
- Reliable reasoning over user-provided text input.
- Strong performance on summarization, transformation, and structured output generation.
- Stable API and predictable behavior during development.

The LLM is only used **after preprocessing**, and receives sanitized, controlled input. It does not directly read files or access the filesystem.

---

## Notes
- AI suggestions were treated as advisory.
- Final responsibility for correctness and system behavior lies with the developer.