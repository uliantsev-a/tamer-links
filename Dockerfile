FROM python:3.7
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -yf nginx supervisor \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

# supervisor configure
COPY config/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY config/scripts/entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh

# add project files
ADD backend /opt/api
WORKDIR /opt/api

RUN if [ ! -d logs ]; then mkdir -p logs; fi
RUN if [ ! -f logs/debug.log ]; then touch logs/debug.log; fi
RUN if [ ! -f logs/warning.log ]; then touch logs/warning.log; fi
RUN if [ ! -z "$IGNORE_TESTS" ]; then python manage.py test --noinput; fi

RUN python manage.py collectstatic --noinput
ENV WORKERS = $(cat /proc/cpuinfo | grep \"core id\" | wc -l)

CMD ["/opt/entrypoint.sh"]
#CMD ["/usr/bin/supervisord"]