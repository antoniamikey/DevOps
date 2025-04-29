# Task

Now, we want to get the same app from the docker-compose example running on K8s.

1. We need the same Dockerfile as in the docker-compose example.
    -> easy
2. I have already provided the deployment files in the deploy folder. Familiarize with them. In the web deployment, the image is taken from docker.io/gauss71248/webapi_k8s, i.e., from a page on dockerhub. Push your own image to dockerhub (create your own account) and rewrite the deployment accordingly.
    -> create account, create repo (webapi)
    -> web-deployment den image link ändern zum repo 
    -> <docker login> um sich bei Docker Hub einzuloggen
    -> docker image bauen und direkt taggen <docker build . -t antoniamikey/webapi:webapi1>
    -> ansonsten kann das image auch im Nachhinein getagged werden, dazu <docker image ls> die images anzeigen und den repo namen nehmen (hier webapi1) <docker tag webapi1 antoniamikey/webapi:webapi1>
    -> docker push antoniamikey/webapi:webapi1
    !!! es können nur images gepushed werden, die den repo namen tragen !!!
3. Run the app in K8s.
    -> <minikube start>
    -> <kubectl apply -f deploy/>
    -> <kubectl scale deployment web --replicas=5>
4. Now, we want to scale out the web deployment to 5 replicas. Do it. 
    -> <kubectl scale deployment web --replicas=5>
5. The out scaling works like a load balancer. How can we make the load balancing transparent? Can you modify the code that we can see the hostname of the requested pod?
    -> siehe start_server
6. Modify the source code accordingly, deploy with 5 replicas, and verify the different hostnames after multiple accesses.
    -> Code ändern, <kubectl delete -f deploy/> <docker build> <docker push> <kubectl apply -f deploy/>
    -> web-c86c7cccb-bdf4c | web-c86c7cccb-fbbrp | web-c86c7cccb-qkh96 | web-c86c7cccb-xsx85 | web-c86c7cccb-h4mn4
7. Remove the deployment.
    
