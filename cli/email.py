import re
from rich.table import Table
import webbrowser
class KCLEmailChecker():
    
    def is_correct_format(self,email):
        regex=re.compile(r"((k)([0-9]{7,8})(\@)(kcl\.ac\.uk))|(([a-z]{2,})((\.)|(\.([0-9]|[a-z]){1}\.))([a-z]{2,})(\@)(kcl\.ac\.uk))")
        if (regex.match(email)):
            return True
        return False

    def get_name(self,email):
        regex = re.compile(r"[a-z]{1}")
        if self.is_correct_format(email):
            full_name = re.split(r"\@",email)[0]
            if full_name[0]=="k":
                return f'K Number: {full_name.capitalize()}'
            period = re.split(r"\.",full_name)
            if len(period) == 3:
                first_name = re.split(r"\.",full_name)[0]
                middle_name = re.split(r"\.",full_name)[1]
                last_name = re.split(r"\.",full_name)[2]
                if regex.match(middle_name):
                    return f"{first_name.capitalize()} {middle_name.capitalize()}. {last_name.capitalize()}"                
                else:
                    return f"{first_name.capitalize()} {last_name.capitalize()}"                      
            first_name = re.split(r"\.",full_name)[0]
            last_name = re.split(r"\.",full_name)[1]
            return f"{first_name.capitalize()} {last_name.capitalize()}"
        return "Incorrect Format"
    
    def send_email(self, email):
        webbrowser.open(f'mailto:?to={email}',1)  
        
    
    def incorrect_table(self):
        table = Table(title=" Incorrect email format! ",show_lines=True)
        table.add_column(header="Correct formats:",style="magenta")
        table.add_row("k<7-8 digit number>@kcl.ac.uk")
        table.add_row("firstname.lastname@kcl.ac.uk")
        table.add_row("firstname.[0-9 or a-z single character].lastname@kcl.ac.uk")
        return table

