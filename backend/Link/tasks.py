import logging
from datetime import datetime, timezone
from django.conf import settings

from celery.decorators import periodic_task

from datetime import timedelta
from .models import Resource

logger = logging.getLogger('celery')


@periodic_task(run_every=(timedelta(days=settings.CLEANING_TASK_PERIOD)), name="clean_old_resources")
def clean_old_resources():
    logger.info('Clean the old resources was run')

    current_date = datetime.now().replace(microsecond=0)

    limit_date = datetime.fromtimestamp(
        current_date.timestamp() - settings.LIMIT_STORAGE,
        timezone.utc
    )
    Resource.objects.filter(created__lte=limit_date).delete()

    logger.info(f'Resources older {limit_date.isoformat(" ", timespec="minutes")} deleted')
