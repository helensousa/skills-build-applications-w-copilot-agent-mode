from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Initialize the MongoDB database with the required collections and indexes'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Create collections if they do not exist
        collections = ['users', 'teams', 'activity', 'leaderboard', 'workouts']
        for collection in collections:
            if collection not in db.list_collection_names():
                db.create_collection(collection)

        # Remove duplicate documents in users collection
        if 'users' in db.list_collection_names():
            pipeline = [
                {"$group": {
                    "_id": "$email",
                    "uniqueIds": {"$addToSet": "$_id"},
                    "count": {"$sum": 1}
                }},
                {"$match": {"count": {"$gt": 1}}}
            ]
            duplicates = list(db['users'].aggregate(pipeline))
            for duplicate in duplicates:
                uniqueIds = duplicate["uniqueIds"]
                db['users'].delete_many({"_id": {"$in": uniqueIds[1:]}})

        # Create unique index for users collection if it does not exist
        if 'users' in db.list_collection_names():
            indexes = db['users'].index_information()
            if 'email_1' not in indexes:
                db['users'].create_index("email", unique=True)

        self.stdout.write(self.style.SUCCESS('Database initialized successfully'))
