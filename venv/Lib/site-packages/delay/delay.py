from threading import Timer

def delayed(seconds):
    def decorator(f):
        def wrapper(*args, **kargs):
            t = Timer(seconds, f, args, kargs)
            t.start()
        return wrapper
    return decorator

