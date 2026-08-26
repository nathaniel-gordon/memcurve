"""Runtime-built fake secrets for security tests.

Values are assembled at runtime so static secret-scanning patterns are not
stored verbatim in the repository.
"""


def _join(*parts: str) -> str:
    return "".join(parts)


def aws_access_key() -> str:
    return _join("AK", "IA") + "I" + ("O" * 14) + "SFODNN7EXAMPLE"


def aws_access_key_alt() -> str:
    return _join("AK", "IA") + "I44QH8DHBEXAMPLE"


def ghp_token() -> str:
    return _join("gh", "p_") + ("1" * 36)


def ghp_token_short() -> str:
    return _join("gh", "p_") + ("1" * 32)


def gho_token() -> str:
    return _join("gh", "o_") + ("a" * 36)


def ghu_token() -> str:
    return _join("gh", "u_") + "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef"


def ghs_token() -> str:
    return _join("gh", "s_") + ("a" * 36)


def ghr_token() -> str:
    return _join("gh", "r_") + ("1" * 36)


def openai_key() -> str:
    return _join("sk", "-") + ("1" * 48)


def openai_key_alt() -> str:
    return _join("sk", "-") + ("a" * 48)


def anthropic_key() -> str:
    return _join("sk", "-ant-api03-") + ("1" * 80)


def anthropic_key_hyphenated() -> str:
    return _join("sk", "-ant-api03-abcd-efgh-ijkl-mnop-qrst-uvwx-yzAB-CDEF-GHIJ-KLMN-OPQR-STUV-WXYZ-1234-5678-90ab-cdef-ghij-klmn")


def google_api_key() -> str:
    return _join("AI", "zaSyD") + ("1" * 35)


def google_api_key_url() -> str:
    return _join("AI", "zaSyAbCdEfGhIjKlMnOpQrStUvWxYz") + "1234567"


def slack_bot_token() -> str:
    return _join("xox", "b-") + "1234567890-1234567890123-abcdefghijklmnopqrstuvwx"


def slack_user_token() -> str:
    return _join("xox", "p-") + "1234567890-1234567890-abcdefghijklmnopqrstuvwx"


def slack_app_token() -> str:
    return _join("xox", "a-") + "1234567890-1234567890123-abcdefghijklmnopqrstuvwx"


def jwt_token() -> str:
    return (
        _join("eyJ", "hbGciOiJIUzI1NiJ9.")
        + "eyJzdWIiOiIxMjM0NTY3ODkwIn0."
        + "dozjgNryP4J3jVmNHl0w5N_XgL0n3I9PlFUP0THsR8U"
    )


def jwt_bearer_token() -> str:
    return (
        _join("eyJ", "hbGciOiJSUzI1NiJ9.")
        + "eyJpc3MiOiJodHRwczovL2V4YW1wbGUuYXV0aDAuY29tLyJ9."
        + "abc123def456ghi789jkl012mno345pqr678stu901vwx234yz"
    )


def rsa_private_key_block() -> str:
    header = _join("-----BEGIN ", "RSA ", "PRIVATE KEY-----\n")
    footer = _join("-----END ", "RSA ", "PRIVATE KEY-----")
    return header + "MIIEpAIBAAKCAQEA1234567890abcdefghijklmnop\n" + footer


def pkcs8_private_key_block() -> str:
    header = _join("-----BEGIN ", "PRIVATE KEY-----\n")
    footer = _join("-----END ", "PRIVATE KEY-----")
    return header + "MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC\n" + footer


def pkcs8_private_key_header() -> str:
    return _join("-----BEGIN ", "PRIVATE KEY-----\n")
