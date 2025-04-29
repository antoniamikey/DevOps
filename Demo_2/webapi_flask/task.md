# Task

1. Write a Dockerfile that creates an image to start the given server (the requirements are in the rquirements.txt file)
    -> siehe Dockerfile
2. Build the image, tag it as webapi
    -> docker build . -t webapi 
3. Run the container and let it reroute the exposed port 8080 to the local port 80
    -> docker run -p 80:8080 webapi 
4. Access the api via your browser on the port 80
    -> localhost:80
5. Stop the container, delete the image
    -> strg + c
    -> docker rmi webapi (maybe gibt es noch noch container die das nutzen, die aber schon geschlossen sind, von denen wird dann die ID angezeigt, ansonsten bekommt man die IDs auch mit <docker ps -a>)
6. Let the app also run by installing it locally (without docker) 
    -> für mac erstmal virtualle Umgebung starten <python3 -m venv .venv>
    -> venv aktivieren <source .venv/bin/activate>
    -> Abhängigkeiten installieren <pip install -r requirements.txt>
    -> in src gehen 
    -> python <start_server.py> , läuft dann auf localhost:8080
    -> venv mit <deactivate> stoppen 