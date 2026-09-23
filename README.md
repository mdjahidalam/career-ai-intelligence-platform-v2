# 🚀 Career AI Intelligence Platform V2

> An AI-powered Career Intelligence Platform for resume analysis, ATS evaluation, placement prediction, salary prediction, career guidance, AI career assistance, resume optimization, and AI-powered resume generation.

---

# 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Project Objective](#-project-objective)
- [Key Features](#-key-features)
- [Application Walkthrough](#-application-walkthrough)
  - [Authentication](#1-authentication)
  - [Dashboard](#2-dashboard)
  - [Resume Management](#3-resume-management)
  - [AI Resume Analysis](#4-ai-resume-analysis)
  - [AI Report](#5-ai-report)
  - [Career AI Assistant](#6-career-ai-assistant)
  - [Chat History](#7-chat-history)
  - [Real-Time AI Streaming](#8-real-time-ai-streaming)
  - [AI Resume Studio](#9-ai-resume-studio)
  - [Profile](#10-profile)
  - [Settings](#11-settings)
  - [Swagger API](#12-swagger-api)
- [AI Architecture](#-ai-architecture)
- [AI Agents](#-ai-agents)
- [Resume Intelligence Pipeline](#-resume-intelligence-pipeline)
- [System Architecture](#-system-architecture)
- [Backend Architecture](#-backend-architecture)
- [Database Architecture](#-database-architecture)
- [Authentication Architecture](#-authentication-architecture)
- [Career Assistant Architecture](#-career-assistant-architecture)
- [AI Provider Architecture](#-ai-provider-architecture)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Environment Variables](#-environment-variables)
- [Database Setup](#-database-setup)
- [Running the Project](#-running-the-project)
- [Testing](#-testing)
- [Security](#-security)
- [Engineering Concepts](#-engineering-concepts)
- [Current Implementation](#-current-implementation)
- [Future Scope](#-future-scope)
- [Author](#-author)

---

# 🎯 Overview

**Career AI Intelligence Platform V2** is a full-stack AI-powered career platform designed to help students understand their career profile and make better-informed career decisions.

The platform combines:

- Resume Intelligence
- ATS Analysis
- Skill Analysis
- Placement Prediction
- Salary Prediction
- Career Recommendation
- Interview Assistance
- AI Career Chat
- Resume Optimization
- AI Resume Generation

into a single application.

The project follows a modular architecture where the frontend communicates with a FastAPI backend through REST APIs and Server-Sent Events, while the backend manages authentication, database operations, resume processing, AI agents, and AI provider integration.

---

# 💡 Problem Statement

Students generally use different tools for:

- Resume analysis
- ATS checking
- Career guidance
- Salary estimation
- Placement preparation
- Interview preparation
- Resume improvement

These tools are often disconnected from each other.

The goal of this project is to bring these career-related capabilities together into a single personalized platform.

---

# 🎯 Project Objective

The primary objectives are:

1. Analyze student resumes using AI.
2. Extract useful career information from resumes.
3. Provide ATS-related analysis.
4. Provide placement-related predictions.
5. Provide salary-related predictions.
6. Recommend suitable career directions.
7. Provide an AI-powered career assistant.
8. Maintain conversation history.
9. Optimize resumes using AI.
10. Generate resumes using AI.
11. Provide downloadable DOCX resumes.
12. Provide a personalized career dashboard.
13. Build a modular backend architecture that can be extended with additional AI providers and features.

---

# ✨ Key Features

## 🔐 Authentication

- User Registration
- User Login
- JWT Authentication
- OAuth2 Password Flow
- Password Hashing
- Protected APIs
- Current User API

## 📄 Resume Management

- Resume Upload
- Resume Storage
- Resume Listing
- Resume Details
- Resume Deletion
- Resume Analysis
- Analysis Retrieval
- Analysis Download

## 🤖 AI Resume Intelligence

- Resume Parsing
- Structured Resume Information
- Skill Extraction
- ATS Analysis
- Strength Analysis
- Weakness Analysis
- AI Recommendations

## 📊 Career Intelligence

- Placement Prediction
- Salary Prediction
- Career Recommendation
- Interview Assistance
- Resume Optimization

## 💬 Career AI Assistant

- AI Career Chat
- Technical Questions
- Career Questions
- Resume Questions
- Conversation History
- New Conversations
- Conversation Rename
- Conversation Delete
- Real-Time Streaming

## ✍️ AI Resume Studio

- Resume Generation
- Resume Optimization
- AI-assisted Resume Creation
- DOCX Resume Download

## 📊 Dashboard

- ATS Score
- Placement
- Salary
- Career
- ATS Analysis
- Resume Status
- Career Overview

---

# 🖥️ Application Walkthrough

The following section demonstrates how the application works from the user's perspective.

---

# 1️⃣ Authentication

## Login

![Login](login.png)

The user starts by logging into the platform.

The login system communicates with the FastAPI authentication API and receives a JWT access token after successful authentication.

---

## Registration

![Registration](register.png)

New users can create an account through the registration interface.

The password is securely hashed before being stored in the database.

---

## Authentication Flow

```text
User
 │
 ▼
Register / Login
 │
 ▼
FastAPI Auth API
 │
 ▼
Validate Credentials
 │
 ▼
Password Verification
 │
 ▼
JWT Access Token
 │
 ▼
Frontend
 │
 ▼
Protected API Requests