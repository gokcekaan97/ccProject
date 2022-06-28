First we have to build docker image with
docker build -t ccapp .
after build image we deploy container
docker run -d --name mycontainer -p 80:80 ccapp
we have 3 sites
localhost/ --- welcome page
localhost/input/ --- taking the input page
localhost/calculate/ --- after the taking input this page shows the result 
