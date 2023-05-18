import sentry_sdk
from sentry_sdk import configure_scope
from sentry_sdk import capture_message, capture_exception

sentry_sdk.init("https://2131369168c2450694a907ace884106d@o4505203280838656.ingest.sentry.io/4505203320356864")

with configure_scope() as scope:
    scope.set_tag("GG", "EZ")
    scope.set_tag("Lab", "6")

capture_message("Деление")

def division(x, y):
    return x / y

def void():
    return z
    
try:
    result = division(1, 0)
except Exception as e:
    capture_exception(e)

try:
    v = void()
except Exception as e:
    capture_exception(e)











