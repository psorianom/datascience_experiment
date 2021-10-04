echo "Remove image"
docker rm -f datascience-experiment
echo "Build image"
docker build -t datascience-experiment .

echo "Run container"
docker run -d -p 8050:80 --name datascience-experiment datascience-experiment