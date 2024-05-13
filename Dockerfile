# 
FROM python:3.9

#  Sets the working directory in Docker. Any subsequent command will be relative to this folder.
WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copies aoo folder in the host machine to the /app folder within the Docker container
COPY ./app /app

# 
CMD ["fastapi", "run", "main.py", "--port", "80"]