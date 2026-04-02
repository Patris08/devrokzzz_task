# DevOps Task 

Minimal Flask application demonstrating Docker, Docker Compose, GitHub Actions CI, and Ansible automation.

---

## Table of Contents
- [About](#about)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Installation & Running](#installation--running)
  - [Using Docker](#using-docker)
  - [Using Docker Compose](#using-docker-compose)
  - [Using Ansible](#using-ansible)
  - [Using WSL (Windows Subsystem for Linux)](#using-wsl-windows-subsystem-for-linux)
  - [CI/CD](#cicd)

---

## About
This repository contains a simple Python Flask application for a recruitment task at Rokezzz. The goal is to demonstrate practical DevOps skills by:

- Creating a minimal Flask application.
- Containerizing the application with Docker.
- Automating builds and testing with GitHub Actions.
- Deploying using Docker Compose or Ansible.

The application exposes a single endpoint at `/` that returns a confirmation message.

---

## Technologies
- **Python 3.11**
- **Flask**
- **Docker**
- **Docker Compose**
- **GitHub Actions**
- **Ansible**
- **WSL** (optional, for Windows users)

---

## Project Structure
- `app.py` – Minimal Flask application.
- `Dockerfile` – Docker image definition.
- `docker-compose.yml` – Orchestrate container(s) with Docker Compose.
- `.github/workflows/main.yml` – GitHub Actions workflow for build and test.
- `playbook.yml` – Ansible playbook to run the container.

---

## Installation & Running

### Using Docker

 ## Key Docker commands
```bash
# Build the Docker image
docker build -t devops_app .

# Run the container
docker run -p 5000:5000 devops_app

# Check running containers
docker ps

# Test the application
curl http://localhost:5000
```
### Using Ansible


## Start container using Ansible
```bash
# Run the playbook to start the container
ansible-playbook playbook.yml

# Verify running containers
docker ps

# Test the application
curl http://localhost:5000
Using WSL (Windows Subsystem for Linux)


Steps for Windows users with WSL

# Open WSL terminal
wsl.exe -d Ubuntu

# Navigate to project directory
cd /path/to/project

# Follow Docker, Docker Compose, or Ansible instructions above inside WSL
```
### CI/CD


## GitHub Actions workflow
```bash
Workflow located at .github/workflows/main.yml
Performs:
Builds the Docker image
Runs the container in detached mode
Tests the / endpoint to confirm the app is running
Triggered automatically on pushes to the main branch
```
