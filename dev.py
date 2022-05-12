import click
import yaml
import shlex
from subprocess import Popen

with open("./dev.yml", "r") as f:
    YML = yaml.safe_load(f)

def run(s: str):
    Popen(shlex.split(s))

class Funcs:
    def favicons(*args):
        for k, v in YML["favicons"].items():
            for vk, vv in v.items():
                run(f'magick "./public/static/favicons/test.png" -scale "{vv}" "./public/static/favicons/{vk}.{k}"')

@click.command()
@click.argument("func")
@click.argument("args", nargs=-1)
def main(func, args):
    try:
        getattr(Funcs, func)(*args)
    except:
        run(f'./dev.sh {"".join(args)}')

if __name__ == "__main__":
    main()