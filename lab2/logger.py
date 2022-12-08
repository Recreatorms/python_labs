from time import strftime, localtime


class Singleton(type):
    _instances = {}

    # cls ~~ class
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print("call")
            cls._instances[cls] = super(Singleton,
                                        cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class log(metaclass=Singleton):
    def log(self, status, message):
        if not (status == "DEBUG" or
                status == "INFO" or
                status == "WARNING" or
                status == "ERROR" or
                status == "CRITICAL" or
                status == "FATAL"):
            print("Bad status")       
            return
        time = strftime("%H:%M:%S", localtime())
        try:
            with open('log.log', 'a') as f:
                f.write(f"[{status}]\t<{time}>\t\"{message}\"\n")
        except FileNotFoundError:
            with open('log.log', 'w') as f:
                f.write(f"[{status}]\t<{time}>\t\"{message}\"\n")


log = log()
log.log("DEBUG", "message1")
log.log("DEBUG", "message2")
log.log("DEBUG", "message3")
