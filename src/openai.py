# import os
# import sys

# project_relative_dir = "../"
# sys.path.append(project_relative_dir)

import json
from openai import OpenAI

from secret.secret import api_key

class MyOpenAI():

    def __init__(self, key = None):

        if not key:
            key = api_key
            print("[Info] Used test api key")

        self.client = OpenAI(
            # This is the default and can be omitted
            api_key=key # os.environ.get("OPENAI_API_KEY"),
        )

    def testing(self):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="gpt-3.5-turbo",
        )
        return chat_completion

    def ask(self, question, details, output_format: dict = {}):

        system_content = "You only output JSON."
        if output_format:
            # add output format
            system_content += json.dumps(output_format, indent=4)

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={ "type": "json_object" },
             messages=[
                {f"role": "system", "content": system_content},
                {"role": "user", "content": question + "\n" + details}
            ]
        )
        return response
