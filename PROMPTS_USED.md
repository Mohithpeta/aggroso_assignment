# PROMPTS_USED.md

This file records representative prompts used during development of the text-file input application.
Only developer prompts are listed. No AI responses, API keys, or runtime prompts are included.

---

## Project Kickoff

- “This is the requirement. Based on this, give me a clean folder structure for the app.”
- “Assume this is a small backend-focused project. Keep the structure simple and scalable.”
- “What files should exist on day one?”

---

## Backend Setup & Flow

- “Help me design the backend flow for accepting a text file as input.”
- “Where should file validation, parsing, and processing live in the folder structure?”
- “What should be handled before calling the LLM vs after?”

---

## Docker & Environment

- “Help me write a Dockerfile for this app.”
- “What should go into .dockerignore?”
- “How do I keep the Docker image minimal and predictable?”
- “How should environment variables be passed when running the container?”

---

## Text File Handling

- “How do I safely accept and read a text file from the user?”
- “What edge cases should I expect with text files?”
- “How should encoding issues be handled?”
- “What is a reasonable file size limit?”

---

## Preprocessing & Chunking

- “How should a large text file be chunked before sending to an LLM?”
- “Should chunking be character-based or token-based?”
- “Where should chunking logic live in the codebase?”

---

## Prompt Construction

- “How should user-provided text be framed in a prompt?”
- “How do I avoid prompt injection when the input comes from a file?”
- “What guardrails should be added around file-based inputs?”

---

## Error Handling

- “What errors should be returned if the file is empty or malformed?”
- “How should errors be surfaced without leaking internals?”
- “What should happen if the LLM fails or returns invalid output?”

---

## Testing & Verification

- “What test cases should I manually run for this app?”
- “What inputs are most likely to break a naive implementation?”
- “How do I verify correctness across repeated runs?”

---

## Documentation

- “Write a short README explaining what works and what doesn’t.”
- “Create an AI_NOTES.md explaining what AI was used for.”
- “Create a PROMPTS_USED.md listing the prompts used during development.”

---

## Notes

- Prompts were used during design and development only.
- All implementation, testing, and final decisions were done manually.
- AI outputs were treated as suggestions and verified before use.