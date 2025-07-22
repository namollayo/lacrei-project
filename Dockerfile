# Use a slim Python image for optimization
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Configure Poetry to not create virtualenvs
RUN poetry config virtualenvs.create false

# Copy dependency files and install dependencies
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-interaction --no-ansi --only main

# Copy the project code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
