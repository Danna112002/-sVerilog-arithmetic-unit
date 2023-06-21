#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>
#include <stdbool.h>
#include <openssl/sha.h>
#include <errno.h>
#define BUF_SIZE 4096
//Przy kompilacji dużo warningów, gdyż ponieważ komendy używane do hashu są już przestarzałe?
//jednakowo nawet z tymi warningami działa poprawnie.

//Sprawdzanie obecności pliku - funkcja 
int fileExistence(const char *UserInput)
{
    const char* path = UserInput; //wskaźnik do zmiennej przechowującej ścieżkę do hashowanego pliku   
    FILE *file; //wskażnik do struktury FILE potrzebnej do hashu
    file = fopen(path, "rb");
        if (file == NULL) 
    {
        //zwracany jest tutaj również kod błędu i program się kończy 
        printf("Błąd otwierania pliku: %s\n", strerror(errno));
        printf("KONIEC PROGRAMU!! \n");
        exit(EXIT_FAILURE);
        return 1;
    }
    else 
    return 0;
}

//właściwa funkcja hashująca
int hash(const char *filePath) 
{
    
    const char* path = filePath; //wskaźnik do zmiennej przechowującej ścieżkę do hashowanego pliku
    FILE *file; //wskażnik do struktury FILE potrzebnej do hashu
    unsigned char buffer[BUF_SIZE]; // bufor tablicy znaków 
    unsigned char hash[SHA256_DIGEST_LENGTH]; // gotowy hash 
    SHA256_CTX sha256; //inicjalizacja struktury hashującej 
    int bytesRead; // zmienna całkowita przechowująca odczytane bity 
    
    printf("Ścieżka pliku przekazana do funcji: %s\n", path);
    // zmienna file jest wskaźnikiem do otwartego pliku, który chcemy hashować
    file = fopen(path, "rb");
    //inicjalizacja hashu wg tego, co napiane w bibliotece
    SHA256_Init(&sha256);
    //pętla hashująca bit po bicie 
    while ((bytesRead = fread(buffer, 1, BUF_SIZE, file)) > 0) 
    {
        SHA256_Update(&sha256, buffer, bytesRead);
    }
    //finalny kształt hashu 
    SHA256_Final(hash, &sha256);
    fclose(file);
    //wypisz hash w hexadecymalnym formacie
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) 
    {
        printf("%02x", hash[i]);
    }
    printf("\n");
    return 0;
}
int main(int argc, char *argv[]) 
{
    //warunek sprawdzajacy, czy liczba argumentów przekazanych do funkcji jest równa 2, jak nie, program się kończy
    if (argc != 2) 
    {
        printf("Aby użyć programu po wpisaniu: %s", argv[0]);
        printf(" wpisz poprawnie ścieżkę do pliku!\n KONIEC PROGRAMU!! \n");
        exit(EXIT_FAILURE);
        return 1;
    }
    //wskaźnik do drugieo elementu wektora argumentów przekazanych do funkcji 
    const char *filePath = argv[1];
    //dupokryjka error-handlingowa, niech wypisuje 2 razy ścieżkę do pliku, żeby zobaczyć, gdzie się wywraca w razie czego
    printf("Ścieżka do hashowanego pliku przekazana do terminalu: %s\n", filePath);
    if (fileExistence(filePath) == 0)
    {
        hash(filePath);
    }
    return 0;
}
/* przykładowe pliki do hashowania
/home/ania/Pulpit/Studia/PROS/LaboratoriumC02/text.txt
/home/ania/Pulpit/SuperiorDomekRozliczenie.xlsx
*/