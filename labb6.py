import os

while True:
    try:
        # Låt användaren mata in filnamnet
        fil_namn = input("Skriv namnet på filen med alla studenterna: ")
        # Kolla om filen finns
        if os.path.exists(fil_namn):
            break
        else:
            # Om filen inte finns, skriv ut ett felmeddelande
            print("Filen hittades ej!")
    except Exception as e:
        # Om något annat fel inträffar, skriv ut ett felmeddelande
        print(f"Ett fel uppstod: {str(e)}")


class Skola:
    # Skapa en klass för skolan
    def __init__(self):
        # Skapa tre tomma listor för förnamn, efternamn och personnummer
        self.student_förnamn = []
        self.student_efternamn = []
        self.student_persnr = []

    def importering_förnamn(self):
        # Skapa en metod för att importera förnamn
        with open(fil_namn, "r", encoding="utf-8") as studentfil:
            rad = studentfil.readlines()
            # Loopa igenom filen och lägg till förnamnen i listan
            for i in range(2, len(rad), 3):
                # Ta bort mellanslag och radbrytningar
                studentnamn = rad[i].strip()
                # Lägg till förnamnen i listan
                self.student_förnamn.append(studentnamn)
            studentfil.close()

    def importering_efternan(self):
        # Skapa en metod för att importera efternamn
        with open(fil_namn, "r", encoding="utf-8") as studentfil:
            rad = studentfil.readlines()
            # Loopa igenom filen och lägg till efternamnen i listan
            for i in range(1, len(rad), 3):
                # Ta bort mellanslag och radbrytningar
                studentefternamn = rad[i].strip()
                # Lägg till efternamnen i listan
                self.student_efternamn.append(studentefternamn)
            studentfil.close()

    def importering_personnummer(self):
        # Skapa en metod för att importera personnummer
        with open(fil_namn, "r", encoding="utf-8") as studentfil:
            rad = studentfil.readlines()
            # Loopa igenom filen och lägg till personnumren i listan
            for i in range(0, len(rad), 3):
                # Ta bort mellanslag och radbrytningar
                studentpersnmr = rad[i].strip()
                # Lägg till personnumren i listan
                self.student_persnr.append(studentpersnmr)
            studentfil.close()

    def utskrift_student(self):
        # Skapa en metod för att skriva ut studenterna
        self.importering_förnamn()
        self.importering_efternan()
        self.importering_personnummer()

    def __repr__(self):
        text = "\nHär är alla studenter på KTH:\n"
        # Skapa en loop för att skriva ut studenterna
        for i in range(len(self.student_förnamn)):
            # Skriv ut studenterna
            text += f"Namn: {self.student_förnamn[i]} {self.student_efternamn[i]} Personnummer: {self.student_persnr[i]}\n"
        return text


# Skapa en instans av klassen School
skola = Skola()

" " " Skapar en instans av klassen School " " "

skola.utskrift_student()

print(skola)
