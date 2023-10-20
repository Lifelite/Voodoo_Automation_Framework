from urllib.request import urlopen
import VD_Connectors
import MySQL

url = "http://www.acsgaleagues.com/"

page = urlopen(url)

pageContents = page.read()

html = pageContents.decode("utf-8")

db = VD_Connectors.Database()
q = MySQL.Query(db)


class ACSWebsite:

    def race_grid_calculator(self, player1, player2):
        