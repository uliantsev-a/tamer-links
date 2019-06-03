from datetime import datetime, timezone
from django.conf import settings

from celery.decorators import periodic_task
from celery.utils.log import get_logger

from datetime import timedelta
from .models import Resource

logger = get_logger('django_celery')


@periodic_task(run_every=(timedelta(**settings.CLEANING_TASK_PERIOD)),
               name="clean_old_resources", ignore_result=True)
def clean_old_resources():
    logger.info('Clean the old resources was run')

    current_date = datetime.now().replace(microsecond=0)

    limit_date = datetime.fromtimestamp(
        current_date.timestamp() - settings.LIMIT_STORAGE,
        timezone.utc
    )
    old_resources = Resource.objects.filter(created__lte=limit_date)
    if old_resources.exists():
        old_resources.delete()
        logger.info(f'Resources older {limit_date.isoformat(" ", timespec="minutes")} deleted')
    logger.info('Clean the old resources finished')
