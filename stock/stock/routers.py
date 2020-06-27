class LocalDatabaseRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ['currencies']:
            return 'local'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ['currencies']:
            return 'local'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # if obj1._meta.app_label in ['currencies'] and obj2._meta.app_label in ['currencies']:
        return True
        # return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'local':
            if app_label in ['currencies']:
                return True
            else:
                return False
        elif app_label in ['currencies']:
            return False
        return None


class RemoteDatabaseRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label not in ['currencies']:
            return 'remote'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label not in ['currencies']:
            return 'remote'
        return None

    def allow_relations(self, obj1, obj2, **hints):
        if obj1._meta.app_label not in ['currencies']:  # and obj2._meta.app_label not in ['currencies']:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'remote':
            if app_label not in ['currencies']:
                return True
            else:
                return False
        elif app_label not in ['currencies']:
            return False
        return None
