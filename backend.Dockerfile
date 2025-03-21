# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy necessary files
COPY requirements.txt .
COPY main.py .
COPY model.h5 .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
