import typer
from rich import print
from cli.email import KCLEmailChecker

app = typer.Typer()
checker =  KCLEmailChecker()

@app.command()
def get_name(email:str):
    if checker.is_correct_format(email):
        print(checker.get_name(email)) 
    else:
        print(checker.incorrect_table())
    
@app.command()
def is_valid(email:str):
    if checker.is_correct_format(email):
        print("Correct email format!")
    else:
        print(checker.incorrect_table())
        

    
if __name__ == "__main__":
    app()