from playhouse.shortcuts import model_to_dict

def models_to_dict(models):
	return [model_to_dict(model) for model in models]

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj
