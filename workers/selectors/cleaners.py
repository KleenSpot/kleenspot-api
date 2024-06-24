from models.Cleaners import Cleaner
from django.db.models import Q

def get_cleaner_by_id(cleaner_id):
    """
    Retrieves a cleaner by its ID.

    :param cleaner_id: ID of the cleaner.
    :return: Cleaner object or None if not found.
    """
    try:
        return Cleaner.objects.get(id=cleaner_id)
    except Cleaner.DoesNotExist:
        return None

def get_all_cleaners():
    """
    Retrieves all cleaners.
    """
    return Cleaner.objects.all()

def get_cleaners_by_category(category_name):
    """
    Retrieves all cleaners offering services in a specific category.

    :param category_id: ID of the category.
    :return: QuerySet of Cleaner objects.
    """
    return Cleaner.objects.filter(category__name=category_name)

def search_cleaners(keyword):
    return Cleaner.objects.filter(
        Q(name__icontains=keyword) |
        Q(address__icontains=keyword) |
        Q(category__name__icontains=keyword) |
        Q(contactPerson__icontains=keyword)
    )

def get_cleaner_images(cleaner_id):
    cleaner = get_cleaner_by_id(cleaner_id)
    if cleaner:
        return cleaner.images.all()
    return None

def get_cleaner_details(cleaner_id):
    cleaner = get_cleaner_by_id(cleaner_id)
    if cleaner:
        return {
            "name": cleaner.name,
            "about": cleaner.about,
            "address": cleaner.address,
            "category": cleaner.category.name if cleaner.category else None,
            "contactPerson": cleaner.contactPerson,
            "email": cleaner.email,
            "price": cleaner.price,
            "images": [image.url for image in cleaner.images.all()]
        }
    return None


def get_cleaners_by_service(service_id):
    """
    Retrieves all cleaners offering a specific service.

    :param service_id: ID of the service.
    :return: QuerySet of Cleaner objects.
    """
    return Cleaner.objects.filter(services__id=service_id)



