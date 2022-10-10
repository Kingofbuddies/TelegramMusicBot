from os import getenv
from dotenv import load_dotenv

load_dotenv()


SESSION_NAME = getenv("SESSION_NAME", "BQCn1oAYSbPu5wURRvQEgebiAaxBKO-vYg9-A8HA6upfMDFH4NV22gJuiO9k6H8xKGtGtruqw1lpjJQOKPoD8_g5W9WeJir8-4Boh_TF_OxJ2eiUXJUYmJytJsY8SBbYwaBBoEVAZEpJlT1g2fWR_bTjZY3yGyVpqFQiBYfck7Le7yjVe2MSkrnuvHhFfpse5jG3emmzV9z-qfhW_quhyi6VRRy8TfdNmxH3d3_tY2H2XessUfwMEoZqFALnHUQpAToe9Uc-YggUFQS6qBUbUDoQCPB5DYK_eDdjCVz18KR7zww4Y5LXyH26mwyvch-9zdNC0ONPWOvWz_R2Pol2zrAAAAAU8sPSMA")
BOT_TOKEN = getenv("5769472418:AAGcjFcDnv4d-HHElu7YQd-ffoYVtIw7Crc")

API_ID = int(getenv("10926177"))
API_HASH = getenv("4e880dd4c6a4e7ca887bc2f20c67e0ff
")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "160"))

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
