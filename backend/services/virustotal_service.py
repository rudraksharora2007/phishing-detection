import requests


def check_virustotal(url: str, api_key: str):
    if not api_key:
        return {"enabled": False}
    try:
        response = requests.post(
            "https://www.virustotal.com/api/v3/urls",
            headers={"x-apikey": api_key},
            data={"url": url},
            timeout=10,
        )
        if response.status_code not in (200, 201):
            return {"enabled": True, "error": "Unable to query VirusTotal"}
        return {"enabled": True, "status": "submitted"}
    except Exception:
        return {"enabled": True, "error": "VirusTotal request failed"}
