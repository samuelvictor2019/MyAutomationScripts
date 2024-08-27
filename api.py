import requests
import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

SOURCE_URL = "http://192.168.3.202"
SOURCE_API_KEY = ""
SOURCE_API_SECRET = ""

TARGET_URL = "http://192.168.3.101"
TARGET_API_KEY = ""
TARGET_API_SECRET = ""

source_headers = {
    "Authorization": f"token {SOURCE_API_KEY}:{SOURCE_API_SECRET}",
    "Content-Type": "application/json"
}

target_headers = {
    "Authorization": f"token {TARGET_API_KEY}:{TARGET_API_SECRET}",
    "Content-Type": "application/json"
}

def fetch_sales_invoice():
    try:
        response = requests.get(f"{SOURCE_URL}/api/resource/Sales Invoice", headers=source_headers, parameters=)
        response.raise_for_status()
        return response.json()["data"]
    except Exception as e:
        logger.error(f"Error fetching invoices: {e}")

def get_user_details(user_id):
    try:
        response = requests.get(f"{SOURCE_URL}/api/resource/User/{user_id}", headers=source_headers)
        response.raise_for_status()
        user_details = response.json()["data"]
        return user_details
    except Exception as e:
        logger.error(f"Error fetching user details")
        return []

def invoice_exists_in_target(invoice_name):
    try:
        

























































