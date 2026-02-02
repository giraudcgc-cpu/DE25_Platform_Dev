uppgifter\_3



● Mapping

● Endpoint

● HTTP-method

● Query-parameter

● Status Code



Mapping:

I FastAPI innebär detta att du kopplar ihop en specifik URL (t.ex. /users) och en HTTP-metod (t.ex. GET) med en specifik Python-funktion i din kod. 

När någon besöker den adressen, "mappar" FastAPI anropet till rätt funktion så att den körs.



Endpoint:

En endpoint är den specifika adressen (URL:en) på servern dit en användare skickar sin förfrågan för att utföra en viss uppgift



HTTP-method:

Detta är ett "verb" som talar om för servern vad man vill göra med en resurs.

De vanligaste är: 

GET: Hämta data (läsa)

POST: Skapa ny data 

PUT/PATCH: Uppdatera existerande data 

DELETE: Ta bort data



Query-parameter:

Detta är extra information som läggs till i slutet av en URL efter ett frågetecken (?) för att filtrera eller anpassa resultatet

Exempel: I URL:en /items?limit=10 är limit en query-parameter med värdet 10



Status code:

En siffra som servern skickar tillbaka för att berätta hur det gick med anropet:

200 (OK): Allt gick bra 

201 (Created): Något skapades framgångsrikt 

404 (Not Found): Sidan eller resursen hittades inte 

500 (Internal Server Error): Servern kraschade eller något gick fel på insidan

Vill du se ett kodexempel i FastAPI där vi använder alla dessa delar tillsammans? 



---Theory: Delete mapping---



Analysera koden.



@app.delete("/users", status code= status.HTTPS 200\_OK)

def delete\_user(username: str) -> dict\[str:str]:

&nbsp;  for user in userList:

&nbsp;	if user.username == username:

&nbsp;	   userList.remove(user)

&nbsp;	   return {"message": "User deleted"}

&nbsp;  return {"message": "User not found"}





\# notera att nu kommer vi ALLTID att returnera 200 ok även om

\# resultatet ej hittas…



\*\*\*lösning:

@app.delete("/users", status code= status.HTTPS 200\_OK)

def delete\_user(username: str) -> dict\[str:str]:

   for user in userList:

 	if user.username == username:

 	   userList.remove(user)

 	   return {"message": "User deleted"}

   return {"message": "User not found"}



&nbsp;  raise HTTPException(

&nbsp;  	status\_code=status.HTTP\_404\_NOT\_FOUND,

&nbsp;	detail="User not found"

)



\# Vi kan grena ut med HTTPException (glöm inte importera bara)

\# ‘raise’ är likt ‘throw’ inom Java, C#, javascript/typescript, kotlin





// –Uppgift #1– //



/\* INSTRUCTIONS

Skapa ett helt nytt projekt.

Installera rätt bibliotek:

https://fastapi.tiangolo.com/#create-it

Försök hitta hur en installerar!

\*/

// HINT \& Examples

hint(”Leta efter terminal kommandon”)

hint(”Installation inkluderar pydantic”)





// –Uppgift #2– //



/\* INSTRUCTIONS

Skapa en ‘app’ variabel:

from fastapi import FastAPI

app = FastAPI(title="My First API")

Skapa nu en enkel ‘Hello World’

GET-Mapping som använder sig av en

‘Dictionary’

\*/

hint(”@”)

hint(”app”)

hint(”get()”)

hint(”return {}”)





// –Uppgift #3– //



/\* INSTRUCTIONS

Skapa ett nytt ‘package’

Döp den till ‘schema’

Skapa en ny .py fil: Product

class ProductSchema(BaseModel):

&nbsp;TBD: tbd

Inkludera

● id,

● title,

● price,

● description,

● category,

● image

\*/

// HINT \& Examples

hint(”Glöm inte data typer: str, int etc…”)





// –Uppgift #4– //



/\* INSTRUCTIONS

Inom main.py

Skapa en enkel array med produkter:

productList: list\[ProductSchema] = \[

&nbsp;ProductSchema(...),

&nbsp;ProductSchema(...),

&nbsp;ProductSchema(...),

&nbsp;ProductSchema(...),

&nbsp;ProductSchema(...),

]

Hämta ut alla produkter inom en

‘getProducts mapping’

\*/

// HINT \& Examples

hint(”Glöm inte att returnera listan inom ‘def’

också för bättre struktur”)



// –Uppgift #5– //



/\* INSTRUCTIONS

Kolla på URL’n

Fakestore API

https://fakestoreapi.com/products

Skapa nu en till ‘Schema’ klass inom

product.py

Vi har redan definierat de 6 första värden…

\*/

// HINT \& Examples

hint(”Ignorera index elementen. Detta är enbart en

lista med objekt.

Fokusera enbart på objekt”)

hint(”rating”)





// –Uppgift #6– //

&nbsp;Tough nut

/\* INSTRUCTIONS

Konsumera API:et

https://fakestoreapi.com/products

Använd datan för att visa upp alla produkter.

(Notera att allt är en enda stor array)

FACIT finns på nästkommande sidor!

\*/

// HINT \& Examples

hint(”List + For loop”)

hint(”Denna uppgift är svår, ta gärna hjälp av

google eller andra externa resurser”)





// –FACIT– //

&nbsp;Tough nut

from pydantic import BaseModel

class RatingSchema(BaseModel):

&nbsp;rate: float

&nbsp;count: int

class ProductSchema(BaseModel):

&nbsp;id: int

&nbsp;title: str

&nbsp;price: float

&nbsp;description: str

&nbsp;category: str

&nbsp;image: str

&nbsp;rating: RatingS



// –FACIT– //

&nbsp;Tough nut

@app.get("/products" , response\_model =list\[ProductSchema ])

def get\_products () -> list\[ProductSchema ]:

&nbsp;result =

requests.get ("https://fakestoreapi.com/products" )

&nbsp;response\_json = result.json()

&nbsp;products: list\[ProductSchema ] = \[]

&nbsp;for item in response\_json :

&nbsp;product = ProductSchema (\*\*item)

&nbsp;products.append(product)

&nbsp;return list(products)















































## 







