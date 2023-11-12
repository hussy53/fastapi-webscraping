
# Simple Webscraping & FastApi Project

Imagine you are a historical explorer and are interested in retreiving information on historical events that have taken place over the years!

Task: **Create an API using FastAPI to provide us information on important events that have occurred on a given day/month or throughout the year**. Instructions given below.

Description: This application does basic GET operations. Take advantage of the operations to explore and retreive information that interests you.

Credits 1: https://www.youtube.com/watch?v=Nni0HX9O4hc

Credits 2: https://www.youtube.com/watch?v=hOipXax0Ogw


## Prerequisites
On your **virtual environment** (deployment section):
- pip install **virtualenv**
- pip install **requests**
- pip install **beautifulsoup4**
- pip install **fastapi**
- pip install **uvicorn[standard]**
## Deployment

Once the folder is downloaded on your local machine, open up your preferred editor, go to the project directory (../fastapi-webscraping/src) and run:

 On windows:

```bash
python -m venv .
```

```bash
.\Scripts\activate
```

```bash
pip install fastapi
```

```bash
pip install "uvicorn[standard]"
```

```bash
uvicorn main:app --reload
```

On mac:

Follow this link to start the virtual environment on mac os: https://programwithus.com/learn/python/pip-virtualenv-mac




## API Reference

#### Root webpage

```http
  local_host/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| - | `GET` | Create a welcome page when the app loads up |

#### Fetch items

```http
  local_host/events
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| - | `GET` | Fetches all the historical events stored in the json file |

#### Fetch items

```http
  local_host/events/today
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `-` | `GET` | Fetches all the historical events that happened today |

#### Fetch items

```http
  local_host/events/{month}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `month` | `GET` | Fetches all the historical events that happened on the specified month |

#### Fetch items

```http
  local_host/events/{month}/{day}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `month` | `GET` | Fetches all the historical events that happened on the specified month |
| `day` | `GET` | Fetches all the historical events that happened on the specified day |



## Appendix

**NOTE**: Once you download the folder, make sure you delete *events.json* file. The JSON file is to be created from the *collect_events.py* file

Order of running the files:

- Run the *collect_events.py* file to create the JSON file
```bash
python ./collect_events.py
```
- Then run the *main.py* file endpoints
```bash
uvicorn main:app --reload
```

