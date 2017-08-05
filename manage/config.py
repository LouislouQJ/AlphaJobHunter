from datetime import datetime, timedelta

config = dict()
config["MAX_PAGE_RANGE"] = 50
config["KEY_TIMESTAMP"] = datetime.now() - timedelta(days=30)
