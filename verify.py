import base64
import hashlib
import hmac

channel_secret = zlO7n7p65AleR7iu0zB+yk8i8juIKfxHd6JqySBY3X/Bxw35QizAG9DV/aomX9VE4LLu3YICTsBl5JTAUij2CIApeWXd4jc3E8uJ1xgPClzj+YqeP7DsKn2bbFjSoA5qnx9V6a/fa4B8lTxMTlVUtwdB04t89/1O/w1cDnyilFU= # Channel secret string
body = ... # Request body string
hash = hmac.new(channel_secret.encode('utf-8'),
    body.encode('utf-8'), hashlib.sha256).digest()
signature = base64.b64encode(hash)
# Compare X-Line-Signature request header and the signature
