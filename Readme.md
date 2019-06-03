## TamerLinks   
The simple app for link reduction. It's similar to __bit.ly__  
or other the service for making short links from original URLs 


App include next option:   
- Celery worker periodic delete old resources (links)  
    for this a settings.py in django have next options:  
    ```python
    # how often worker will start the clear script
    CLEANING_TASK_PERIOD = {
        'days': 30
        'seconds': 30
    }
    
    # how old time should be after create for delete link
    LIMIT_STORAGE = 3600 * 24 * 30
    ```
- Backend app (from Django) with API endpoinds for create and getting links of current session.   
  
    List links use pagination and access by session only.
- web client on Vue.
- Docker config for running the applications together

**Fast way for running:**
```sh 
docker-compose build  
docker-compose up  
```
And connect to 80 port to gateway host of docker network or to nginx host:
```sh
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' tamerlinks_nginx
```

#### Configure
Before run necessary set settings.  
Fill the `.env` file in project root directory.  
Next variables is example for settings:
```sh
DEBUG=TRUE
DATA_SAVE_PATH=/tmp

DEBUG=TRUE
MYSQL_DATABASE=TamerLinks
MYSQL_USER=m_user
MYSQL_PASSWORD=some_pass
MYSQL_ROOT_PASSWORD=root
MYSQL_HOST=mysql
MYSQL_PORT=3306
```
If you have outside instance with DB, can disable _mysql_ image in docker-compose.yml  
