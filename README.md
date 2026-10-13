# AI-governance-lab

# Enterprise AI Governance

> An open research project exploring enterprise AI governance, compliance automation, and runtime policy enforcement for AI systems.

## Overview

As organizations increasingly adopt AI assistants, LLM-powered applications, and autonomous AI agents, new challenges emerge around governance, compliance, security, and auditability.

This project explores architectural approaches for governing enterprise AI systems, beginning with document-based compliance analysis and gradually expanding toward a broader AI governance platform.

The project is built incrementally, with each module addressing a specific enterprise problem before expanding into a larger system.

---

## Current Phase: AI Compliance Engine

The first module focuses on assisting compliance teams with one specific workflow:

**Identifying compliance gaps between regulatory documents and internal company policies.**

The goal is to reduce manual document analysis through AI-assisted obligation extraction, policy comparison, and explainable reporting, while keeping final compliance decisions with human reviewers.

## Problem Statement

Compliance professionals spend significant time:

- Reading lengthy regulatory documents
- Identifying applicable obligations
- Comparing regulations with internal policies
- Detecting missing controls
- Preparing audit evidence and compliance reports

This project investigates how LLMs and retrieval techniques can assist with these tasks while maintaining transparency and explainability.

## Research Question

**Can an AI-assisted system extract regulatory obligations, compare them against enterprise policies, and generate explainable compliance gap reports?**

---

## Current Implementation

The backend foundation is operational, with PDF upload, text extraction, OCR for scanned documents, and document-processing APIs implemented and tested.

### Implemented Features

- FastAPI backend with CORS configuration for the frontend
- Interactive API documentation through Swagger UI
- PDF upload with UUID-based document identifiers
- Local PDF storage in the backend uploads directory
- Text extraction from digital PDFs using `pypdf`
- OCR for scanned PDF pages using Tesseract OCR
- PDF page rendering using PyMuPDF
- Document-processing endpoint with generated analysis IDs
- Analysis result retrieval endpoint
- Health-check endpoint

### Backend API

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health/` | Check backend availability |
| POST | `/upload/` | Upload a PDF document |
| POST | `/analysis/` | Process an uploaded document |
| GET | `/analysis/{analysis_id}` | Retrieve processing results |

**API documentation:** Available locally at `http://127.0.0.1:8000/docs` when the backend is running.

### Current Processing Workflow

```text
PDF Upload
    |
    v
Local Document Storage
    |
    v
PDF Text Extraction
    |
    +---- Digital PDF ----> pypdf
    |
    +---- Scanned PDF ----> Tesseract OCR
                               ^
                               |
                            PyMuPDF
    |
    v
Extracted Text and Metadata
    |
    v
Analysis ID Generation
    |
    v
Analysis Result Retrieval
```

**Current limitation:** The analysis endpoint currently processes documents and returns extraction statistics. Automated regulation-versus-policy comparison and compliance gap detection are not implemented yet. Analysis results are stored in memory and are lost when the backend restarts.

---

## Technology Stack

### Backend
- Python
- FastAPI
- Uvicorn
- Pydantic
- `pypdf`
- PyMuPDF
- Tesseract OCR
- `pytesseract`
- Pillow

### Frontend
- React
- Vite
- Tailwind CSS (planned/integration dependent)

### Database
- PostgreSQL (planned)

### AI Components
- OpenAI API
- Sentence Transformers
- Retrieval-Augmented Generation (RAG)

### Vector Database
- Chroma (initial prototype)
- Qdrant (future consideration)

### Infrastructure
- Docker

---

## High-Level Target Workflow

```text
Regulation PDF
       |
       v
Document Parsing and OCR
       |
       v
Regulatory Obligation Extraction
       |
       v
Structured Requirements
       |
       +----------------------+
                              |
                              v
Company Policy PDF ---> Policy Control Extraction
                              |
                              v
                       Policy Comparison
                              |
                              v
                         Gap Analysis
                              |
                              v
                  Explainable Compliance Report
```

---

## Roadmap

### Phase 1: Backend and Document Ingestion
- [x] Repository setup
- [x] FastAPI backend
- [x] React/Vite frontend setup
- [x] PDF upload endpoint
- [x] PDF text extraction
- [x] OCR for scanned PDFs
- [x] Document-processing API
- [x] Analysis result retrieval
- [x] Health-check endpoint
- [ ] PostgreSQL integration
- [ ] Persistent analysis storage

### Phase 2: Document Processing and Retrieval
- [ ] Document normalization and validation
- [ ] Text chunking
- [ ] Embedding generation
- [ ] Vector search
- [ ] Source and page-level references

### Phase 3: Structured Extraction
- [ ] Regulatory obligation extraction
- [ ] Internal policy control extraction
- [ ] Structured outputs and validation
- [ ] Extraction quality evaluation

### Phase 4: Compliance Gap Analysis
- [ ] Regulation-to-policy comparison
- [ ] Covered, partially covered, and missing classifications
- [ ] Evidence-backed findings
- [ ] Risk and confidence scoring
- [ ] Explainable compliance reports

### Phase 5: Enterprise Capabilities
- [ ] Authentication and authorization
- [ ] Role-based access control
- [ ] Audit logging
- [ ] Document versioning
- [ ] Human review workflows
- [ ] Secure document storage

### Phase 6: Broader AI Governance Research
- [ ] Runtime policy enforcement
- [ ] AI authorization layer
- [ ] AI activity monitoring
- [ ] AI risk assessment
- [ ] Governance for autonomous AI agents

---

## Long-Term Vision

The Compliance Engine is the first building block of a broader Enterprise AI Governance platform.

Future research may explore:

- Runtime governance and policy enforcement
- Authorization controls for AI agents
- AI activity and audit logging
- Human approval workflows
- AI risk scoring and monitoring
- Explainable AI governance

The long-term objective is to investigate how enterprise AI systems can operate within explicit, auditable, and enforceable governance boundaries.

---

## Project Status

🚧 **Early Research & Development**

The backend document-ingestion foundation is implemented and tested. The next milestone is to build the regulation-versus-policy comparison engine, followed by persistent storage, retrieval, and explainable reporting.

This is an evolving research and learning project. Architecture and implementation will change as the project develops and requirements become clearer.

---

## License

MIT License
