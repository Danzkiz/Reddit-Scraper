# happy-sentiment-analysis

## Configuration

### 1. Install docker

MacOS: https://docs.docker.com/docker-for-mac/install/

Windows: https://docs.docker.com/docker-for-windows/install/

_Note: This step can be skipped if docker is already installed_

### 2. Obtain Google Application credentials 
Get Google Application credentials in a JSON file from your Google Cloud account. Place the file in the `credentials` folder and name it `google_application_credentials.json` - see `credentials/google_application_credentials.json.template` for an example.

### 3. Import csv files
Place the csv file that are to be analyzed in the `csv` folder. The docker container will be able to access this folder while it is running.

### 4. Configure docker-compose.yml
Copy and rename `docker-compose.yml.template` to `docker-compose.yml`. 

In `docker-compose.yml`, find the line that says `command: ["python", "sentiment_analysis.py", "some_csv_file.csv"]` and change `some_csv_file.csv` according to the filename of the csv file you placed in the `csv` folder in the previous step.

## Building

Execute `build.sh` to build the docker container
```bash
$ ./build.sh develop
```

_note_: You only have to build the docker container, if you have added new python dependencies or haven't build it before. 

## Running

Execute:
```bash
$ docker-compose up
```

