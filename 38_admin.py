def admin_only(func):
    """Decorator that allows execution only if user is 'admin'"""
    def wrapper(user, *args, **kwargs):
        if user != "admin":
            print(f"Access denied for user: {user}")
            return None
        return func(user, *args, **kwargs)
    return wrapper


@admin_only
def delete_database(user):
    print("Database deleted successfully!")

delete_database("guest")   # Not allowed
delete_database("admin")   # Allowed
