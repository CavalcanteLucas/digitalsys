from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from proposals.models import Proposal
import pika

@receiver(post_save, sender=Proposal)
def send_proposal_to_rabbitmq(sender, instance, created, **kwargs):
    if created:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.RABBITMQ_HOST))
        channel = connection.channel()
        channel.queue_declare(queue=settings.RABBITMQ_QUEUE)
        message = f"{instance.pk}"
        channel.basic_publish(exchange='', routing_key=settings.RABBITMQ_QUEUE, body=message)
        connection.close()
