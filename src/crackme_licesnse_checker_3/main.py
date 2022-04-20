from random import randint

import typer

app = typer.Typer()


def random(max: int) -> str:
    numbers = []
    while sum(numbers) < max:
        numbers.append(randint(0, 9))
    total: int = sum(numbers)
    diff = total - max
    numbers[-1] -= diff
    return "".join([str(n) for n in numbers])


@app.command()
def keygen() -> None:
    typer.echo(random(50))


if __name__ == "__main__":
    app()
