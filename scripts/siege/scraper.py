import json
import datetime as dt 

import typer
from sh import siege


def sample(time=1, concurrency=100):
    """Run siege and collect stats."""
    out = siege(
        "https://calmcode.io", 
        "--benchmark", 
        "--time", 
        f"{time}s", 
        "--concurrent", 
        f"{concurrency}"
    )
    print(out.stdout)
    # data = json.loads(out.stdout)
    # data['datetime'] = str(dt.datetime.now())[:19]
    # data['time'] = time
    # data['concurrency'] = concurrency
    # with open("a.jsonl", "a") as f:
    #     f.write(json.dumps(data) + '\n')

if __name__ == "__main__":
    typer.run(sample)
